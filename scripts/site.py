#!/usr/bin/env python3
"""Validate public content, build a clean artifact, or serve it locally."""

import argparse
from functools import partial
from html.parser import HTMLParser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import re
import shutil
import sys
import tempfile
from urllib.parse import unquote, urljoin, urlsplit


ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"
DIST = ROOT / "dist"
ORIGIN = "https://cybermaak.dev"
ROUTES = ("index.html", "polytray/index.html", "maakdown/index.html", "khatmah/index.html")
EXTENSIONS = {
    ".html", ".css", ".js", ".json", ".xml", ".txt", ".webmanifest",
    ".png", ".jpg", ".jpeg", ".webp", ".avif", ".gif", ".svg", ".ico",
    ".woff", ".woff2", ".mp4", ".webm",
}
CSS_URL = re.compile(r"url\(\s*['\"]?([^)'\"\s]+)['\"]?\s*\)")


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.references = []
        self.ids = set()
        self.canonicals = []
        self.problems = []
        self.has_title = False
        self.feed(text)
        self.references.extend((value, False) for value in CSS_URL.findall(text))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "title":
            self.has_title = True
        if tag == "img" and "alt" not in attrs:
            self.problems.append("image missing alt attribute")
        for attr in ("href", "src", "poster"):
            if attrs.get(attr):
                self.references.append((attrs[attr], tag == "a" and attr == "href"))
        if tag == "link" and "canonical" in attrs.get("rel", "").split():
            self.canonicals.append(attrs.get("href", ""))
        if tag == "meta" and attrs.get("property", attrs.get("name")) in {
            "og:image", "twitter:image", "og:url",
        }:
            self.references.append((attrs.get("content", ""), False))


def validate(directory):
    """Check the actual publishable tree; never search or copy sibling repos."""
    problems = []
    files = []
    if directory.is_symlink() or not directory.is_dir():
        raise ValueError(f"Expected a real content directory: {directory}")
    directory = directory.resolve()
    for path in sorted(directory.rglob("*")):
        name = path.relative_to(directory).as_posix()
        if path.is_symlink():
            problems.append(f"{name}: symlinks are not publishable")
            continue
        if any(part.startswith(".") for part in Path(name).parts) and name != ".nojekyll":
            problems.append(f"{name}: hidden repository/local content is not publishable")
            continue
        if path.is_dir():
            continue
        if not path.is_file():
            problems.append(f"{name}: expected a regular file")
            continue
        if path.stat().st_nlink != 1:
            problems.append(f"{name}: hard links are not publishable")
        if name not in {"CNAME", ".nojekyll"} and path.suffix.lower() not in EXTENSIONS:
            problems.append(f"{name}: unsupported public file type")
        files.append(path)

    # Refuse an unsafe tree before opening or copying its contents.
    if problems:
        raise ValueError("\n".join(problems))

    for route in (*ROUTES, "404.html", "CNAME", ".nojekyll"):
        if not (directory / route).is_file():
            problems.append(f"Missing required public file: {route}")
    cname = directory / "CNAME"
    if cname.is_file() and cname.read_text().strip() != "cybermaak.dev":
        problems.append("CNAME must retain cybermaak.dev until the domain plan changes")

    pages = {path: Page(path.read_text()) for path in files if path.suffix == ".html"}
    for path, page in pages.items():
        name = path.relative_to(directory).as_posix()
        problems.extend(f"{name}: {problem}" for problem in page.problems)
        if not page.has_title:
            problems.append(f"{name}: missing page title")
        if path.name == "index.html":
            expected = ORIGIN + "/" + name.removesuffix("index.html")
            if page.canonicals != [expected]:
                problems.append(f"{name}: canonical must be {expected}")

    for path in files:
        name = path.relative_to(directory).as_posix()
        if path in pages:
            references = pages[path].references
        elif path.suffix == ".css":
            references = [(value, False) for value in CSS_URL.findall(path.read_text())]
        else:
            continue
        for value, check_fragment in references:
            if not value or value.startswith(("data:", "mailto:", "tel:")):
                continue
            url = urlsplit(urljoin(ORIGIN + "/" + name, value))
            if url.scheme not in {"http", "https"}:
                problems.append(f"{name}: unsupported URL scheme in {value}")
                continue
            if url.netloc != "cybermaak.dev":
                continue
            target = (directory / unquote(url.path).lstrip("/")).resolve()
            if not target.is_relative_to(directory.resolve()):
                problems.append(f"{name}: reference escapes public directory: {value}")
                continue
            if target.is_dir():
                target /= "index.html"
            if not target.is_file():
                problems.append(f"{name}: missing local destination: {value}")
            elif check_fragment and url.fragment and target in pages:
                if unquote(url.fragment) not in pages[target].ids:
                    problems.append(f"{name}: missing anchor: {value}")

    if problems:
        raise ValueError("\n".join(problems))
    return len(files), len(pages)


def build():
    validate(PUBLIC)
    if DIST.is_symlink() or (DIST.exists() and not DIST.is_dir()):
        raise ValueError("dist must be a generated directory, not a symlink or file")
    with tempfile.TemporaryDirectory(prefix=".site-build-", dir=ROOT) as temporary:
        staged = Path(temporary) / "dist"
        shutil.copytree(PUBLIC, staged)
        counts = validate(staged)
        if DIST.exists():
            shutil.rmtree(DIST)
        staged.rename(DIST)
    print(f"Built dist/: {counts[0]} public files, {counts[1]} HTML pages", flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("check", help="validate the public tree and local references")
    commands.add_parser("build", help="validate and copy public/ to a clean dist/")
    serve = commands.add_parser("serve", help="build and preview dist/ on localhost")
    serve.add_argument("--port", type=int, default=4173)
    args = parser.parse_args()
    try:
        if args.command == "check":
            files, pages = validate(PUBLIC)
            print(f"Checked {files} public files and {pages} HTML pages")
        else:
            build()
        if args.command == "serve":
            handler = partial(SimpleHTTPRequestHandler, directory=str(DIST))
            with ThreadingHTTPServer(("127.0.0.1", args.port), handler) as server:
                print(f"Preview: http://127.0.0.1:{args.port}", flush=True)
                server.serve_forever()
    except (ValueError, OSError) as error:
        print(f"Website check failed: {error}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())

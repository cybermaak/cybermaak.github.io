#!/usr/bin/env python3
"""Serve only the local design board and selected public media on loopback."""

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import argparse
from pathlib import Path
import mimetypes
from urllib.parse import urlsplit

HERE = Path(__file__).resolve().parent
MEDIA = HERE / "baseline-media"
FILES = {"/": HERE / "index.html"}
FILES.update({"/" + name: HERE / name for name in (
    "01-warm-paper.png", "02-ink-and-gold.png", "03-quiet-editorial.png",
    "01-warm-paper.html", "02-ink-and-gold.html", "03-quiet-editorial.html",
    "proposal.css", "04-quiet-editorial-refined.html", "04-quiet-editorial-refined.css",
    "04-quiet-editorial-refined.js",
)})
FILES.update({"/staged-media/" + name: HERE / "staged-media" / name for name in (
    "icon.jpg", "page.png", "dark.png", "landscape.png", "sharing.png", "tracking.png",
    "bookmarks.png", "focus-en.png", "focus-ar.png",
    "sharing-rendered-preview.png", "app-store-badge.svg",
    "page-ar.png", "tracking-ar.png", "bookmarks-ar.png", "dark-ar.png",
    "landscape-ar.png", "sharing-rendered-preview-ar.png", "landscape-dark-en.png",
    "landscape-dark-ar.png",
    "app-store-badge-ar.svg",
    "iphone-18-pro-max-black-portrait.png", "iphone-18-pro-max-black-landscape.png",
)})
FILES.update({"/media/" + name: MEDIA / name for name in (
    "icon.jpg", "page-mode.png", "focus-mode.png", "khatma-tracking.png", "bookmarks.png",
)})


class Preview(BaseHTTPRequestHandler):
    def do_GET(self):
        path = FILES.get(urlsplit(self.path).path)
        if path is None or path.is_symlink() or not path.is_file():
            self.send_error(404)
            return
        size = path.stat().st_size
        start, end = 0, size - 1
        requested_range = self.headers.get("Range")
        if requested_range:
            try:
                unit, bounds = requested_range.split("=", 1)
                first, last = bounds.split("-", 1)
                if unit != "bytes" or "," in bounds:
                    raise ValueError
                start = int(first) if first else max(0, size - int(last))
                end = int(last) if first and last else size - 1
                if start < 0 or end < start or start >= size:
                    raise ValueError
                end = min(end, size - 1)
            except ValueError:
                self.send_error(416, "Invalid byte range")
                return
        self.send_response(206 if requested_range else 200)
        self.send_header("Content-Type", mimetypes.guess_type(path)[0] or "application/octet-stream")
        self.send_header("Content-Length", str(end - start + 1))
        self.send_header("Accept-Ranges", "bytes")
        if requested_range:
            self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Robots-Tag", "noindex, nofollow")
        self.end_headers()
        try:
            with path.open("rb") as source:
                source.seek(start)
                remaining = end - start + 1
                while remaining:
                    chunk = source.read(min(1024 * 1024, remaining))
                    if not chunk:
                        break
                    self.wfile.write(chunk)
                    remaining -= len(chunk)
        except BrokenPipeError:
            pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Preview only the Khatmah design files")
    parser.add_argument("--port", type=int, default=4174)
    port = parser.parse_args().port
    print(f"Khatmah design review: http://127.0.0.1:{port}", flush=True)
    with ThreadingHTTPServer(("127.0.0.1", port), Preview) as server:
        server.serve_forever()

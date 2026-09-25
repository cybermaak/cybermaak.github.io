# MAAK website

Public static source for [cybermaak.dev](https://cybermaak.dev), including the
homepage and the Polytray, Maakdown, and Khatmah promotional pages.

**Publishing:** GitHub Actions validates `public/` and publishes a clean `dist/`
artifact to GitHub Pages. See [publishing and cutover](docs/publishing.md) for
the deployment controls, domain scope, and verification procedure.

## Local use

Requires Python 3.10 or newer; no package installation or app checkout is needed.

```sh
python3 scripts/site.py check
python3 scripts/site.py build
python3 scripts/site.py serve
```

Open `http://127.0.0.1:4173`. The server builds and serves only `dist/`.
After editing `public/`, restart it to rebuild, or run the build command in
another terminal and refresh. Use `serve --port 4174` if the default port is busy.

For changes to the build/check tool, run
`python3 -m unittest discover -s scripts -p 'test_*.py'`. These regression checks
cover broken links and the boundary between repository files and the artifact.

## Layout

```text
AGENTS.md                  Agent instructions and all product SOP pointers
public/                    Reviewed publishable content
  index.html               Homepage
  assets/                  Homepage media
  polytray/                Polytray landing page and public assets
  maakdown/                Maakdown landing page and public assets
  khatmah/                 Bilingual Khatmah marketing page and public assets
  404.html                 Missing-page content
  CNAME                    cybermaak.dev
scripts/site.py            Local checks, clean artifact build, preview server
docs/                      Website architecture, provenance, and cutover guide
.github/workflows/pages.yml Validation and publication from dist/ only
dist/                      Generated output; ignored by Git
```

The app repositories retain product SOPs and capture tools. The website retains
the selected public output; deployment never fetches the private Khatmah repo.
See [AGENTS.md](AGENTS.md) for instruction pointers and
[architecture](docs/architecture.md) for ownership.

Use the [design language](docs/design-language.md) for visual updates. Khatmah's
approved Quiet editorial design is integrated at `/khatmah/`; its
[design history and asset handoff](docs/design/khatmah/README.md) remain outside
the public build. Khatmah 1.1.0 was verified publicly available on 2026-09-24.
The owner approved the final website, including the sharing previews, on
2026-09-24 and authorized publication.

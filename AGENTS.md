# MAAK website agent guide

This public repository owns the homepage and all promotional landing pages.
Read this guide, `README.md`, and `docs/architecture.md` when starting work.
Read `docs/design-language.md` before visual or content-layout changes; it
defines the personal homepage identity and the shared product-page language.
Read `docs/publishing.md` before changing publishing or preparing a cutover.

## Working agreement

- Check `git status` in every repository you will edit. Preserve existing work.
- Keep changes uncommitted unless the user asks for a commit. Do not push,
  publish, change DNS, or change repository settings without authorization.
- Edit website content in `public/`. `dist/` is generated. Never publish the
  checkout root or introduce symlinks to app repositories in the public tree.
- Keep the site static and dependency-free unless a concrete requirement
  justifies a build framework. Preserve working URLs and app download links.
- Reuse actual reviewed app media. Never fabricate product UI or imply that
  unreleased features are already available.

## Product instructions: resolve these before editing a landing page

The website is the primary local project folder. The three app repositories
are attached folders, not submodules or website build dependencies. They are
usually siblings under `/Users/maak/repos`, but resolve their actual locations
from the current project; a website worktree may live elsewhere.

For the relevant product, explicitly read its root `AGENTS.md`, any applicable
nested instructions, and the SOP below. Secondary-folder instructions are not
automatically loaded. Read the app context required by those instructions.

| Website path | App repository | Canonical product SOP |
|---|---|---|
| `/maakdown/` | [cybermaak/maakdown](https://github.com/cybermaak/maakdown) | `docs/release-site-refresh.md` |
| `/polytray/` | [cybermaak/polytray](https://github.com/cybermaak/polytray) | `docs/marketing-site-refresh.md` |
| `/khatmah/` | [cybermaak/khatmah](https://github.com/cybermaak/khatmah) (private) | `docs/MARKETING_SITE_SOP.md` |

Product SOPs own release facts, screenshot generation/reuse, fixtures, and
product-specific checks. Keep those procedures in the app repositories rather
than copying them here. If a checkout is unavailable, existing website-only
layout work can proceed; do not invent release claims or new media instructions.

The Khatmah repository URL is a pointer, not an access credential. Do not copy
its private instructions, source, app databases, diagnostic evidence, or build
artifacts into this public repository. Its SOP identifies public-safe sources.

## Website preparation and verification

1. Follow the relevant product SOP and identify the intended public release.
2. Copy only selected public assets into that product's directory. Record the
   source release/commit and reuse or capture decision in `docs/content-sources.md`.
3. Update product copy, captions, links, canonical metadata, and social metadata
   together. Use root-relative links for internal navigation and absolute URLs
   for canonical metadata and external destinations.
4. Run `python3 scripts/site.py check` and `python3 scripts/site.py build`.
   When changing the build/check tool or workflow, also run
   `python3 -m unittest discover -s scripts -p 'test_*.py'` to verify that
   repository metadata, links, and out-of-tree files cannot enter the artifact.
5. Preview with `python3 scripts/site.py serve`. Check the homepage-to-product
   flow, return navigation, images, and desktop/narrow layouts. Verify changed
   external downloads and information links when network access is available.
6. Run `git diff --check` in each edited repository. Review the final file list
   for accidental private content. Apply the user's commit/publication scope.

The website build must work without access to any app repository. Cross-repo
access is for preparing content; the public deployment consumes committed
website files only.

## Khatmah information site

The separate Cloudflare Worker continues to own:

- `https://khatmah.maaktech.dev/`
- `https://khatmah.maaktech.dev/privacy`
- `https://khatmah.maaktech.dev/support`
- `https://khatmah.maaktech.dev/credits`

Keep these information URLs independent of the promotional page. The owner's
current direction for `/khatmah/` is marketing with an App Store download and
return-home navigation; do not add information-site, privacy, support, credits,
or private-repository links there. Do not move the information pages, change
App Store metadata, or run an App Store publishing lane as part of a refresh.

Khatmah's approved Quiet editorial design is implemented in `public/khatmah/`
with English/Arabic copy, still screenshots, and official Apple device frames.
The three original proposals and accepted reference remain in
`docs/design/khatmah/`, outside the public build. Follow the private product
SOP for release verification and media preparation, and `docs/publishing.md`
for the publication checks. Apple's public listing verified
Khatmah 1.1.0 on 2026-09-24; the featured release is available. Verify release
facts again when preparing future product updates.

## Project context

Keep GPT project context minimal: the project name/purpose and attached folder
locations are enough. All instruction pointers belong in this file. Do not
create a parallel SOP index in project context or in `/Users/maak/repos`.

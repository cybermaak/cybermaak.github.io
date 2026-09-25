# Website ownership

The public `cybermaak.github.io` repository is the editable source for the
homepage and all promotional pages. The canonical domain remains
`cybermaak.dev`. A static `public/` tree is validated and copied into a clean
`dist/` artifact for GitHub Pages.

| Responsibility | Owner |
|---|---|
| Homepage, landing-page HTML/CSS, selected public media, shared navigation | Website repo |
| Product facts, capture tooling, fixtures, screenshot reuse decisions | Each app repo |
| Agent instruction and product SOP pointers | Website `AGENTS.md` |
| Khatmah application code and private maintenance instructions | Private Khatmah repo |
| Khatmah policy/support/credits source and Worker | Private Khatmah repo; separate information deployment |
| Published desktop installers and releases | Existing public app repositories |

Public routes are `/`, `/polytray/`, `/maakdown/`, and `/khatmah/`. Existing
Polytray/Maakdown media filenames and download destinations are preserved.
Khatmah uses the approved Quiet editorial marketing design, with English and
Arabic in one static page, a small local language-switch script, and selected
media stored entirely in this website. Its media matches the reviewed 1.1
exports; Apple verified public version 1.1.0 on 2026-09-24. GitHub Actions
publishes the central website as described in `publishing.md`.

## Content preparation

An agent starts in the website repository, reads its `AGENTS.md`, and explicitly
loads the relevant instructions in the attached app repository. It generates
or selects release-appropriate media there, then copies reviewed public files
into the website. App and website changes remain separate Git changes.

Do not make the website's build depend on a sibling checkout, symlink, submodule,
private repository token, Simulator, or desktop app build. The checked-in media
are deliberate publishing copies. Product procedures remain app-owned.

The public repository is public even when its Markdown documents are excluded
from the deployed artifact. Keep confidential product notes in the private app
repository. The artifact boundary prevents accidentally serving repository
metadata; it does not make GitHub source files private.

## Domains and transition

GitHub Pages for the website repository owns all four public routes. The app
repositories retain their old `site/` files for reference and rollback, but their
Pages sites are disabled and their `pages.yml` workflows are disabled manually.
App release workflows are unchanged.

`maaktech.dev` currently has an independent Cloudflare homepage deployment.
The eventual choice is a full-site proxy to GitHub Pages or a path-preserving
redirect. This structure does not select or apply that choice.

`khatmah.maaktech.dev` remains the existing Workers Static Assets information
site. Its privacy, support, credits, and legacy `.html` links retain their
current roles. The promotional page is separate marketing with a verified
App Store download; it does not link to the information site or copy its
policies. App Store metadata remains unchanged.

## Local GPT project

Make this checkout primary and attach the three app checkouts. A sufficient
project description is: “Maintain the MAAK website and its app landing pages.”
Keep instruction/SOP pointers in root `AGENTS.md`; do not duplicate them in
project context. Folder selection supplies the locations.

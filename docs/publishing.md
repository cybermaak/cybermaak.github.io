# Publishing and migration

## Publishing controls

The owner approved the final website and authorized committing and publishing
on 2026-09-24. GitHub Pages is configured for **GitHub Actions**, with the existing
`cybermaak.dev` custom domain. The workflow validates pull requests and pushes;
publication runs on `main` when `PAGES_DEPLOY_ENABLED=true` (enabled at cutover).
Only `dist/` is uploaded. The app repositories are not build dependencies.

The Maakdown and Polytray Pages sites were already disabled when checked on
2026-09-24. Their separate `pages.yml` workflows have also been disabled manually.
App release workflows and repository source files are unchanged.

The old `maaktech.dev` Cloudflare build connection remains enabled. The connector
rejected the attempted update with an authentication error. After being informed
that this connection deploys the repository root, the owner explicitly directed
on 2026-09-24 to leave Cloudflare unchanged and proceed, and will handle it later.
No Cloudflare settings, Worker code, or domains were changed during this cutover.
The root-directory publisher is an outstanding follow-up: it can publish this
public repository's instructions and metadata, and it does not use the Pages
`dist/` artifact. A future proxy or redirect remains a separate decision.

## Initial deployment verified

Website commit `284c5726396833d039fcbf5e792f3e64666a89b3` was published by
[the successful Website workflow](https://github.com/cybermaak/cybermaak.github.io/actions/runs/36091069842)
on 2026-09-24 Pacific time (2026-09-25 UTC). Both build and deploy jobs passed.

All 51 live HTTP/content checks passed: the four routes and all 42 deployable
content files matched the approved build byte for byte, the three product paths
without trailing slashes resolved correctly, and six unknown or excluded
repository paths returned 404. The normal HTTP client and browser succeeded;
an initial Python HTTP client was blocked with 403 and was not used as evidence
of site failure. Live English/Arabic switching, right-to-left layout, hero media,
App Store destinations, and return-home navigation passed browser checks.

Khatmah's seven information URLs (root, privacy, support, credits, and three
`.html` aliases) all returned 200 after redirects. No app repository was committed
or pushed. Cloudflare remains the owner-deferred follow-up described above.

For future rollback, revert the affected website content while retaining the
`public/` build boundary and Actions workflow, then publish and verify all four
routes. Do not blindly revert the initial migration: the legacy commit uses a
repository-root layout and no longer matches the Actions publishing setup.
Restoring separate project sites would require a coordinated hosting rollback.

## Before the first publication

1. Review the local website and product SOP changes. Resolve product page/media
   sources from `docs/content-sources.md`. Keep Khatmah policy pages separate.
2. Record the existing GitHub Pages settings, app Pages settings, workflow
   states, and Cloudflare versions for rollback. The September 2026 audit is
   the baseline; recheck relevant settings at cutover time.
3. Normally disable the old `maaktech.dev` repository-root Cloudflare build
   before pushing this tree. The owner deferred this step for the initial
   cutover (see above). Resolve it before treating Cloudflare as a supported
   publisher. The old Worker is not a clean security rollback.
4. Prepare the authorized GitHub transition from branch publishing to GitHub
   Actions for this repository. Keep the existing `cybermaak.dev` custom domain
   and HTTPS configuration. Publish only the workflow's `dist/` artifact.
5. Coordinate the final central-site deployment with retiring the Polytray and
   Maakdown project Pages sites and disabling their old `pages.yml` workflows.
   Check the product paths immediately after the transition. Do not leave two
   independent publishers responsible for the same path.
6. After authorization for this cutover, enable `PAGES_DEPLOY_ENABLED`, commit
   and push the reviewed changes, or dispatch the workflow on the reviewed
   `main` commit. GitHub Pages must already be configured for Actions.
7. Verify the public URL matrix below. Record the deployed website commit and
   any product SOP commits. Keep a rollback plan for the coordinated hosting
   transition; do not delete old app site files until the central site works.

The gate is one-time migration control, not an extra approval for each routine
authorized website publication. After cutover, pushes to `main` publish the
central site automatically. The workflow never builds or publishes the apps.

## Khatmah publication approval

The owner-approved bilingual Quiet editorial page is integrated at
`public/khatmah/`. Apple’s public US lookup verified **1.1.0** on 2026-09-24,
with a release timestamp of `2026-09-24T19:36:59Z`. Its listing confirms dark
theme, landscape Focus, and ayah image sharing. The release-availability
check is complete; all selected media remains unchanged from the approved
handoff. The owner completed final website review and approved committing and
publishing on 2026-09-24, including the sharing-image preview crops. Their exact
source and dimensions are recorded in `docs/design/khatmah/README.md`.

- Follow the private product SOP through the root `AGENTS.md` pointer for
  subsequent changes to product copy or screenshots.
- Preserve the existing App Store support/privacy destinations and separate
  information Worker. The marketing page links only to the App Store, the
  homepage, and its own full-size media.

The owner waived the Safari/WebKit mobile check for this iteration on
2026-09-23. Record that check as skipped, not passed; the normal requirement
returns for future refreshes. The current authorization covers this website repository; app repository
changes are not included in the website commit.

## Publication checks

- `/`, `/polytray/`, `/maakdown/`, `/khatmah/`: correct title/content and 200.
- Product paths without a trailing slash: normalize to working pages.
- Homepage/product/back links and every referenced image/style: work locally
  and after deployment. Check desktop and narrow widths.
- Unknown paths: actual 404; do not mask missing pages with the homepage.
- Canonical and social URLs: `https://cybermaak.dev/...`.
- Khatmah root, privacy, support, credits, and `.html` aliases: remain working
  on `khatmah.maaktech.dev`.
- `/.git/HEAD`, `/AGENTS.md`, `/docs/architecture.md`, `/scripts/site.py`, and
  `/wrangler.jsonc`: not served from the public artifact.
- `maaktech.dev`, HTTP, and `www`: match the separately approved domain plan.

## Routine changes after cutover

Follow root `AGENTS.md` and the relevant product SOP. Validate, build, preview,
and review the diff. When a push is authorized, the Pages workflow uploads only
`dist/` and deploys from `main`. Inspect the live page and record its source
release/commit. Public content changes require no private-repository credential.

References: [GitHub custom Pages workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
and [publishing-source settings](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

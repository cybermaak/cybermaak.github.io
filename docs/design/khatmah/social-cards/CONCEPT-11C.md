# Concept 11C — Arabic icon-led identity

Revision of concept 11B, prepared 2026-09-25 at the owner's request.
Remove the separate Arabic title and enlarge the genuine icon from 176px to
320px, centered at x885 with top y106. The icon artwork contains the app name.
Keep the Arabic badge, phone, background, and all English drawing unchanged.
English output is byte-identical to 11B. Selected by the owner for publication. Earlier candidates remain local review files.

## Deterministic regeneration prompt

```text
Regenerate Khatmah concept 11C using render-11c.swift and the unchanged inputs
in manifest-11c.json. Execute the native renderer, not an image model. Preserve
concept 11B's phone, gradient, colors, badge, and complete English design.
For Arabic only, remove the separately typeset “ختمة” title. Render icon.jpg
at (725,106),320×320,22% rounded corners, preserving its lettering and artwork.
Keep the localized App Store badge centered at x885,y474,width220 with its
original proportions. Add no separate Arabic title, tagline, or version.
Export 11c-en.png and 11c-ar.png at1200×630, plus 11c-pair.png for comparison.
Render twice and compare hashes; confirm English matches 11b-en.png exactly.
For future versions, replace only approved public assets through the product
SOP and record a new manifest. Do not commit, change metadata, or publish.
```

```sh
CLANG_MODULE_CACHE_PATH=/private/tmp/khatmah-card-modules \
  swift docs/design/khatmah/social-cards/render-11c.swift
```

Append an output directory to preserve these candidates. Arabic was visually
inspected, dimensions checked, and all three outputs reproduced byte for byte.
Exact reproduction requires the recorded assets, fonts, and macOS environment.

## Published use

The approved outputs are copied unchanged to
`public/khatmah/assets/social-card-ar-v1.png` and `social-card-en-v1.png`.
Run the renderer here, compare its output hashes to `manifest-11c.json`, then
copy the two locale PNGs to those public filenames. Do not publish the pair
board. For a changed composition use new versioned public filenames.

The static page embeds Arabic Open Graph and Twitter large-image metadata.
The browser language switch updates the image, title, description, alternative
text, and locale. GitHub Pages returns the same HTML for `?lang=en`; crawlers
that skip JavaScript still see Arabic. A guaranteed English social preview
requires a separate static URL or server-side response, outside this change.

Only this prompt, renderer, and manifest are committed from the concept folder.
The manifest's review PNGs can be regenerated; the approved locale bytes are
also available under the public filenames above. Exact reproduction requires
the recorded rendering environment. No private app repository is needed.

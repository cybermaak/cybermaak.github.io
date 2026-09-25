# Khatmah landing-page design and handoff

Prepared 2026-09-23; responsive previews and a refined direction added the same day.
**The owner approved Quiet editorial on 2026-09-23 and the final integrated
website, including the sharing previews, on 2026-09-24.** The page is in
`public/khatmah/`; committing and publication are authorized. Public **1.1.0
availability was verified on 2026-09-24** through Apple's US lookup; its release
timestamp is `2026-09-24T19:36:59Z`. The owner waived Safari/WebKit testing for
this iteration; it is recorded as skipped, not passed.

The accepted reference is `04-quiet-editorial-refined.html` with its CSS and
JavaScript. The normal website preview at `http://127.0.0.1:4173/khatmah/`
shows the integrated page. The proposal files below remain the design history.
The public page has the requested marketing-only links and no design-review
banner. On 2026-09-24 the obsolete pending-release banner was also removed
from the accepted reference, including its English/Arabic strings and styling.
Release readiness is tracked in documentation, not visitor copy.

## Compare the proposals

From the website root, run:

```sh
python3 docs/design/khatmah/preview.py
```

Open `http://127.0.0.1:4174/` for the comparison board, then open
`http://127.0.0.1:4174/04-quiet-editorial-refined.html` for the current
accepted reference. This loopback-only review server exposes an exact allowlist of the
design pages and selected assets.
It does not serve the repository root or private app checkout. The normal
`scripts/site.py` website preview remains separate on port 4173.

| Proposal | Direction | Relationship to the existing pages |
|---|---|---|
| **1. Warm paper** | Centered introduction, warm paper and gold, reading-to-tracking story | Closest to Maakdown; clear and familiar, though less distinctive |
| **2. Ink and gold** | Dark canvas, split hero, gold action, landscape Focus as wide proof | Strongest visual drama; dark screenshot needs careful contrast review |
| **3. Quiet editorial** | Off-white, forest green, large serif headlines, open sections | Recommended: the clearest reading identity while retaining the shared download flow |

Each direction now has a separate HTML/CSS responsive preview using genuine
reviewed 1.1 screenshots. Open [Warm paper](01-warm-paper.html),
[Ink and gold](02-ink-and-gold.html), or
[Quiet editorial](03-quiet-editorial.html) through the local review server.
The previews originally showed the 1.1 story while Apple review was pending.
Version 1.1.0 is now publicly verified. The earlier interactive concepts are
labeled historical proposals; their obsolete pending-release wording has been
removed. Saved September 23 screenshots retain the notices visible at capture
time and serve only as historical evidence.

First-screen captures at desktop and 390px mobile widths are saved as
`*-desktop-hero.png` and `*-mobile-hero.png`. The three older `*-review.png`
files remain the complete desktop concept references and show the verified
1.0.1 story. The responsive HTML pages are the current layout proposals and
show the 1.1 media. The two generations should not be presented as the same
render. App version 1.1.0 is released; the final website is approved for publication.

Standalone review images include the real screenshots and correct backgrounds:

- [Warm paper](01-warm-paper-review.png)
- [Ink and gold](02-ink-and-gold-review.png)
- [Quiet editorial](03-quiet-editorial-review.png)

All three contain a hero, released-product benefits, real reading/tracking
screens, a closing App Store action, and a quiet All apps return link. They
have no information-site, support, privacy, credits, or private-repository
links. The working download link is available in the review board; buttons
inside the generated mock images are visual proposals, not live controls.

## Design assets and fidelity

### Refined Quiet editorial proposal

The [current HTML proposal](04-quiet-editorial-refined.html) and
[its stylesheet](04-quiet-editorial-refined.css) preserve the editorial
composition while drawing color from the actual app: light reader parchment,
ink, and gold. The hero gives reading and khatma tracking equal visual weight;
later sections cover Focus Scroll, saved places, dark and landscape reading,
and sharing. The hero uses a normal text download link to the verified listing. The closing
action uses the sole official, unchanged, localized App Store badge.

The owner approved this final visual direction on 2026-09-23. The
same document now switches between original English and Arabic marketing copy
with a labeled button. The switch changes `lang`, `dir`, page metadata, visible
text, accessible names, genuine localized still screenshots, and Apple's
official localized badge. It remembers a selection locally when storage is
available and keeps the current section in view. No translation service or
tracking is used. Arabic labels follow the app's own “صفحة المصحف” and
“تركيز السطر”. The product name is ختمة; App Store and iPhone remain in English.

| English intent | Arabic copy |
|---|---|
| Reading and khatma tracking in a way that suits you | اقرأ القرآن وتابع ختماتك بالطريقة التي تناسبك. |
| Continue your khatma | واصل ختمتك. |
| Page and Focus reading | اختر «صفحة المصحف» بتخطيطها المألوف، أو اقرأ سطرًا بسطر مع «تركيز السطر». |
| Share verses as an image | شارك آيات القرآن في صورة. |

The source design media remains in `staged-media/`, outside the public build;
21 selected files are now also in `public/khatmah/assets/`, with exact copy
checksums in [asset-handoff.json](asset-handoff.json). Screens
come from the reviewed 1.1 English/Arabic fastlane exports. Focus Scroll uses
`05_FocusMode.png` in each locale. The sharing images are exact 1224 × 930
pixel crops at x=48, y=855 of the app-rendered previews visible within each
locale's `04_QuranSharing.png`. A separate standalone reviewed share export
was not available, so this crop should be confirmed with the owner before
final publication. No Quran text or app UI was generated or redrawn. The
badges came from Apple's official assets, including the Arabic `ar-ar`
marketing-tools badge.

The dark Landscape Focus still for each language is the complete frame at
12 seconds from its owner-approved 1.1 landscape App Preview (1920 × 886).
Source SHA-256: English `ff0d7e0bf0f055c8528cbd2c455af45c2773b9c118f781d98385a137cb096737`;
Arabic `bb26d18e609d2997d569c25c71822663d6516cf28644a9175a06c19f85071004`.
The existing light landscape capture remains next to it, with a full-size
link on each still. The source videos remain in the private app repository;
the active proposal serves no video. Nothing was uploaded or changed in App
Store Connect for this page.

Every full app screenshot is composed behind Apple's **unchanged official
iPhone 18 Pro Max Black bezel**. The portrait PNG is 1470 × 3000 with a
1320 × 2868 screen opening at x=75, y=66. The landscape PNG is 3000 × 1470
with a 2868 × 1320 opening at x=66, y=75. CSS places the authentic screenshot
at those exact insets and layers the unchanged transparent bezel above it.
The dark landscape video frame is contained within that opening with a very
small black margin because its 1920 × 886 source ratio differs slightly from
the device opening. No screenshot or bezel is stretched or cropped. The
rendered sharing image is an exported image preview, so it is shown without a
device bezel.

Apple source: [Design Resources](https://developer.apple.com/design/resources/),
`Bezel-iPhone-18.dmg` from
`https://devimages-cdn.apple.com/design/resources/download/Bezel-iPhone-18.dmg`.
The owner reviewed and accepted the embedded Apple Design Resources License
before these files were copied from the mounted volume. Both staged bezel
files are byte-identical to the source PNGs. SHA-256: portrait
`13fc8a8f0bc612f50c00d073b12aefa87bce1e4618fbdd3aa882438ae171e2be`;
landscape
`f69c104b8c1852d5b4ef58c0ecf6c5d5699e73d4a526b3f4efb808287350d8d2`.
The composition follows [Apple's App Store marketing guidelines](https://developer.apple.com/app-store/marketing/guidelines/):
no added shadow, tilt, reflection, recolor, or alteration to the bezel.

The official badge appears once per language view in the closing section,
above the minimum 40px screen height with at least one-quarter its height
clear around it. The hero has a regular App Store text link. The footer
credits Apple and its marks. The current localized, still-only captures are
saved as `06-{en,ar}-{320,390,430,desktop}-*.jpg` where applicable. The older
`05-*` captures document the superseded video and raw-screen iteration, and
`04-refined-*` documents the earlier English-only iteration.

The current page was visually checked in the in-app Chromium browser at
configured 320px, 390px, 430px, and 1200px widths in both languages. Its
desktop-style scrollbar reduces the visible content width by 15px; the saved
JPEGs reflect that. There was no horizontal overflow or missing image at
those sizes, and the active page contains eight official-bezel compositions,
one localized badge, and no video. These viewport checks are not an iPhone
Safari or WebKit device-emulation result. An attempt to launch Safari stalled
and was interrupted. The owner subsequently approved the design and explicitly
waived that remaining check for this iteration. Future refreshes retain the
normal mobile Safari/WebKit check in the product SOP.

### Original concept assets

The three numbered PNGs were generated with the built-in Image Gen tool using
the briefs in [prompts.md](prompts.md). They contain layout and page copy, with
deliberately empty app-media windows. Their alpha backgrounds require the
specified canvas colors in `index.html`; do not judge them on a black image
viewer background or copy them into the public website.

The board layers unchanged, real Page Mode and khatma-tracking PNGs and the
published app icon from `baseline-media/` over the generated layouts.
This keeps Quran text and application UI authentic. No simulator, new app
capture, source rebuild, or App Store publication was involved.

Concept canvases are 1024 × 1536. Actual media uses `object-fit: contain`, so
the full 1320 × 2868 capture is preserved even where a generated window has a
slightly different aspect ratio. The final page should use intrinsic image
dimensions and natural content flow; do not reproduce the board's absolute
positioning or small letterbox gaps as a production layout.

The shared 1.0.1 story and CTA text remain as accessible HTML at the bottom of
the original board. The new responsive previews provide resolved mobile
layouts; they are design artifacts, not the public page.

The original staged files under `staged-media/` are selected copies of the private
app's reviewed 1.1 `fastlane/screenshots/en-US/` exports: Page Mode, Dark Mode,
Landscape Focus, Quran Sharing, and Khatmah Tracking. The icon is the already
public App Store icon. No Quran text or application interface was generated.
The full design stage stays outside the website build; the approved subset is
copied into `public/khatmah/assets/`. The reviewed
1.1 preview videos also exist in the private app repository, but the proposals
use stills. The approved implementation also uses only stills; source videos
remain in the private app repository.

## Review evidence

The original generated reviews were inspected at their native 1024px canvas
width. The new HTML previews were inspected in the Codex in-app browser at
1024px desktop and 390px mobile widths. Every image loaded; each page has one
main heading and no horizontal overflow at either width. The first-screen
exports were visually inspected. The complete layout remains reviewable in
HTML. Full-page IAB exports were discarded because its capture stitched
duplicate content; the saved first-screen exports are clean.

The review covered headline/CTA copy, hierarchy and section order, palette and
canvas treatment, typography, whitespace, screenshot integrity and framing,
and footer navigation. The board intentionally adds the authentic app icon
and unchanged release screenshots to the generated concepts. Small media
letterbox gaps are a review-only consequence of fitting real screenshots to
generated windows; intrinsic proportions replace those windows in the final
page. This paragraph records the original proposal review; the later accepted
reference and implementation are described above and below.

Before integration, website checks and the clean build passed with 27 public files / five HTML
pages. Proposal images, prompts, this board, and documentation are excluded
from `dist/`. All four copied screenshots match their release-source bytes.

## Content basis

Apple's public listing was rechecked on 2026-09-24: Khatmah **1.1.0**, free for
iPhone, iOS 17 or later. The published description and release notes support
reading modes, khatma tracking, saved places, dark theme, landscape Focus,
ayah image sharing, offline use, no account, and no ads. The September 23
1.0.1 check remains the historical basis for the original generated concepts.

Public asset provenance and checksums are in
[content-sources.md](../../content-sources.md). Product preparation instructions
remain in the private Khatmah repository's `docs/MARKETING_SITE_SOP.md`; use
the pointer in the website [AGENTS.md](../../../AGENTS.md).

## Integration, 2026-09-23

The approved page replaced the starter with the same layout, copy, palette,
type, section order, localized screenshots, and official Apple compositions.
Integration changes are limited to production file/asset paths, canonical and
social metadata, removal of the internal review notice, and loading images
below the first viewport lazily. The language switch also updates social
metadata, tolerates a malformed URL fragment, and uses the website preference
key `khatmah-language`. With JavaScript unavailable, the English page remains
usable and the inactive language button is hidden.

The five original concept assets were preserved in `baseline-media/`; the
review server's `/media/` mapping now reads them there. The public build uses
only the selected 21 media files listed in the handoff manifest. No asset was
redrawn, resized, recompressed, or otherwise changed during integration.

Integration verification passed in the in-app Chromium browser for English
and Arabic at configured widths of 320, 390, 430, and 1200px (visible content
width is 15px narrower with this browser's scrollbar). Checks covered no
horizontal overflow, all localized images loading, the eight unchanged bezel
compositions, the single localized badge above 40px high, metadata, allowed
links, and absence of video. Browser screenshots were compared with the
accepted reference; the page body and CSS also match it after the documented
integration adjustments. Keyboard switching retains visible focus and the
current section; the language survives reload. Both directions, full-size
media navigation, and a malformed URL fragment were exercised. No console
errors or warnings were observed.

Website validation, a clean 44-file / five-page build, JavaScript syntax, and
diff whitespace checks passed. All 21 public assets match their staged and
built-copy checksums. The 20 other public files, including the homepage,
Maakdown, and Polytray, remain byte-identical to their pre-integration state.
All historical review-server paths resolve after the baseline archive move.
Temporary browser evidence is outside the repository. The integration preview
used port 4176 to avoid an old starter stylesheet cached on port 4173.
Safari/WebKit remains skipped under the owner's iteration-specific waiver;
storage-denial and JavaScript-disabled fallbacks were source-reviewed, not
separately exercised in this browser.

Follow the private product SOP, the shared [design language](../../design-language.md),
and the [remaining publication checks](../../publishing.md#khatmah-candidate-before-publication).
The independent support/privacy deployment and App Store metadata remain
unchanged. No commit, push, DNS edit, hosting cutover, or deployment was made
as part of this website integration.

## Release refresh, 2026-09-24

Ran the product SOP again after the owner reported release. Apple's public
lookup verified 1.1.0, clearing the former pending-release condition. Removed
the accepted reference's review banner, its localized strings, and unused
styling; earlier interactive proposals now identify themselves as historical
without saying the release is upcoming. The marketing page already omitted
the banner, so its approved layout, copy, and assets remain unchanged.

Rechecked the 21 asset hashes, including 12 exact matches to reviewed app
screenshot exports. Site validation and the 44-file / five-page build pass,
as do both JavaScript syntax checks and whitespace checks. Chromium checks
passed again in English and Arabic at 320/390/430/1200px: no banner, overflow,
missing image, or console warning/error; localized media, metadata, badge size,
keyboard language switching, preference persistence, and full-size link
targets are correct. The existing Safari/WebKit waiver remains limited to
this same approved design iteration. The owner subsequently approved the refreshed preview and authorized committing
and pushing on 2026-09-24.

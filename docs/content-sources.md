# Public content sources

Record the source release/commit and media reuse or capture decision whenever
updating a product page. The initial migration and Khatmah integration reuse
existing reviewed media; no app captures were regenerated for the integration.

| Destination | Source | Source checkout commit | Initial decision |
|---|---|---|---|
| `public/` homepage and `assets/` | Existing homepage repository | `089924edadb4934759c7c0f9f8aae955994be818` | Reused HTML/media; corrected favicon and local product navigation |
| `public/polytray/` | Polytray `site/` | `0cbe3c342c41b211b96ad41311c7c85502e2c24d` | Reused existing landing page and PNG assets; excluded the social-card authoring HTML and local Finder metadata |
| `public/maakdown/` | Maakdown `site/` | `6df0f90145dc6fadc302aecccc4399b51c3b439a` | Reused existing v0.2.0 presentation and all published media |
| `public/khatmah/` | Khatmah `docs/app-store-public-site/index.html` and `styles.css` | `69c7b858ff650c0d92e2e2514b095c3b45a48df4` | Reused only the already-public basic app description and styling; no private feature/release material or app media copied |

The commits identify source checkouts, not a claim that their latest app builds
are released. Tracked product site files were unchanged before import. The
initial Khatmah starter was replaced by the approved bilingual marketing page
on 2026-09-23. The 1.1 media handoff below is the current source record.
The central pages add return navigation;
the homepage and Maakdown page also include narrow-screen layout corrections.

Future entries should record the product release/tag, selected filenames,
where they were captured (or why existing media remains accurate), and the
website verification performed. Do not record private diagnostics or credentials.

## Khatmah original concept media, 2026-09-23

Verified against [Khatmah's public App Store listing](https://apps.apple.com/us/app/khatmah-%D8%AE%D8%AA%D9%85%D8%A9/id6773775419)
and Apple's public lookup for app `6773775419`: version 1.0.1, released
2026-08-06, minimum iOS 17.0. The listing supports the reading, tracking,
bookmarks, offline, no-account, and no-ads facts used in the proposals.

Four genuine English screenshots were exported unchanged from the recorded
public-release baseline through the app's private SOP. They were reused
because their UI and claims match that release, rather than using newer draft
captures. All are 1320 × 2868. Only selected public media crossed into this
repository; app instructions, build artifacts, and diagnostics did not.

These original 1.0.1 assets now live in `docs/design/khatmah/baseline-media/`
for the historical comparison board. They are excluded from the public build.

| Archived filename | Public-release source asset | SHA-256 |
|---|---|---|
| `page-mode.png` | `01_PageMode.png`, Khatmah 1.0.1 | `2a7014b0b85547ebe8364a092348001b2d79626b5b5e8bcc8460b1e705e9b1aa` |
| `khatma-tracking.png` | `02_KhatmahTracking.png`, Khatmah 1.0.1 | `6b43ace2876071a3ee6cf9d77d75d77f3ff52b5434ba7269466e59715390af3b` |
| `focus-mode.png` | `03_FocusMode.png`, Khatmah 1.0.1 | `a8b125fd09f006036600d2aa0bc82a130e35319c9f377f7ab988e724f98588ca` |
| `bookmarks.png` | `07_Bookmarks.png`, Khatmah 1.0.1 | `d331efc95cf72218c65c55864d516b419e734f5870a5d4fe026aaa37487cb760` |
| `icon.jpg` | Published 512px icon returned by Apple's lookup on 2026-09-23 | `8fc409b0b9d77094f199b13a0dccebf9d1c6114cb0aa7dd6fd3cfca074bb1f70` |

The three generated layout concepts, prompts, and review board live in
`docs/design/khatmah/`, outside the public build. Real PNGs are layered into
the board without redrawing app UI or Quran text. The generated concepts are
not product screenshots and must not become production page images.

## Khatmah approved implementation, 2026-09-23

The owner approved the refined Quiet editorial design in the separate
"Design Khatmah marketing landing page" task and requested its incorporation
into this website update. The HTML/CSS/JavaScript reference is
`docs/design/khatmah/04-quiet-editorial-refined.*`; the editable implementation
is `public/khatmah/{index.html,styles.css,script.js}`.

Exactly 21 selected files were copied byte-for-byte from the design task's
reviewed `staged-media/` into `public/khatmah/assets/`. The complete filename
and SHA-256 mapping is [asset-handoff.json](design/khatmah/asset-handoff.json).
The unused sharing-composer screenshot and private source videos were not
included in the public artifact.

| Public media | Reviewed source |
|---|---|
| `page{,-ar}.png`, `tracking{,-ar}.png`, `bookmarks{,-ar}.png`, `dark{,-ar}.png`, `landscape{,-ar}.png` | Corresponding English/Arabic 1.1 candidate App Store still exports selected in the design handoff |
| `focus-{en,ar}.png` | Each locale's reviewed 1.1 `05_FocusMode.png` |
| `landscape-dark-{en,ar}.png` | Complete frame at 12 seconds from each locale's approved 1.1 Landscape Focus App Preview; source checksums in the design README |
| `sharing-rendered-preview{,-ar}.png` | Exact 1224 × 930 crop at x=48, y=855 from each locale's `04_QuranSharing.png`; owner approved the crop on 2026-09-24 |
| `icon.jpg` | Same published 512px icon as the original concepts |
| `app-store-badge{,-ar}.svg` | Unchanged official Apple English and Arabic badges |
| `iphone-18-pro-max-black-{portrait,landscape}.png` | Unchanged official Apple design-resource PNGs; source and accepted license recorded in the design README |

On 2026-09-24, [Apple's public US lookup](https://itunes.apple.com/lookup?id=6773775419&country=us)
verified app `6773775419`, bundle `com.cybermaak.khatmah`, version **1.1.0**,
released at `2026-09-24T19:36:59Z`, free for iPhone with iOS 17.0 or later.
Its listing confirms the featured dark theme, landscape Focus, and ayah
image-sharing features, alongside reading, tracking, bookmarks, offline use,
no account, and no ads. The previously selected media is therefore reused;
no new capture or app build is needed. All 21 files match the approved handoff
checksums, and the 12 full screenshots also match the app's reviewed English
and Arabic exports at source checkout `69c7b858ff650c0d92e2e2514b095c3b45a48df4`
(the later `34299c0` commit changed only the private SOP).

The release-availability check is complete. Follow the remaining
[publishing checks](publishing.md#khatmah-publication-approval) before
deploying the website. Product capture procedures remain in the private app
SOP; none were copied into the website.

The page uses the verified App Store destination, homepage navigation, and
local full-size media links. Existing support/privacy URLs, App Store metadata,
and the information Worker remain unchanged.

## Khatmah presentation refinements, 2026-09-24

Reused all 21 approved public assets unchanged; no release claims, app captures,
or download destinations changed. Arabic is now the default HTML and runtime
fallback, with explicit `?lang=ar` / `?lang=en` overrides ahead of saved choice.
The single official badge moves to the hero, the closing CTA becomes a text
link, the existing published icon also appears beside the main title, and the
sticky header spans the full viewport with aligned inner content.

Build/link validation and Chromium EN/AR checks at 320/390/430/1200px passed
after fixing narrow English title overflow. First-visit Arabic, saved English,
explicit Arabic override, keyboard switching, URL query/fragment preservation,
and header edge coverage were checked. Safari automation stalled; its mobile
check is incomplete for this refinement and the earlier waiver is not extended.

## Khatmah social preview, 2026-09-25

The owner selected concept 11C: Arabic icon-led identity, an angled iPhone
reading close-up, and official localized App Store badge; English retains the
separate app name. The approved 1200 × 630 PNGs are published as
`khatmah/assets/social-card-{ar,en}-v1.png`. They reuse the existing reviewed
public 1.1.0 screenshots, icon, bezel, and badges without new capture or claims.
[Regeneration prompt](design/khatmah/social-cards/CONCEPT-11C.md), fixed renderer,
and input/output hashes are retained outside the public build. The Arabic
card is embedded in static HTML for crawlers; browser language changes also
update the social metadata. Query parameters do not localize static crawler
responses. Earlier unselected concepts remain local review artifacts.

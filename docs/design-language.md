# MAAK website design language

Extracted on 2026-09-23 from the rendered personal homepage, Maakdown, and
Polytray pages and their existing HTML/CSS. This is the shared reference for
future website work. It documents the current visual identity and makes the
rules for extending it explicit; it does not redesign the existing pages.

## Identity and scope

The personal site feels like a small, carefully arranged developer workspace:
dark, quiet, readable, and personal. Product pages explain a useful app through
plain language, a clear download action, and genuine product imagery.

Keep these two related expressions distinct:

| Surface | Visual role | Preserve |
|---|---|---|
| Personal homepage | A terminal window containing a person and their projects | Monospace typography, dark surfaces, mint accents, compact project navigation |
| Product landing pages | An introduction to an app and a route to download it | App identity, readable sans-serif copy, actual screenshots, restrained page structure |

This guide governs the shared website source intended for the main domains.
The owner confirmed the same site is also deployed at `maaktech.dev` and
chose to retain both copies for now. Product palettes may differ without
creating a different navigation or maintenance system.

## Personal homepage: observed tokens

These values describe `public/index.html`. Reuse them when extending the
homepage; do not introduce a second almost-identical palette or type system.

| Role | Value | Use |
|---|---|---|
| Canvas | `#070a10` | Page background beneath the existing circuit image |
| Window | `#0b0e14` | Main terminal surface |
| Chrome | `#0e131d` | Title bar and status foundation |
| Project surface | `#11151f` | Project links |
| Border | `#243042` | Main window and active edges |
| Subtle separator | `#1e2632` | Divisions and quiet borders |
| Primary text | `#cdd6e4` | Readable interface content |
| Heading | `#e4ebf5` | Name and strongest hierarchy |
| Supporting text | `#8a94a3` | Bio and secondary descriptions |
| Accent | `#46e6b0` | Prompts, arrows, hover emphasis, cursor |
| Existing utility grays | `#5b6677`, `#3d4756` | Observed decorative/chrome details; not defaults for meaningful text |

The status bar also uses olive `#a3c23f`, blue `#2f6d84`, ochre `#d4a13c`,
and green `#5f9e3f`. Keep those colors local to the terminal status treatment;
they are not four new general-purpose action colors.

| Element | Current treatment |
|---|---|
| Type | JetBrains Mono, weights 400/500/700, with a monospace fallback |
| Name | 23px, bold; may wrap at narrow widths |
| Bio | 15px, line height 1.7 |
| Utility text | Approximately 13–14px; subordinate to identity and project names |
| Window width | 660px maximum |
| Outer spacing | 40px vertically, 20px horizontally |
| Window body | 34px top / 40px sides / 26px bottom; narrow layout uses 26px / 22px |
| Corners | Window 14px, avatar 12px, project links 10px, social buttons 9px |
| Avatar | 84px square; use the existing photograph |
| Social buttons | 46px square, 11px gap, approximately 21px icons |
| Projects | Two columns with 12px gap; one column at 520px and below |
| Borders | Thin, usually 1px; depth comes mainly from surface separation |

The circuit background stays faint. It supports the terminal silhouette and
must not compete with text. Preserve the existing terminal header, prompt
motif, and powerline footer as one composition. New project links use the same
row shape, alignment, type, and mint arrow as existing links.

The shell is a visual identity, not a simulated command-line application.
Do not add command input, invented system telemetry, badges, or moving charts
to decorate ordinary navigation. Avoid extra nested windows.

## Product pages: the shared family

The review found stronger common structure than common color. Maakdown is
warm and light; Polytray is dark and technical. Both use a roughly 980px-wide
content column, simple system typography, generous separation between sections,
real app media, and direct download links.

| Element | Maakdown today | Polytray today | Extension rule |
|---|---|---|---|
| Palette | Paper `#faf9f4`, ink `#232320`, blue `#075cc7` | Canvas `#0a0a0f`, text `#e8ecf4`, accent `#8b9bff` | Choose colors that belong to the app; use one principal action accent |
| Supporting colors | Muted `#6b6a61`, border `#d8d8d2` | Muted `#aab4c6`, border `#2c3648` | Maintain readable contrast rather than copying a low-contrast value |
| Identity | 84px icon beside a 52px name | 96px icon above a 52px name | Genuine app icon and unmistakable product name |
| Intro | 24px tagline and 17px description | 21px tagline and 16px body | Short promise, then one specific explanation |
| Proof | Release and verified product facts | Verified signing, licensing, privacy facts | Include only useful, sourced facts; no decorative pill collection |
| Action | Download, then GitHub | Primary macOS download, other platforms secondary | One clear primary action; secondary actions only when useful |
| Media | Animated app demo, then six screenshots | One large app screenshot | Show actual product behavior at a readable size |
| Benefits | Compact feature grid | Compact feature grid and privacy section | Start from benefits; use open rows or columns when cards add no meaning |
| Footer | Home and public repository resources | Home and public repository resources | Always provide a quiet return to the personal homepage |

Khatmah belongs to this family through hierarchy, spacing, trustworthy media,
and the download flow. It does not inherit the desktop apps' GitHub, MIT,
notarization, or platform claims. Its app repository is private. Its public
marketing action is the App Store download.

## Khatmah: approved Quiet editorial expression

The owner-approved design was integrated on 2026-09-23. Use
`public/khatmah/styles.css` as the implementation reference and
`docs/design/khatmah/04-quiet-editorial-refined.html` as the accepted visual
reference. It extends the product family without changing the personal
homepage's terminal identity.

| Role | Approved treatment |
|---|---|
| Palette | White `#fffdf8`, parchment `#faf7eb`, ink `#241a0a`, body `#4d3d29`, muted `#6c5b46`, gold `#a1761f`, line `#e2d8c4`, panel `#f3ecdc` |
| English type | Georgia for editorial headings; system sans-serif for copy and controls |
| Arabic type | Geeza Pro / SF Arabic with appropriate line heights; native copy and RTL layout |
| Width | 1050px maximum, 24px desktop gutters; one column at 760px and below, at least 16px mobile gutters |
| Hero | App icon beside the large product name and reading/tracking promise; two authentic phone screens with equal importance |
| Story | Reading views → khatma and saved places → dark/landscape comfort → sharing → app essentials → download |
| Actions | One unchanged localized official badge in the hero; plain App Store text link at the bottom; quiet All apps navigation |
| Media | Still images, eight official device-frame compositions, unframed rendered sharing preview, full-size image links |

Use the genuine English and Arabic media selected by the app SOP. Change text
direction and alignment without mirroring images. The language switch updates
visible copy, accessible names, page metadata, screenshots, and badge; it keeps
the reader's section in view and remembers their choice when storage works.
Arabic is the default, including the complete no-JavaScript HTML. A valid
`?lang=ar` or `?lang=en` overrides a saved choice; otherwise use the saved
choice, then Arabic. Switching updates the URL while retaining other parameters
and its fragment. The sticky header background and border span the viewport;
its inner content stays aligned to the page gutters.

Keep Apple's official frames unchanged and align screenshots to their measured
screen openings with `object-fit: contain`. Do not add shadows, reflections,
tilt, or recoloring to the frames. Preserve the restrained gold rules, open
sections, and parchment bands; do not replace them with repeated cards. Media
provenance, frame geometry, and the remaining publication checks belong in
the design handoff and product SOP, not in the visitor-facing page.

## Layout and typography rules for new work

- Use a readable content width near 980px for product pages, with 24px desktop
  gutters and at least 16px on small screens. A deliberately approved design
  can vary the width; do not let every section choose a different alignment.
- Build a clear first viewport: product identity, short promise, supporting
  sentence, primary download action, then genuine product imagery. Keep useful
  facts below the main promise. Avoid new eyebrow labels above the headline.
- Use system sans-serif for product copy and controls. Typical desktop product
  headings are 40–56px, supporting copy 20–24px, body 16–17px with a comfortable
  line height. Scale headings down for mobile rather than squeezing words.
  An approved editorial concept may add one heading serif; record that choice.
- Use a small spacing scale: 4, 8, 12, 16, 24, 32, 48, 64, 96px. Prefer
  generous section space over large padding inside many boxed elements.
- Keep buttons legible, deliberately sized, and consistent. Existing product
  controls use restrained corners near 8px. Phone-screen corners may follow
  the device; they should not dictate the corners of every other component.
- Show product screenshots proportionally. Preserve their aspect ratios,
  readable text, and full relevant controls. Avoid color washes, stretched
  images, clipped Quran text, invented overlays, and perspective gimmicks.
- Use shadows sparingly around media, and borders only where they explain a
  boundary. New sections should vary between media, open text, and subtle
  background bands instead of repeating a wall of identical cards.
- Keep icons consistent within a page. The homepage's social marks retain
  their established silhouettes. New product decoration does not need an icon
  for every sentence; use icons only when they clarify meaning.

## Copy and content

Write as the app's maker: specific, useful, modest, and direct. Lead with what
someone can do. Explain technical detail only when it helps them choose the
app. Do not invent ratings, download totals, testimonials, compatibility,
privacy promises, or claims about an unreleased feature.

Use the relevant product SOP to establish release facts and media. The public
site contains the chosen copy and selected export files, not private release
procedures. Khatmah copy should support comfortable reading and continuity at
the reader's own pace; avoid competition, guilt, or streak pressure.

For Khatmah, use a verified App Store destination and a Home/All apps link.
Do not add information-site, support, privacy, credits, or private-repository
links to its promotional page. The separate information deployment remains
responsible for the existing App Store URLs.

## Responsive behavior, accessibility, and motion

These are requirements for future changes, not a claim that the current pages
have passed a complete accessibility audit.

- Keep reading order sensible without CSS. Use one main heading and sequential
  section headings, semantic links, meaningful image alternatives, and visible
  keyboard focus. A screenshot's alternative text explains its purpose; it
  should not reproduce all visible scripture or interface labels.
- Test at 320px, 390px, and a representative desktop width. Content and buttons
  must fit without horizontal page scrolling. Stack multiple media columns on
  mobile and keep screenshots useful, rather than shrinking a desktop collage.
- Allow browser zoom and text growth. Do not hide important content to preserve
  a visual composition. The homepage currently hides decorative git/clock
  segments at 520px and the path segment at 360px to keep its footer usable.
- Check text and controls for contrast on their actual backgrounds. Existing
  muted chrome colors are observations, not approval for new low-contrast text.
- Prefer still media unless motion explains a real workflow. Respect
  `prefers-reduced-motion`; give meaningful animation/video a still alternative
  and appropriate controls. No ambient parallax, autoplay audio, or attention
  effects. The current homepage cursor blink and Maakdown animated image are
  existing behaviors, not evidence that reduced-motion handling is complete.
- Preserve real Arabic/RTL content in screenshots. Any future Arabic page copy
  needs proper language/direction markup and review; do not imitate Arabic with
  decorative generated glyphs.

## Review checklist

Before accepting a visual update, compare the rendered result to this guide
and the selected concept. Check hierarchy, copy, palette, type, spacing,
media treatment, button states, and the narrow layout. Confirm the download
destination and the path back home. Test the public artifact boundary and
local links using the repository's existing commands.

For a new design, keep proposals outside `public/`, record the chosen direction,
then implement that direction. Review the actual browser output alongside the
accepted mockup. Update this guide only for an intentional shared-design
decision; put app-specific capture changes in the app's own SOP.

See [AGENTS.md](../AGENTS.md) for product SOP pointers,
[content sources](content-sources.md) for media provenance, and
[Khatmah proposals](design/khatmah/README.md) for the current design review.

# S1 Sarah — DR Prompt Log (Higgsfield + CapCut)

**Concept:** S1 — Trucking / I-17 commercial collision (non-DUI) — Direct-Response copy-led print stills
**Persona:** Sarah Mitchell, 38, ICU charge nurse, Flagstaff Medical Center
**Companion doc:** `../Copy_Treatments.md` (where Davis locks the variant copy before Higgsfield runs)
**Status:** SHELL — most variants `[AWAITING COPY LOCK]`. Once Davis writes `[LOCKED]` in `Copy_Treatments.md` Davis Selection Tracker, the matching prompt block here gets filled.
**Director:** Giuseppe Karma (AI Creative Director). McCabe wrote copy. Saul-cleared. Branding-last-pass per `feedback_branding_last_pass.md`.

---

## Aspect / format strategy

- **Native generation:** 4:5 portrait (1024×1280 ChatGPT Image 2 / Higgsfield) — Feed-optimal, also crops cleanly to 1:1 if Robert's deck wants it.
- **Reels motion-still extension (V1, V2, V5, V6 only):** generate the still in 4:5 first, then in CapCut layer the type, extend the canvas to 9:16 with the photographic background's environmental cue continued (steam, light shift, paper edge stir). Designed-static variants V3 (Hero Number) and V4 (Exhibit) do **NOT** get a Reels treatment — Bass distillation requires stillness; animated $1M numbers / bar charts read cheap.

---

## Designer / director anchors

Per `Designed_Overlay_System.md` + the Giuseppe Designed_Overlay_Reference library, each variant's anchor is documented in the per-variant block below. The set draws from:

- **Saul Bass** — distillation discipline on V3 (Hero Number $1M) + V4 (Exhibit Settlement Comparison). Single-idea-two-beats, type-as-image, ~25% deliberate negative space (HN-1.7B precedent — see Designed_Overlay_System).
- **Massimo Vignelli + Paul Rand** — Tiempos / Caslon serif typography hierarchy on copy-heavy print stills (V1, V2, V5, V6). Strict baseline grid. ~12% L/R margins.
- **Tufte data-ink minimum** — V4 chart discipline. No axis ticks, no gridlines, just the bars + range labels.
- **Alec Soth / Hiroshi Sugimoto** — photographic anchors for the dark-gradient photographic backgrounds (V1, V2, V5, V6). Clinical-respect register, warm-charcoal palette, late-afternoon Flagstaff kitchen light. **NEVER** Coens/Fargo or Sopranos register on Sarah — that lives in M1 Ty's photographic anchor set.

---

## Iteration targets (apply to every Higgsfield render)

1. **Side-specific continuity props (load-bearing — match S1 Primary's reference_lock):**
   - Sarah's **LEFT** arm in a black canvas Velcro brace (visible above the wrist). NEVER right.
   - Pale-blue FMC scrubs partially visible under a beige zip-up jacket / cardigan.
   - Banner-Phoenix medical bill stack on the kitchen table (recognizable letterhead — light blue header band).
   - Late-afternoon warm light camera-left through a kitchen window. Flagstaff 4 PM register, NOT Phoenix harsh sun.
   - Hair: shoulder-length brown, slightly grown out from the post-crash haircut documented in S1 reference lock.

2. **Type legibility on dark-gradient:** minimum **70% black-to-warm-charcoal gradient** over photographic background where serif copy lands (per Copy Treatments visual-treatment paragraphs). Falls off into full-color photo bleed in lower 30-40% of frame.

3. **No text in the rendered Higgsfield image** for variants that use CapCut text overlay (V1, V2, V5, V6). Higgsfield generates the photographic background ONLY; copy is layered in CapCut for editability per `feedback_ad_post_workflow.md`. **Exception:** V3 (Hero Number) and V4 (Exhibit) use ChatGPT Image 2's editorial text rendering for Tiempos serif at scale + Tufte chart discipline — generate text in-image but verify exact spelling against the locked Copy Treatment variant.

4. **No AI tells:** waxy skin, symmetrical face, HDR-glow, plastic eyes, melted hands, extra fingers. If a render has any of these, kill the seed and iterate.

5. **Branding-last-pass:** Fair Case torch logo (white, small, bottom-right), Torch Amber `#C8821A` typography on closing line, IBM Plex Mono 8pt footer disclaimer — **all added in CapCut**, never baked into Higgsfield. No `getafaircase.com` URL in-image.

6. **Reference image carry:** per `feedback_higgsfield_workflow.md`, start each generation with the `Renders/S1_Sarah_Trucking/Primary/` reference frame (or the locked S1 reference portrait file) loaded as the character anchor. Prompts describe ACTION + ENVIRONMENT, never re-describe Sarah's face / build / age.

---

## Per-variant prompt blocks

Variant IDs match `Copy_Treatments.md`. Status flips from `[AWAITING COPY LOCK]` → `[LOCKED, copy: …]` once Davis picks. Phase 2 ammo variants stay `[AWAITING COPY LOCK]` until post-Day-14 expansion.

### Block S1-DR-V1 — Commercial Insurance Asymmetry

**Status:** `[AWAITING COPY LOCK from Copy_Treatments.md §S1-DR-V1]`
**Designer anchor pick:** Vignelli grid + Soth photographic background
**Visual treatment:** Dark-gradient photographic. Top 60% scrim carries Tiempos headline + Caslon italic subhead. Lower 40% photo bleed of Sarah at kitchen table, LEFT arm brace visible, Banner-Phoenix bills foreground. Closing line (Torch Amber Caslon) + footer in CapCut.

**Prompt template** (fill once copy locks):
```
[REFERENCE IMAGE: Sarah reference_lock loaded as character anchor.]

Cinematic photographic still. The woman in the picture — Sarah, mid-30s nurse —
sits at her warm-wood kitchen table in late afternoon, three-quarter angle
camera-left, soft focus on her LEFT arm in a black canvas Velcro brace resting
near a stack of medical bills (Banner-Phoenix letterhead, light blue header
band, recognizable). Beige zip-up cardigan over pale-blue FMC scrubs partially
visible at the collar. Warm late-afternoon Flagstaff kitchen light from a
window camera-left, soft golden tonality, gentle backlight catching her hair.
Subtle environmental detail: a coffee mug, slightly OOF in foreground.

Composition leaves the upper 60% of the frame deliberately empty / quieter for
type to land — gradient-friendly negative space (a dim wall, a quiet stretch of
warm shadow, OOF kitchen depth). The bottom 40% is the photo focus.

4:5 portrait aspect. Mid-format film register: Mamiya 645 with 80mm lens
equivalent, ISO 400, soft natural light only. Alec Soth color palette —
warm-charcoal shadows, golden midtones, no HDR, no glamour skin. Clinical
respect, not pity; competent calm.

NO text in the image. NO logos. NO graphic overlays. The image is pure
photographic background — type will be added in CapCut.

Avoid: waxy skin, symmetrical face, plastic eyes, melted hands, harsh
direct flash, billboard energy.
```

**Iteration notes:** [empty until generation runs]
**Failure flags:** [empty]
**Winning seed:** [empty]

---

### Block S1-DR-V2 — The $35K Settlement Gap

**Status:** `[AWAITING COPY LOCK from Copy_Treatments.md §S1-DR-V2]`
**Designer anchor pick:** Bass anchoring + Soth photographic ground
**Visual treatment:** Top 70% Warm Charcoal solid field carrying two stacked hero numbers ($35,000 Cream / $33,700 Torch Amber) — type rendered in CapCut, NOT Higgsfield. Bottom 25% photo bleed of Sarah's LEFT arm + Banner-Phoenix bill stack on the kitchen table (tighter crop than V1).

**Higgsfield generates:** the bottom 25% photographic strip ONLY (will be composited under the Warm Charcoal type-field in CapCut). Generate the strip as a 4:5 still where Sarah's bill stack + braced LEFT hand fill the lower third, upper two-thirds is the OOF kitchen wall as soft warm-charcoal headroom.

**Prompt template:**
```
[REFERENCE IMAGE: Sarah reference_lock loaded.]

Tight crop on Sarah's LEFT hand (in black canvas Velcro brace) resting near a
stack of Banner-Phoenix medical bills on her warm-wood kitchen table. Bills
foreground, soft focus. Her hand visible but face cropped out / very soft OOF
upper-frame. Late-afternoon golden Flagstaff window light from camera-left.
The upper two-thirds of the frame is OOF warm-charcoal kitchen wall — a soft,
empty headroom that will receive type composited in CapCut.

4:5 aspect. Mid-format film, Soth color palette. NO text. NO logos.

Avoid: AI tells, harsh light, HDR.
```

**Iteration notes:** [empty]
**Failure flags:** [empty]
**Winning seed:** [empty]

---

### Block S1-DR-V3 — Hero Number, $1M Policy Floor

**Status:** `[AWAITING COPY LOCK from Copy_Treatments.md §S1-DR-V3]`
**Designer anchor pick:** Saul Bass single-idea-two-beats + Vignelli typography
**Visual treatment:** **No photograph.** Pure-color designed-static editorial in Roman Navy `#0D1F3C`. Bass distillation with $1,000,000 in Tiempos Headline 160-180pt Cream dominating, single 0.5pt Torch Amber structural rule, Caslon Pro small caps subhead.

**Generation tool:** **ChatGPT Image 2** (NOT Higgsfield) — for editorial Tiempos serif text rendering at scale per `feedback_ad_post_workflow.md`. Verify exact spelling against locked Copy Treatment.

**Prompt template:**
```
Editorial designed-static print ad. Pure Roman Navy field (#0D1F3C). Saul Bass
distillation discipline — single dominant typographic element with ~25% empty
upper-quadrant negative space.

Center frame: the figure "$1,000,000" in Tiempos Headline serif at 160-180pt,
Cream (#FFF7F0). Below the figure: a 0.5pt Torch Amber (#C8821A) horizontal
rule, ~40% width, centered. Below the rule: small-caps Caslon Pro at 22pt in
Torch Amber — "FEDERAL MINIMUM FOR AN INTERSTATE COMMERCIAL TRUCK" on three
lines, generously letter-spaced.

Below the small-caps subhead: a small body-text block in Caslon Pro 14pt at
50% Cream opacity (recedes — the number is the message).

Bottom-third: closing action line in Caslon Pro 18pt Torch Amber semi-bold.
Below that: IBM Plex Mono 8pt source attribution in Muted Navy Light.

Vignelli grid discipline — strict baseline, ~12% L/R margins, deliberate
upper-quadrant negative space. NO photograph, NO ornament, NO logo (Fair Case
torch added in CapCut last pass).

4:5 portrait. Editorial print-magazine register, not poster. Saul Bass + Massimo
Vignelli reference. The number carries the meaning; everything else is
structural support.

Render text exactly as specified in the locked Copy Treatment §S1-DR-V3.
Verify spelling letter-by-letter.
```

**Iteration notes:** [empty]
**Failure flags:** [empty — common Image-2 tells: number kerning irregularity, subhead small-caps not properly spaced, Torch Amber rule too thick]
**Winning seed:** [empty]

---

### Block S1-DR-V4 — Exhibit, Settlement Comparison

**Status:** `[AWAITING COPY LOCK from Copy_Treatments.md §S1-DR-V4]`
**Designer anchor pick:** Bass + Vignelli grid + Tufte data-ink minimum
**Visual treatment:** **No photograph.** Cream `#FFF7F0` field. Vignelli grid, Tiempos Headline upper-third, Torch Amber structural rule, two horizontal bars (Muted Navy Light short / Torch Amber long), small-caps chart label, closing line lower-third.

**Generation tool:** **ChatGPT Image 2** for editorial chart + serif typography precision.

**Prompt template:**
```
Editorial designed-static print ad. Pure Cream field (#FFF7F0) — not white.
Tufte data-ink minimum + Vignelli grid + Saul Bass distillation reference.

Top-left corner, Inter 9pt small caps in Roman Navy: "EXHIBIT A".

Upper-third center: headline in Tiempos Headline 32-36pt Roman Navy, two
lines, generous leading. Below the headline: a 0.5pt Torch Amber horizontal
rule, ~30% width, left-aligned with the type column.

Mid-frame: a horizontal bar chart with TWO bars only.
- Bar 1: short, in Muted Navy Light (#3D4A6B desaturated). Label above in
  Caslon Pro 14pt Roman Navy: "Without representation". Range label to the
  right of the bar in Caslon Pro 14pt Roman Navy.
- Bar 2: ~3-4× longer than Bar 1, in Torch Amber (#C8821A). Label above:
  "With Arizona trial counsel". Range label to the right.

Below the chart: a chart-label line in IBM Plex Mono 9pt small caps Muted
Navy Light, indented to the chart's left edge.

Lower-third: closing action line in Caslon Pro 18pt Torch Amber semi-bold.
Below that: IBM Plex Mono 8pt source attribution + disclaimer in Muted Navy
Light.

NO axis ticks. NO gridlines. NO percentage labels on bars. ~30% white space
across the composition.

4:5 portrait. NO photograph, NO ornament, NO logo (Fair Case torch added in
CapCut last pass).

Render text + numbers exactly as specified in the locked Copy Treatment
§S1-DR-V4. Verify spelling and dollar-figure formatting letter-by-letter.
```

**Iteration notes:** [empty]
**Failure flags:** Common Image-2 tells: bars not on baseline, range labels wrong typeface, dollar signs in wrong weight.
**Winning seed:** [empty]

---

### Block S1-DR-V5 — FMCSA, Different Rules (ultra-lean)

**Status:** `[AWAITING COPY LOCK from Copy_Treatments.md §S1-DR-V5]`
**Designer anchor pick:** Soth photographic ground + Vignelli typography (CapCut pass)
**Visual treatment:** Photographic-led, 70% black-to-warm-charcoal scrim upper third for headline. Middle 50% photo bleed of Sarah's LEFT hand on a stack of bound commercial-insurance policy paperwork; top page legibly shows "$1,000,000 LIABILITY LIMIT".

**Generation tool:** Higgsfield with reference_lock; OPTIONAL Image-2 pass to render the policy-paperwork text crisply.

**Prompt template:**
```
[REFERENCE IMAGE: Sarah reference_lock loaded.]

Cinematic photographic still. The woman in the picture — Sarah, mid-30s nurse —
sits at her warm-wood kitchen table in late afternoon. Camera angle three-
quarter from camera-right, mid-focal-length. Her LEFT hand (in black canvas
Velcro brace) rests on a stack of bound commercial-insurance policy paperwork.
The top page of the policy stack is legible in the frame — text visible at
thumb-scroll legibility: "$1,000,000 LIABILITY LIMIT". Other pages stacked
beneath.

The kitchen-table surface fills the lower-half. Beige zip-up cardigan over
pale-blue FMC scrubs visible. Late-afternoon Flagstaff window light camera-
left, soft warm tonality.

Upper-third of frame: OOF dim kitchen wall as warm-charcoal headroom that
will receive type composited in CapCut. The headline lands above her hands.

4:5 portrait. Soth color palette. Mid-format film register. NO additional
text overlays. The "$1,000,000 LIABILITY LIMIT" on the policy page is the
ONLY text in the image — render that text precisely; verify spelling.

Avoid: AI tells, glossy paper, fake insurance graphics, billboard energy.
```

**Iteration notes:** Optional pass — if Higgsfield can't render "$1,000,000 LIABILITY LIMIT" cleanly on the policy paper, generate the photographic background WITHOUT visible policy text in Higgsfield, then composite the policy-page text in CapCut as a paper-texture overlay.
**Failure flags:** Policy paper looking too clean / too generic insurance-mock.
**Winning seed:** [empty]

---

### Block S1-DR-V6 — Arizona Two-Year Window

**Status:** `[AWAITING COPY LOCK from Copy_Treatments.md §S1-DR-V6]`
**Designer anchor pick:** Soth photographic + Vignelli typography (CapCut pass)
**Visual treatment:** Dark-gradient photographic. Top 60% scrim carries headline + Caslon italic subhead. Bottom 35% photo bleeds — Sarah at kitchen table with a wall calendar visible behind her, pages slightly out of focus (temporal cue, not specific date).

**Prompt template:**
```
[REFERENCE IMAGE: Sarah reference_lock loaded.]

Cinematic photographic still. The woman in the picture — Sarah — at her
warm-wood kitchen table, three-quarter angle camera-left. On the kitchen
wall behind her, slightly out of focus, a paper wall calendar hangs (or a
quiet wall clock — temporal cue, never a specific date legible). Late-
afternoon Flagstaff window light camera-left.

Sarah's LEFT arm with black canvas Velcro brace rests on the table. Beige
cardigan, FMC scrubs at collar.

Composition: upper 60% of the frame is OOF warm-charcoal kitchen wall as
gradient-friendly headroom — the calendar is in this OOF zone, just present
enough to register but not legible. Lower 35% is the photo focus — Sarah +
table + brace.

4:5 portrait. Soth palette. Mid-format film register. NO text overlays.

Avoid: a calendar with a specific date legible (compliance — no manufactured
deadline), AI tells, harsh light, HDR.
```

**Iteration notes:** [empty]
**Failure flags:** Calendar reading as a specific date / month — must stay quietly OOF.
**Winning seed:** [empty]

---

## CapCut layout spec (per variant — fonts, sizes, colors, safe zones)

Type system and palette per `Designed_Overlay_System.md` and `feedback_fair_case_overlay_palette_rule.md`. SC parent overlay palette (Cream / Burgundy / Warm Charcoal) for headline + body; Roman Navy + Torch Amber discipline only at closing-line type + Fair Case torch corner mark.

| Element | Font | Size | Color | Notes |
|---|---|---|---|---|
| V1/V2/V5/V6 Headline | Tiempos Headline | 40-60pt | Cream `#FFF7F0` | Upper-third, on dark-gradient scrim |
| V1/V2/V5/V6 Subhead | Caslon Pro Italic | 18-22pt | Cream `#FFF7F0` | Below headline, lighter weight |
| V1-V6 Closing action line | Caslon Pro Semi-Bold | 18pt | Torch Amber `#C8821A` | Lower-third, just above Meta button position |
| V1-V6 Footer disclaimer | IBM Plex Mono | 8pt | Warm Grey (photo) / Muted Navy Light (designed-static) | Bottom strip |
| V3 Hero Number | Tiempos Headline | 160-180pt | Cream `#FFF7F0` | Center frame, dominates |
| V3/V4 Subhead small-caps | Caslon Pro Small Caps | 22pt | Torch Amber `#C8821A` | Below structural rule |
| V3/V4 Body context | Caslon Pro | 14pt | Cream 50% opacity / Roman Navy | Recedes |
| V4 Exhibit label | Inter Small Caps | 9pt | Roman Navy `#0D1F3C` | Top-left corner |
| V4 Chart bar labels | Caslon Pro | 14pt | Roman Navy / Torch Amber | Above each bar |
| V4 Chart range labels | Caslon Pro | 14pt | Roman Navy / Cream | Right of each bar |
| V4 Chart label | IBM Plex Mono Small Caps | 9pt | Muted Navy Light | Below chart |
| Fair Case torch | logo (white) | ~24px tall | white | Bottom-right corner, ~40px margin |

**Safe zones:** Meta Feed crops from a 1:1 master at 4:5 are conservative — keep critical type within central 90% of frame both axes. The closing action line should sit in the lower-third but at least 80px above the bottom edge to avoid Meta's "Sponsored" / Learn More button overlap on iOS Feed.

**Reels (9:16) extension** for V1, V2, V5, V6 only: in CapCut, extend canvas to 9:16, animate the photographic background with subtle environmental motion (1-2 second loops): coffee steam (V1), bills page edge stir (V2), policy paperwork edge settling (V5), calendar pages slight waver (V6). Type holds locked-position. Total runtime 6-10s, music bed neutral (Fair Case sonic palette per brand brief).

---

## Cross-references

- Copy authority: `../Copy_Treatments.md` (where Davis locks variant before any generation runs)
- Designed Overlay System: `Abracadabra/08_Brands/Second_Chair/02_Visual/Designed_Overlay_System.md`
- Designer anchor library: `Abracadabra/04_Production/Giuseppe_Karma_(AI_Creative_Director)/Designed_Overlay_Reference/Saul_Bass.md`, `Patrick_Clair.md`, `Vignelli.md` (or equivalent)
- Fair Case brand: `08_Brands/Second_Chair/20_Fair_Case/04_Visual_Identity_Brief/BRAND_SYSTEM_BRIEF.md`
- Branding-last-pass discipline: memory `feedback_branding_last_pass.md`
- Higgsfield iterative flow: memory `feedback_higgsfield_workflow.md`
- Post workflow: memory `feedback_ad_post_workflow.md`
- Sarah reference lock: `Renders/S1_Sarah_Trucking/Primary/` reference frame
- AZ MVA reference setting: `Audience/Deep_Personas/Sarah/01_Life_World.md` (Flagstaff kitchen, FMC scrubs, Banner-Phoenix bills)

---

*Giuseppe scaffolding. McCabe wrote copy. Davis picks variant. Saul gates compliance. Higgsfield generates per locked variant block. CapCut last-pass adds branding + animates Reels-eligible variants. — 2026-04-27*

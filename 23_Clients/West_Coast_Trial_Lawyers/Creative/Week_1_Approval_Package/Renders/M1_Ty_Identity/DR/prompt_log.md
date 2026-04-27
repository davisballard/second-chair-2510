# M1 Ty — DR Prompt Log (Higgsfield + CapCut)

**Concept:** M1 — Motorcycle / Rider Identity (covers M1/M2/M3 thematically — one DR set serves all three M concepts)
**Persona:** Ty Rivera, 28, commercial HVAC tech, Chandler AZ, 2020 Yamaha R6 totaled by left-turning Nissan Rogue at Ahwatukee intersection (non-DUI)
**Companion doc:** `../Copy_Treatments.md` (where Davis locks variant copy before Higgsfield runs)
**Status:** SHELL — most variants `[AWAITING COPY LOCK]`. Once Davis writes `[LOCKED]` in `Copy_Treatments.md`, the matching prompt block here gets filled.
**Director:** Giuseppe Karma. McCabe wrote copy. Saul-cleared. Branding-last-pass per `feedback_branding_last_pass.md`.

**Sister doc:** `../Primary/prompt_log.md` — the existing M1 cinematic primary work.

---

## Aspect / format strategy

- **Native generation:** 4:5 portrait — Feed-optimal.
- **Reels motion-still extension (V1, V2, V5, V6 only):** generate still in 4:5, then in CapCut layer type, extend canvas to 9:16 with environmental motion (distant intersection traffic, headlight glow shift, paper edge stir, calendar page waver). Designed-static V3 + V4 do **NOT** get Reels.

---

## Designer / director anchors

- **Joel Coen (Coens / Fargo register)** + **The Sopranos** — photographic anchors for V1, V2, V5, V6 dusk intersection compositions. Hard-light shadow + warm-key tradesman register. NEVER neighborly-soft (that's Laura's set).
- **Saul Bass** — V3 (Hero Number 47%) distillation discipline.
- **Massimo Vignelli + Tufte** — V4 chart discipline.
- **Alec Soth** — supplementary photographic anchor for the kitchen-table scenes (V2, V6) where Ty is at home with bills + helmet, NOT at the intersection.
- **NEVER** biker-stereotype anchors: no Hunter Thompson-on-a-Vincent, no chrome-and-leather glamour, no "freedom of the open road." Tradesman first, rider second. Plain.

---

## Iteration targets (apply to every Higgsfield render)

1. **Side-specific continuity props (load-bearing — match M1 Primary reference_lock):**
   - **Shoei helmet under his RIGHT arm** (NEVER left — left arm is unused for hand props in his pose; right arm is helmet-carrying side per Primary lock).
   - **Dainese leathers + visible Tech-Air airbag vest** — the airbag vest is critical (story prop: he almost didn't buy it; Rachel pushed him to). It should read clearly on screen as the slim outer vest over the leathers.
   - **Right-leg brace** partially visible under denim cuff just above the boot. NEVER left.
   - **Hair:** dark, short, slightly grown out post-crash.
   - **Beard:** short, kempt — tradesman not lumberjack.

2. **Settings:**
   - **Ahwatukee intersection** for V1, V5 (the intersection where the crash happened — three-quarter angle, looking at painted lines, distant traffic light just visible, headlights blooming OOF).
   - **Ty's kitchen** for V2, V6 (bills + helmet on counter; Soth photographic register here, NOT Coens — kitchen scenes are quieter, financial-pressure-coded).

3. **Light register:** **dusk only.** Coens-style hard-light shadow + amber key on intersection scenes. Late dusk warm window light on kitchen scenes. NEVER midday daylight, NEVER night-black.

4. **Type legibility on dark-gradient:** minimum 70% black-to-warm-charcoal gradient over photographic background.

5. **No text in Higgsfield image** for V1, V2, V5, V6. V3 + V4 use Image 2.

6. **No AI tells, no biker-stereotype glamour.**

7. **Branding-last-pass:** Fair Case torch (white, small, bottom-right), Torch Amber typography on closing line, IBM Plex Mono 8pt footer — all CapCut.

8. **Reference image carry:** start each generation with the locked Ty reference portrait file as character anchor.

---

## Per-variant prompt blocks

### Block T-DR-V1 — A Driver Didn't See the Rider

**Status:** `[AWAITING COPY LOCK from Copy_Treatments.md §T-DR-V1]`
**Designer anchor pick:** Coens dusk-intersection + Vignelli typography (CapCut pass)
**Visual treatment:** Dark-gradient photographic. Top 60% scrim. Bottom 35% photo bleed — Ty at intersection, helmet under R arm, leathers + Tech-Air vest, R-leg brace under denim, distant headlights blooming OOF.

**Prompt template:**
```
[REFERENCE IMAGE: Ty reference_lock loaded.]

Cinematic photographic still. The man in the picture — Ty, late-20s HVAC
tech / rider — stands at the Ahwatukee intersection where the crash
happened. Three-quarter body angle camera-left. Shoei helmet under his
RIGHT arm. Dainese leathers visible, with Tech-Air airbag vest as a slim
outer layer over the leathers (the airbag vest reads clearly as a separate
piece). RIGHT-leg brace partially visible under denim cuff just above the
boot.

Dusk light from frame-right (Coens-style hard-light shadow + warm amber key).
Headlights of distant cars blooming softly out of focus in the deep
background. Intersection traffic light just visible upper-frame. Cyan-fade
dusk sky overhead.

Composition: upper 60% of frame is the dusk sky + warm-charcoal scrim zone
for headline type. Lower 40% is the photo focus.

4:5 portrait. Mid-format film register: Mamiya 645 with 80mm equivalent,
ISO 400, natural light only. Coens-Fargo color palette — hard-shadow
warm-amber-against-cool-cyan. NO HDR. Tradesman-competence register.

NO text in the image. NO logos. NO graphic overlays.

Avoid: biker-stereotype glamour (chrome-and-leather poetry, freedom-of-the-
road register), AI tells, daylight, looking at camera, billboard energy.
```

**Iteration notes:** [empty]
**Failure flags:** Helmet in wrong arm. Tech-Air vest invisible / merging with leathers. Looking at camera. Biker-stereotype register.
**Winning seed:** [empty]

---

### Block T-DR-V2 — First-Offer Math, Rider

**Status:** `[AWAITING COPY LOCK from Copy_Treatments.md §T-DR-V2]`
**Designer anchor pick:** Bass anchoring + Soth kitchen photographic ground
**Visual treatment:** Top 70% Warm Charcoal solid field carrying two stacked hero numbers ($35,000 Cream / $33,700 Torch Amber) — type in CapCut. Bottom 25% photo bleed of Ty at kitchen table, ER discharge papers + Banner-Desert bills foreground, helmet on counter behind in OOF.

**Prompt template:**
```
[REFERENCE IMAGE: Ty reference_lock loaded.]

Tight composition. Ty seated at his kitchen table. Hospital discharge papers
+ Banner-Desert medical bill stack on the table foreground (recognizable
letterhead). RIGHT-leg brace partially visible under denim cuff. Shoei
helmet on the kitchen counter behind him in soft OOF (the bike isn't there
— only the helmet from the wreck).

Composition: upper two-thirds of frame is OOF kitchen wall as warm-charcoal
headroom that will receive the two-number type-anchor in CapCut. Lower 25%
is the photo focus — table, bills, hand, brace.

Late dusk warm window light from frame-right. Soth photographic register —
quiet, observational, financial-pressure-coded. Mid-format film, no HDR.

4:5 portrait. NO text overlays.

Avoid: text in image, biker-stereotype glamour, daylight, harsh light.
```

**Iteration notes:** [empty]
**Failure flags:** Helmet too prominent (compete with type composite); biker-stereotype register.
**Winning seed:** [empty]

---

### Block T-DR-V3 — Hero Number, 47%

**Status:** `[AWAITING COPY LOCK from Copy_Treatments.md §T-DR-V3]`
**Designer anchor pick:** Saul Bass single-idea-two-beats + Vignelli typography
**Visual treatment:** **No photograph.** Pure Roman Navy field. "47%" in Tiempos Headline 200-220pt Cream. 0.5pt Torch Amber rule. Caslon Pro small caps subhead.

**Generation tool:** ChatGPT Image 2.

**Prompt template:**
```
Editorial designed-static print ad. Pure Roman Navy field (#0D1F3C). Saul
Bass distillation — single dominant typographic element with ~25% empty
upper-quadrant negative space.

Center frame: the figure "47%" in Tiempos Headline serif at 200-220pt, Cream
(#FFF7F0). Below: 0.5pt Torch Amber horizontal rule, ~40% width, centered.
Below the rule: small-caps Caslon Pro at 22pt in Torch Amber — "OF ARIZONA
MOTORCYCLE CRASHES INVOLVE NO FAULT OF THE RIDER." on three lines.

Below: small body block in Caslon Pro 14pt at 50% Cream opacity.

Bottom-third: closing action line in Caslon Pro 18pt Torch Amber semi-bold.
Below: IBM Plex Mono 8pt source attribution in Muted Navy Light.

Vignelli grid, ~12% L/R margins. NO photograph, NO logo.

4:5 portrait.

Render text exactly as Copy Treatment §T-DR-V3. Verify spelling.
```

**Iteration notes:** Saul-flagged the 47% statistic for source verification — see Copy_Treatments §T-DR-V3 Saul note. If source-locked alternative is used (e.g., "3,036" hero with "Arizona motorcycle crashes, 2024"), update prompt accordingly.
**Failure flags:** Percent sign kerning / typography weight; small-caps tracking.
**Winning seed:** [empty]

---

### Block T-DR-V4 — Exhibit, Rider Compensation Comparison

**Status:** `[AWAITING COPY LOCK from Copy_Treatments.md §T-DR-V4]`
**Designer anchor pick:** Bass + Vignelli grid + Tufte
**Visual treatment:** **No photograph.** Cream field. Tufte chart, Tiempos headline, Torch Amber long bar / Muted Navy short bar.

**Generation tool:** ChatGPT Image 2.

**Prompt template:**
```
Editorial designed-static print ad. Pure Cream field (#FFF7F0). Tufte
data-ink minimum + Vignelli grid.

Top-left: Inter 9pt small caps Roman Navy: "EXHIBIT C".

Upper-third: headline Tiempos 32-36pt Roman Navy, two lines. Below: 0.5pt
Torch Amber rule, ~30% width.

Mid-frame: two horizontal bars only.
- Bar 1 (short): Muted Navy Light. Label above: "First offer". Range right.
- Bar 2 (~3-4× longer): Torch Amber. Label above: "Negotiated with counsel".
  Range right.

Below chart: IBM Plex Mono 9pt small caps Muted Navy chart-label.
Lower-third: closing line Caslon Pro 18pt Torch Amber. IBM Plex Mono 8pt
footer Muted Navy Light.

NO axis ticks, NO gridlines, NO percentages. ~30% white space.

4:5. NO photograph, NO logo.

Render exactly as Copy Treatment §T-DR-V4. Verify.
```

**Iteration notes:** [empty]
**Failure flags:** Bars not on baseline; range labels in wrong typeface.
**Winning seed:** [empty]

---

### Block T-DR-V5 — Left-Turn Presumption (ultra-lean)

**Status:** `[AWAITING COPY LOCK from Copy_Treatments.md §T-DR-V5]`
**Designer anchor pick:** Coens dusk-intersection
**Visual treatment:** Photographic-led, 70% scrim upper third. Middle 50% photo bleeds — Ty at the Ahwatukee intersection, helmet under R arm, leathers + Tech-Air vest, looking down/across at intersection lines.

**Prompt template:**
```
[REFERENCE IMAGE: Ty reference_lock loaded.]

Same composition family as Block T-DR-V1 — Ty at the Ahwatukee intersection
in three-quarter angle camera-left, helmet under RIGHT arm, leathers +
Tech-Air vest, looking down/across at painted intersection lines (NOT at
camera). RIGHT-leg brace under denim cuff.

Dusk sky cyan-fade, distant traffic light just visible upper-frame, distant
headlights blooming softly OOF.

Composition holds upper third as gradient-friendly OOF dusk sky for headline
scrim. Middle 50% is the photo focus. Bottom strip is gradient-light asphalt
for closing-line type in CapCut.

4:5 portrait. Coens-Fargo palette. NO text overlays.

Avoid: AI tells, daylight, harsh-flash, looking at camera, biker-glamour.
```

**Iteration notes:** [empty]
**Failure flags:** Composition reading too similar to V1 — slight angle / pose variation distinguishes them.
**Winning seed:** [empty]

---

### Block T-DR-V6 — Arizona Two-Year Window

**Status:** `[AWAITING COPY LOCK from Copy_Treatments.md §T-DR-V6]`
**Designer anchor pick:** Soth kitchen + Vignelli typography (CapCut pass)
**Visual treatment:** Dark-gradient photographic. Top 60% scrim. Bottom 30% photo bleed — Ty at kitchen table, helmet on counter OOF, ER discharge + bills foreground, R-leg brace under denim, late dusk light.

**Prompt template:**
```
[REFERENCE IMAGE: Ty reference_lock loaded.]

Same kitchen composition family as Block T-DR-V2 — Ty at his kitchen
table, ER discharge papers + Banner-Desert bills foreground, RIGHT-leg
brace partially visible, Shoei helmet on the kitchen counter behind him in
soft OOF, late dusk warm window light from frame-right.

Composition holds upper 60% as OOF kitchen wall scrim zone for headline +
subhead. Lower 30-35% is the photo focus.

4:5. Soth photographic register. NO text overlays.

Avoid: AI tells, biker-glamour, calendar/clock visible (compliance — no
specific date in-frame), daylight.
```

**Iteration notes:** [empty]
**Failure flags:** Calendar visible (NOT allowed — temporal cue lives in copy only).
**Winning seed:** [empty]

---

## CapCut layout spec

| Element | Font | Size | Color | Notes |
|---|---|---|---|---|
| V1/V2/V5/V6 Headline | Tiempos Headline | 40-60pt | Cream `#FFF7F0` | Upper-third on dark-gradient scrim |
| V1/V2/V5/V6 Subhead | Caslon Pro Italic | 18-22pt | Cream | Below headline |
| V1-V6 Closing action line | Caslon Pro Semi-Bold | 18pt | Torch Amber `#C8821A` | Lower-third, above Meta button |
| V1-V6 Footer disclaimer | IBM Plex Mono | 8pt | Warm Grey / Muted Navy Light | Bottom strip |
| V3 Hero Number | Tiempos Headline | 200-220pt | Cream | Center frame, dominates |
| V3/V4 Subhead small-caps | Caslon Pro Small Caps | 22pt | Torch Amber | Below structural rule |
| V3/V4 Body context | Caslon Pro | 14pt | Cream 50% / Roman Navy | Recedes |
| V4 Exhibit label | Inter Small Caps | 9pt | Roman Navy | Top-left |
| V4 Chart bar labels | Caslon Pro | 14pt | Roman Navy / Torch Amber | Above each bar |
| Fair Case torch | logo (white) | ~24px tall | white | Bottom-right, ~40px margin |

**Reels (9:16) extension** for V1, V2, V5, V6: animate environment — distant headlight glow shift + intersection traffic light cycle (V1, V5 — slow, ambient), bills page edge stir + window light shift (V2, V6).

---

## Cross-references

- Copy authority: `../Copy_Treatments.md`
- Sister lane: `../Primary/prompt_log.md`
- Designed Overlay System: `08_Brands/Second_Chair/02_Visual/Designed_Overlay_System.md`
- Designer anchors: `Abracadabra/04_Production/Giuseppe_Karma_(AI_Creative_Director)/Designed_Overlay_Reference/`
- Fair Case brand: `08_Brands/Second_Chair/20_Fair_Case/04_Visual_Identity_Brief/BRAND_SYSTEM_BRIEF.md`
- Branding-last-pass: memory `feedback_branding_last_pass.md`
- Higgsfield workflow: memory `feedback_higgsfield_workflow.md`
- Ty reference lock: `Renders/M1_Ty_Identity/Primary/` reference frame
- Setting research: `Audience/Deep_Personas/Ty/01_Life_World.md`

---

*Giuseppe scaffolding. McCabe wrote copy. Davis picks variant. Saul gates. — 2026-04-27*

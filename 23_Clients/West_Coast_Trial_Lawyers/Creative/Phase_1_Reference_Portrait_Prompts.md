# Phase 1 Reference Portrait Prompts — ChatGPT Images 2.0 via Higgsfield
## Second Chair × West Coast Trial Lawyers — Arizona Pilot

**Prepared:** 2026-04-22
**Room:** Giuseppe Karma (chair), Hegarty (emotional truth), Fink (art direction / side-specific craft), Indigo Sato (silent observer — downstream scene derivability), Phil Dusenberry (silent observer — reproducibility discipline). Liaison: Nigel Bogle.
**Upstream (archived 2026-04-23):** `Archive/Week_1_Launch_Concepts_2026-04-21.md` §"Protagonist Character Briefs" — retained for reference only. Current canonical persona source is `Audience/Deep_Personas/{Sarah,Diana,Laura,Ty}/` and the active creative package at `Creative/Week_1_Approval_Package/`.
**Scope:** Four reference portraits. Ty Rivera, Sarah, Laura, Diana. English-only, Phase 1. Miguel deferred to Phase 2.
**Purpose:** Davis pastes each prompt below into Higgsfield's ChatGPT Images 2.0 workflow, generates 4 candidates per character, picks one per character. That locked image becomes the character-consistency reference for every downstream scene prompt (M1/M2/M3/S1/S2/S5).

---

## Style system (2026-04-22 original; 2026-04-23 director-anchored upgrade)

The four reference prompts below are split across two SC style sheets that live in `../Style_Sheets/`:

- **Ty Rivera, Sarah, Laura** use **Elevated Documentary** (Luca Maxim × WCTL). See `Style_Sheets/Elevated_Documentary.md`. The prompts below bake in that sheet's §2b DIRECTOR-ANCHORED Image Injection Block inline so they're self-contained for copy-paste; treat the style sheet as the source of truth if prompts and sheet ever drift.
- **Diana** uses **UGC Native** (Barry Hott Doctrine × WCTL). See `Style_Sheets/UGC_Native.md`. Diana's prompt was rewritten 2026-04-22 to match UGC style because her one Phase 1 asset (S5 MVA — kitchen + handheld + envelopes falling) is UGC-allocated.

**Why two styles:** Phase 1 runs a 5-Elevated + 1-UGC creative test inside a single Meta ad set. Diana is the UGC test against the five Elevated assets. Side-specific props and character-as-insight specificity are preserved across both styles — the style shift only affects composition, lighting, grain, and color grade.

**2026-04-23 director-anchored rewrite + 2026-04-23 concrete-description refactor:** the three Elevated prompts (Ty, Sarah, Laura) were rewritten to LEAD with concrete photographic description (per `Prompting_Guides/ChatGPT_Image_2.md` §7: "GPT Image 2 responds to specific photographic vocabulary better than to vague aesthetic adjectives"), with director style described in prose rather than named as an abstract "anchor." The neutral-portrait light is **a single large north-facing window as the only key, painterly Vermeer-quality natural interior light** — described in concrete terms (direction / diffusion / falloff) that the image model can actually render. Paul Thomas Anderson's *Phantom Thread*, David Fincher's *Mindhunter* motivated-light discipline, and photographers Alec Soth + Nadav Kander appear as reinforcement prose. This is the "brief the photographer" pattern from the ChatGPT Image 2 guide §3 — tell the model what to shoot, not which director to be. Diana's UGC prompt retains the explicit NO director-anchor discipline.

**Important: the `Director_Reference_Library/` is a writing aid for Giuseppe (the prompt writer), not literal prompt content.** When Giuseppe reaches for "Mindhunter grammar" or "PTA portrait" or "Villeneuve grief weight," the output into the actual prompt is the *transliteration* of that director's visual register into concrete photographic vocabulary — not the director's name verbatim. Director names in prompts work best as light reinforcement, never as the primary anchor the model is asked to interpret.

*Motorcycle persona renamed 2026-04-22 from Marco Reyes (cruiser archetype, archived) to Ty Rivera (supersport archetype — 29-year-old Yamaha R6 rider in Tempe, 4x higher per-capita crash rate than cruiser riders). See `Audience/Deep_Personas/Ty_Rivera.md` for the full new persona and `Audience/Deep_Personas/Archive/Marco_Cruiser.md` for the archived cruiser source.*

---

## How to use this file (Phil)

**Tool:** Higgsfield, with the ChatGPT Images 2.0 (`gpt-image-2`, released 2026-04-21) model selected. If Higgsfield's UI still routes to `gpt-image-1` / GPT Image 1.5 under the same label, the prompt grammar here still works — just with lower text-in-image fidelity and no 4K single-pass; confirm the underlying snapshot in Higgsfield's model selector before production. Do NOT run these prompts in Nano Banana, Flux, Seedream, or Higgsfield Soul — the prompt grammar is tuned for ChatGPT Images 2.0's natural-language instruction-following. Outputs from other models will vary and break the consistency chain. Full model reference: `Abracadabra/04_Production/Giuseppe_Karma_(AI_Creative_Director)/Prompting_Guides/ChatGPT_Image_2.md`.

**Run settings per character:**
- **Aspect ratio:** 1:1 (square) or 4:5 (portrait). Pick one and keep it consistent across all four characters.
- **Candidates:** 4 per character. If Higgsfield shows meaningful variance in interpretation across one batch, generate a second batch of 4 and pick across all 8. Default: 4.
- **Seed:** do not fix the seed on the first batch — let it vary so the candidates differ. Record the winning seed per character after you lock your pick.
- **Reference image input:** none on this pass. These prompts are text-to-image. The *output* of this pass becomes the reference for every subsequent scene prompt.

**Lock protocol:**
1. Generate 4 candidates per character.
2. Check side-specific props FIRST, before face aesthetics — reject any candidate with a flipped prop (Ty's scar on the left eyebrow, Ty's tattoo on the left forearm, Sarah's brace on the right forearm, Laura's cane in the right hand, Laura's ACE wrap on the left ankle, Diana's sling on the left arm, Diana's bruise on the left jawline). A flipped prop breaks the downstream character lock even if the face is perfect.
3. Among the side-correct candidates, pick the one that reads most like the specific person the brief describes — not a generic working-class American.
4. Save the winning image to `Abracadabra/08_Brands/Second_Chair/23_Clients/West_Coast_Trial_Lawyers/Creative/Reference_Portraits/` (create folder if it doesn't exist) as `ty_reference_locked_v1.png`, `sarah_reference_locked_v1.png`, `laura_reference_locked_v1.png`, `diana_reference_locked_v1.png`.
5. Save a companion `{character}_reference_lock.md` alongside each image capturing: Higgsfield seed used, date locked, full prompt pasted in, one-line reason each of the 3 rejected candidates was rejected.

**Run order (recommendation, Giuseppe):** Run Ty FIRST to validate the Elevated Documentary grammar, then Diana SECOND to validate the UGC Native grammar. These two together confirm both style sheets are producing real-feeling output before you commit to Sarah and Laura (both Elevated). Ty is the highest-leverage Elevated character (3 of 6 downstream assets, most distinctive visual anchors — eyebrow scar, right-forearm tattoo, lean build); Diana is the only UGC asset so she must stand on her own. If either first run reads generated, tune that style sheet's Injection Block (for Elevated: add more grain + imperfection, drop "photorealistic" which can push ChatGPT Images 2.0 toward uncanny; for UGC: remove any accidental cinematic vocabulary, double-down on phone-camera specificity) before running the other three characters.

---

## Prompt 1 — Ty Rivera (supersport / identity loss) — Elevated Documentary

**Style sheet:** `Style_Sheets/Elevated_Documentary.md`
**Deep persona:** `Audience/Deep_Personas/Ty_Rivera.md`

Paste the block below into Higgsfield's ChatGPT Images 2.0 prompt field verbatim.

```
A documentary photorealistic waist-up portrait of a specific young-adult American man, indistinguishable from a real digital camera photograph. Shot in the quiet naturalism of Paul Thomas Anderson's Phantom Thread interiors — a single large north-facing window as the only key light, positioned camera-right, diffused, producing soft directional falloff across the face from bright camera-right to gently shadowed camera-left. Painterly Vermeer-quality natural interior light. No three-point cinema setup, no soft-box glamour, no bounce fill — one window doing all the work. Subject and light share the room honestly.

Reference aesthetic: Alec Soth portraits of American working-class subjects for the honest dignity, Nadav Kander portrait compositional rigor for the still weight. Every light source is one you could point to in the room (David Fincher's Mindhunter discipline on motivated-light-only).

Capture format: Fujifilm X-T5 or Sony A7R IV digital look, 50mm prime lens, f/2.8. Subtle-to-moderate 35mm Kodak Vision3-adjacent film grain, honest skin saturation, no HDR, no over-sharpening, no airbrushing. Skin texture must show pores, fine lines, subtle asymmetry — his face is not symmetrical. Hair has flyaways and an imperfect part. Eyes show a single soft catchlight from the window.

Focus plane: eyes sharp at f/2.8, ears already softening, background out-of-focus but legibly dimensional (not abstract blur).

Framing: waist-up, three-quarter body angle turned slightly to camera-left, head turned to face camera directly, eyes to camera. Subject inhabits the frame completely — composed, present, owning the space he occupies. Neutral soft warm-grey or cream out-of-focus background with gentle depth. Composition rule-of-thirds with subject's eyes on the upper-third horizontal line — NOT dead-centered. Aspect ratio 4:5.

Blocking: standing still, weight balanced evenly — composed, not burdened, not performing. Hands visible: RIGHT hand at his side with forearm slightly forward (showing the right-forearm tattoo); LEFT hand at his side or resting on the opposite forearm (showing the wedding band on his left hand). No gesture. Mouth closed or relaxed (no mid-word speech shape, no teeth showing). Micro-settle of weight only.

Subject: Ty Rivera, 29, white (Arizona-native, Spanish surname with mixed Anglo / slight Southwest features), Tempe Arizona. Working-class HVAC tech and supersport rider, quiet confident energy. 5'10", 165 lbs, lean-athletic build (a rider's build, not bulky), sun-tanned skin with moderate Arizona sun exposure — NOT weathered (too young for deep weather lines, only the faintest early crow's feet from desert squinting). Short dark-brown hair, slightly overgrown from 3 weeks post-hospital, messy natural part, no gray. Clean-shaven or 2-day stubble (not a full beard — he shaves for work). A small scar above his RIGHT eyebrow (the scar is above Ty's OWN right eyebrow, which appears on the viewer's LEFT side of the frame in a camera-facing portrait) from a dirtbike spill years ago. Blue, hazel, or green-brown eyes. A small healing abrasion on his RIGHT cheekbone from his recent crash (faintly pink/healing, not fresh red, not bandaged).

Wardrobe: a plain black or faded-black cotton crew-neck t-shirt (no logos, or at most a small faded Yamaha tuning-fork chest logo). NO leather vest. NO leather jacket. NO helmet in frame. Simple, at-rest — this is a neutral reference portrait; ad scenes later will dress him in full Alpinestars leathers. Background is neutral — no motorcycle, no canyon, no garage in frame.

Arms and hands: lean forearms with visible musculature. A small black-ink tattoo on his RIGHT forearm — his grandfather's initials in simple script (2-3 letters, ~1 inch tall, not a sleeve, not decorative). Working hands with a light HVAC-trade callus at the base of the palm — real working hands but not the heavy calluses of an older tech. Short clean nails. A simple titanium or silver wedding band on his LEFT hand.

Emotional register: not defeated, not angry — thoughtful, grounded, quietly confident. Present, not performing. A young husband and working-class tradesman who took his full riding gear seriously and survived a crash a less-geared-up rider might not have. He was a week away from a normal Tuesday and now isn't. Clear eyes, steady gaze.

Critical side-specific details to lock:
- The small eyebrow scar is on Ty's OWN RIGHT eyebrow. Do not flip it to his left.
- The small forearm tattoo is on Ty's OWN RIGHT forearm. Do not flip it to his left.
- The wedding band is on Ty's OWN LEFT hand. Do not flip it to his right.
- The healing abrasion is on his OWN RIGHT cheekbone, same side as the eyebrow scar.

Do NOT generate a cruiser-biker stereotype: no leather vest, no patches, no handlebar mustache, no long beard, no tough-guy scowl, no cruiser-rider aesthetic. Do NOT generate a sportbike-squid stereotype: no shirtless gym-body aesthetic, no racing helmet in the reference frame, no leather race suit in the reference frame, no motorcycle of any kind in the reference frame, no neck or chest tattoos, no visible bandages. No hospital context. No race track, no canyon road, no garage. Reference portrait is neutral on purpose — the motorcycle, helmet, and leathers live in downstream scene prompts, not here.

Failure flag review (regenerate if any hit):
- FLAT EVEN LIGHTING (no directional falloff across the face) → the single-window setup didn't take; reinforce "single large north-facing window as the only key, camera-right, soft directional falloff from bright camera-right to gently shadowed camera-left, like a Vermeer interior."
- CENTERED SYMMETRIC COMPOSITION → rule-of-thirds with eyes on upper-third line was specified; regen.
- EVERYTHING IN FOCUS → eyes sharp + ears softening + background soft; regen with focus-plane language reinforced.
- WAXY / AIRBRUSHED / PLASTIC SKIN → Fujifilm X-T5 + Vision3 grain didn't take; reinforce camera-body and grain phrases.
- MODEL-FACE SYMMETRY → explicit "face is not symmetrical, subtle asymmetry around the eyes" reinforcement needed.
- POSED / PERFORMED EXPRESSION → reinforce "not performing, present, clear eyes, quiet confidence."

Do NOT generate any AI tells: no waxy or plastic skin, no symmetrical faces, no uncanny eyes, no extra or malformed fingers, no floating hair, no distorted hands, no over-saturated color, no HDR look, no over-sharpened edges, no airbrushed finish, no text in image, no watermark, no model-face symmetry, no tattoo sleeves.
```

---

## Prompt 2 — Sarah (trucking / career threat, ICU nurse) — Elevated Documentary

**Style sheet:** `Style_Sheets/Elevated_Documentary.md`

Paste the block below into Higgsfield's ChatGPT Images 2.0 prompt field verbatim.

```
A documentary photorealistic waist-up portrait of a specific middle-aged American woman, indistinguishable from a real digital camera photograph. Shot in the quiet naturalism of Paul Thomas Anderson's Phantom Thread interiors — a single large north-facing window as the only key light, positioned camera-right, diffused, producing soft directional falloff across the face from bright camera-right to gently shadowed camera-left. Painterly Vermeer-quality natural interior light. No three-point cinema setup, no soft-box glamour, no bounce fill — one window doing all the work.

Reference aesthetic: Alec Soth portraits of American working and middle-class subjects for the honest dignity, Nadav Kander portrait compositional rigor for the still weight. Every light source is one you could point to in the room (David Fincher's Mindhunter discipline on motivated-light-only).

Capture format: Fujifilm X-T5 or Sony A7R IV digital look, 50mm prime lens, f/2.8. Subtle-to-moderate 35mm Kodak Vision3-adjacent film grain, honest skin saturation, no HDR, no over-sharpening, no airbrushing. Skin texture must show pores, fine lines, subtle asymmetry — her face is not symmetrical. Hair has flyaways and an imperfect pulled-back look. Eyes show a single soft catchlight from the window.

Focus plane: eyes sharp at f/2.8, ears already softening, background out-of-focus but legibly dimensional.

Framing: waist-up, three-quarter body angle turned slightly to camera-left, head turned to face camera, eyes to camera. Subject inhabits the frame completely — composed, present. Neutral soft warm-grey or cream out-of-focus background with gentle depth. Composition rule-of-thirds with eyes on upper third. Aspect ratio 4:5.

Blocking: standing or seated still, weight composed (not burdened, not glamour-posed). Hands visible and specifically positioned to show the brace: her LEFT forearm with the brace is visible in frame (appears on viewer's RIGHT side); her LEFT hand rests at her lap or crossed at her waist, showing the white-gold wedding band. Mouth closed or relaxed (no mid-word speech shape). Micro-movement only — a slow exhale, fatigue in the set of her shoulders.

Subject: Sarah, 38, racially ambiguous / mixed white-Latina (reads as white-passing in some frames, Latina in others — Arizona-native features), 5'6", athletic-but-soft build of a working ICU nurse. Shoulder-length dark-brown hair pulled back loosely with a few pieces falling loose at the temples, minimal makeup, small stud earrings, no watch. Warm hazel eyes with visible fatigue — she has been running on four hours of sleep for months. A small scar on her chin from childhood. Pale-blue hospital scrubs visible under an open beige or tan zip-up jacket.

Injury / continuity prop: a soft BLACK canvas arm brace with Velcro straps worn on her LEFT forearm (Sarah's own left arm, which on a camera-facing portrait appears on the viewer's RIGHT side of the frame). The brace must be visible. Her LEFT hand rests at her lap or crossed at her waist, showing a thin white-gold wedding band.

Emotional register: the woman who absorbs other people's crises for a living, now quietly absorbing her own. Not crying, not panicked — tired, grounded, holding the world's smallest frown. A nurse who has been holding the world together and is starting to feel it. Present, not performing. Fatigue in the eyes and the set of the jaw, but composed — she is still the one others lean on.

Critical side-specific detail to lock: the black canvas arm brace is on Sarah's OWN LEFT forearm. Do not flip it to her right. The wedding band is on her LEFT hand, same arm as the brace. Do not flip it.

Do NOT generate: nurse stereotype (no stethoscope around neck, no clipboard, no scrub cap, no hospital hallway setting), no glamour lighting, no heavy makeup, no youthful model face — she is 38 and she has lived. No smiling, no pained expression.

Failure flag review (regenerate if any hit):
- FLAT EVEN LIGHTING (no directional falloff) → single-window setup didn't take; reinforce "single north-facing window camera-right as only key, soft directional falloff."
- CENTERED SYMMETRIC COMPOSITION → rule-of-thirds was specified; regen with eyes on upper-third.
- EVERYTHING IN FOCUS → eyes sharp + ears softening + background soft; regen with focus-plane reinforced.
- WAXY / AIRBRUSHED SKIN → reinforce Fujifilm X-T5 + Vision3 grain language; her fatigue and 38-years-lived texture should be visible.
- MODEL-FACE SYMMETRY → "face is not symmetrical, subtle asymmetry, visible fatigue in eyes" reinforcement.
- YOUTHFUL / GLAMOUR FACE → Sarah is 38 and lived — if the output looks 28 and polished, reinforce "middle-aged, subtle fatigue, no glamour."
- BRACE ON WRONG ARM → critical side-specific lock — regen with explicit "brace on Sarah's OWN LEFT forearm (viewer's RIGHT side of frame)" reinforcement.

Do NOT generate any AI tells: no waxy or plastic skin, no symmetrical faces, no uncanny eyes, no extra or malformed fingers, no floating hair, no distorted hands, no over-saturated color, no HDR look, no over-sharpened edges, no airbrushed finish, no text in image, no watermark.
```

---

## Prompt 3 — Laura (pedestrian / suburban safety loss) — Elevated Documentary

**Style sheet:** `Style_Sheets/Elevated_Documentary.md`

Paste the block below into Higgsfield's ChatGPT Images 2.0 prompt field verbatim.

```
A documentary photorealistic waist-up portrait of a specific middle-aged American woman, indistinguishable from a real digital camera photograph. Shot in the quiet naturalism of Paul Thomas Anderson's Phantom Thread interiors — a single large north-facing window as the only key light, positioned camera-right, diffused, producing soft directional falloff across the face from bright camera-right to gently shadowed camera-left. Painterly Vermeer-quality natural interior light. No three-point cinema setup, no soft-box glamour, no bounce fill — one window doing all the work.

Reference aesthetic: Alec Soth portraits of American middle-class subjects for the honest dignity, Nadav Kander portrait compositional rigor for the still weight. Every light source is one you could point to in the room (David Fincher's Mindhunter discipline on motivated-light-only).

Capture format: Fujifilm X-T5 or Sony A7R IV digital look, 50mm prime lens, f/2.8. Subtle-to-moderate 35mm Kodak Vision3-adjacent film grain, honest skin saturation, no HDR, no over-sharpening, no airbrushing. Skin texture must show pores, fine lines, subtle asymmetry — her face is not symmetrical, with faint laugh lines visible (critical — she is 42 and looks it in the good way). Hair has flyaways with a few pieces loose from a low ponytail. Eyes show a single soft catchlight from the window.

Focus plane: eyes sharp at f/2.8, ears already softening, cane visible in lower frame but softened, background out-of-focus but legibly dimensional.

Framing: waist-up, three-quarter body angle turned slightly to camera-left, head turned to face camera, eyes to camera. She is standing, weight shifted subtly onto her LEFT side (her cane side). Subject inhabits the frame completely — composed, present. Neutral soft warm-grey or cream out-of-focus background with gentle depth. Composition rule-of-thirds with eyes on upper third. Aspect ratio 4:5.

Blocking: standing still, weight shifted slightly to the cane side (LEFT), body honest about the injury without performing it. Her LEFT hand holds the cane at her side, cane top visible in frame. Her RIGHT hand at her side or across her waist. Mouth closed or relaxed (no mid-word speech shape). Micro-movement only — a slow exhale, a slight natural settle. Quiet domestic-realism dignity in the standing posture.

Subject: Laura, 42, white, suburban Phoenix (Chandler / Gilbert / Ahwatukee). 5'5", average build of a working mom who used to walk 3 miles a day before the accident. Shoulder-length light-brown hair with sun-lightened ends, pulled back in a low ponytail with a few pieces loose at the temples and nape. Minimal makeup, faint laugh lines, green or blue-green eyes, a subtle freckle pattern across the bridge of her nose. A small old healed scar on her LEFT forearm from a kitchen accident. Wardrobe: a soft cream or pale-gray cardigan over a plain white or light-grey t-shirt, well-worn medium-wash jeans. A thin silver chain at the collar. Small stud earrings. Plain white-gold wedding band on her LEFT hand.

Injury / continuity prop: a walking cane in her LEFT hand (Laura's own left hand, which on a camera-facing portrait appears on the viewer's RIGHT side of the frame). She was struck on her right side, so her weight is shifted slightly to the cane side. The cane is a simple modern hospital-issue or wooden walking cane with a curved handle, resting against the ground at her left side — the cane's top is visible in frame, held in her left hand.

Emotional register: the woman who used to walk the neighborhood every morning — past neighbors' dogs, school drop-off, the same route for fifteen years — and now can't walk it the same. Not pitied, not broken, quietly stubborn. A woman taking stock of what happened. Present, not performing. The laugh lines are the tell — she's a person who laughed a lot before this, and still will.

Critical side-specific detail to lock: the cane is in Laura's OWN LEFT hand. Do not flip it to her right hand. The small old scar on her LEFT forearm should be visible if her forearm is in frame — on her own left arm. The wedding band is on her LEFT hand, same arm as the cane.

Do NOT generate: glamour-shot aesthetic, youthful model face (she is 42 and looks it in the good way — visible laugh lines, not airbrushed), no "dramatic injury victim" pose, no tears, no hospital context, no wheelchair, no visible ankle wrap or medical devices other than the cane (the ACE wrap at her right ankle lives under the jean cuff and is not needed in this waist-up portrait), no cane in the wrong hand.

Failure flag review (regenerate if any hit):
- FLAT EVEN LIGHTING → single-window setup didn't take; reinforce "single north-facing window camera-right as only key, soft directional falloff like a Vermeer interior."
- CENTERED SYMMETRIC COMPOSITION → rule-of-thirds was specified.
- EVERYTHING IN FOCUS → eyes sharp + ears softening + background soft.
- WAXY / AIRBRUSHED / YOUTHFUL FACE → she is 42 with laugh lines; reinforce "visible laugh lines, 42 years old and lived, no airbrushing, no model-face symmetry."
- CANE IN WRONG HAND → critical side-lock failure — regen with explicit "cane in Laura's OWN LEFT hand (viewer's RIGHT side of frame)" reinforcement.
- "DRAMATIC INJURY VICTIM" POSE → no performance of the injury; she's standing composed, weight shifted honestly to cane side but NOT performing pain.

Do NOT generate any AI tells: no waxy or plastic skin, no symmetrical faces, no uncanny eyes, no extra or malformed fingers, no floating hair, no distorted hands, no over-saturated color, no HDR look, no over-sharpened edges, no airbrushed finish, no text in image, no watermark.
```

---

## Prompt 4 — Diana (MVA / control loss, office manager) — UGC Native

**Style sheet:** `Style_Sheets/UGC_Native.md`

Paste the block below into Higgsfield's ChatGPT Images 2.0 prompt field verbatim.

```
Director anchor: EXPLICITLY NONE. UGC Native rejects all director / cinematographer / film-stock references on principle (see Style_Sheets/UGC_Native.md §1.5). This prompt commits to phone-camera vocabulary only. The closest aesthetic reference allowed is "someone's spouse or sister filmed this on their phone from across the kitchen table" — never invoked with a cinematic shorthand.

An iPhone 14 Pro or Samsung Galaxy S24 phone camera photo of a specific middle-aged American woman, indistinguishable from a real phone camera image. Natural window daylight from the side, flat phone color with auto-white-balance feel. No studio lighting. No cinematic color grade. Slightly shaky handheld framing, as if the person filming her is standing in her kitchen holding the phone one-handed. Unposed, imperfect composition. Subject caught mid-moment — she just glanced up from something on the table.

Phone-sensor focus behavior: deep focus throughout (phone cameras physically cannot produce shallow DOF / bokeh). Skin imperfection preserved honestly — the phone captures pores, fine lines, subtle asymmetry, faint under-eye shadow from four hours of sleep. No airbrushing. No smoothing. No film grain (phone sensors produce digital noise if anything, not cinematic grain — the prompt should include "phone-sensor clean-to-slightly-noisy capture, NO film grain").

Framing: waist-up, slightly off-center (subject positioned toward camera-left). Aspect ratio 4:5 or 1:1. Background: her own kitchen — soft out-of-focus cabinetry or wall (from depth, not shallow DOF), perhaps a coffee cup or stack of envelopes visible at the edge of frame. Composition is NOT photographic — composed as if her husband or sister filmed her from across the kitchen table without her posing. Phone-camera imperfect framing: subject's head might cut into upper 10% of the frame, or there's too much headroom — natural misframing.

Subject: Diana, 42, white (Arizona-native, mixed Anglo / slight Mediterranean read), Chandler Arizona (East Valley). 5'4", slim-athletic build of a working mom who used to do yoga twice a week before the accident. Shoulder-length light-brown hair with subtle highlights pulled into a loose low ponytail, minimal makeup (she used to wear more), a pair of reading glasses pushed up into her hair above her forehead. Warm blue-green eyes, subtle crow's feet, a small mole above her LEFT upper lip. Wardrobe: a pale yellow or cream cardigan over a plain white t-shirt — work-from-home post-injury outfit. Thin silver necklace. Simple plain wedding band on her LEFT ring finger.

Injury / continuity prop: a medical-grade BLACK fabric arm sling cradling her RIGHT arm (Diana's own right arm, which on a camera-facing portrait appears on the viewer's LEFT side of the frame). The sling strap runs diagonally across her body from her LEFT shoulder down to her RIGHT hip, cradling her right forearm bent at the chest. The sling must be clearly visible.

Additional continuity detail: a faint yellowing fading bruise visible along her RIGHT jawline — old, not fresh. Pale yellow-green tone, not purple, not red. It should read as healing, not acute.

Emotional register: the woman who ran her household and three kids' schedules from memory and now can't hold her coffee right. Competent, composed, quietly exhausted. A professional at home, not a patient. Tired but not sick. Kept it together for her kids all month. NOT performing emotion — caught being herself for a second while her husband filmed her.

Critical side-specific detail to lock: the black fabric arm sling cradles Diana's OWN RIGHT arm, strap crossing from her LEFT shoulder to her RIGHT hip. Do not flip the sling. The faint healing bruise is on her OWN RIGHT jawline, same side as the slung arm. Do not put it on her left jaw. The small mole is above her LEFT upper lip.

Do NOT generate hospital-patient aesthetic (no gown, no IV, no wheelchair, no hospital bed), no fresh bruises or stitches or red-purple bruising (the bruise is OLD and fading yellow), no ultra-youthful aesthetic, no pained expression, no sling on the wrong arm, no bruise on the wrong side of her jaw.

Do NOT generate cinematic/editorial aesthetic: no film grain (phone cameras don't produce cinematic grain), no shallow depth of field (phone cameras have deep focus), no cinematic color grading, no desaturated with lifted blacks, no motivated dramatic lighting, no studio lighting, no glamour lighting, no heavy makeup, no Deakins reference, no Alec Soth reference, no Nadav Kander reference, no Mindhunter reference, no Villeneuve reference, no PTA reference, no Fincher reference, no cinematographer / director anchor of any kind, no "ad" quality, no perfect framing, no centered composition, no posed subject, no performed emotion.

Failure flag review — UGC-specific (regenerate if any hit):
- SHALLOW DEPTH OF FIELD / BACKGROUND BLUR → phones can't do this; reinforce "deep focus throughout, phone-sensor sharp background-to-foreground."
- DESATURATED / GRADED / CINEMATIC COLOR → phones use auto-WB; reinforce "flat phone color, auto-white-balance, no grading."
- MOTIVATED DRAMATIC LIGHTING / DEEP SHADOW FALLOFF → phones fill shadows; reinforce "even natural room light, phone-camera auto-exposure behavior, no deep shadow."
- FILM GRAIN PRESENT → phones don't produce cinematic grain; reinforce "NO film grain."
- CENTERED / COMPOSED FRAMING → UGC is imperfectly framed; reinforce "slightly off-center, imperfect phone framing, subject caught mid-moment."
- POSED / PERFORMED SUBJECT → reinforce "not posing, caught being herself, natural glance off-camera briefly."
- ANY CINEMATOGRAPHER / DIRECTOR REFERENCE leaks into output → scan the prompt — remove any accidental reference before re-running.
- GLAMOUR / AIRBRUSHED FACE → Diana is 42 and tired; reinforce "honest skin with fatigue visible, no airbrushing, no glamour."
- SLING ON WRONG ARM → critical side-lock — regen with explicit "sling on Diana's OWN RIGHT arm, strap from LEFT shoulder to RIGHT hip."

Do NOT generate any AI tells: no waxy or plastic skin, no symmetrical faces, no uncanny eyes, no extra or malformed fingers, no floating hair, no distorted hands, no over-saturated color, no HDR look, no over-sharpened edges, no airbrushed finish, no text in image, no watermark.
```

---

## After you lock the four references

1. **Save the four locked images** to `Creative/Reference_Portraits/` using the naming convention above.
2. **Save the four lock records** (`{character}_reference_lock.md`) with seed + prompt + rejection notes.
3. **Side-by-side continuity gate before moving to scene prompts:** line up the four locked portraits next to each other. Read them as a set. Do they read as four different specific people with distinct faces, or do they read as variations on a generic "American in their late 20s / early 40s"? If the latter, re-lock the weakest one with the distinguishing-feature lever turned up (Ty's eyebrow scar and right-forearm tattoo; Sarah's chin scar and visible fatigue; Laura's nose freckles and laugh lines; Diana's mole above the left lip and the yellowing jaw bruise).
4. **Downstream viability check (Indigo):** the reference portraits are lit neutrally on purpose so they re-light cleanly into Ty's scenes (M1/M2/M3 — bike garage, kitchen, dusk intersection per the supersport archetype — see `Creative/Week_1_Approval_Package/04_M1_Ty_Identity.md`, `05_M2_Ty_Loss.md`, `06_M3_Ty_Injustice.md` for current canonical scene specs; the old `Archive/Week_1_Launch_Concepts_2026-04-21.md` reflects the cruiser-era world and is archive-only), Sarah's kitchen at morning (S1), Laura's suburban crosswalk at dusk (S2), and Diana's kitchen in morning light (S5). If any of the four locked portraits is so specifically-lit that it reads "indoor overcast day" and nothing else, re-lock that character with even softer, more neutral light. Scene prompts later will reference the locked image for face + wardrobe + props — but the lighting will be redirected per scene, so the reference must accept re-lighting.
5. **Next session:** Giuseppe writes the six scene prompts (M1/M2/M3/S1/S2/S5) against the four locked references. Bring Abracadabra back in when ready.

---

## Open questions surfaced during this session

- **Aspect ratio choice.** 1:1 vs. 4:5 — Davis picks. 1:1 is a tighter reference; 4:5 gives more room for cane (Laura) and sling strap (Diana) to read cleanly. Recommendation: **4:5 for all four for consistency, easier to crop down to 1:1 later than to expand up**.
- **Face variation across re-runs of the same prompt in Higgsfield's ChatGPT Images 2.0.** First time Davis has run this specific tool + model combo on WCTL characters. If variance is high, the Phil-level solution is to lock the winning seed AND use that seed as a starting point for any needed re-generations. If variance is low enough that the prompt alone holds, seeds are a nice-to-have, not required.
- **Reference image input for future scene prompts.** Once locked, scene prompts will reference these images via Higgsfield's character-consistency feature (ChatGPT Images 2.0 supports reference input on Higgsfield's UI). Confirm this works before scene-prompt session — if not, we fall back to very detailed textual character briefs pasted into every scene prompt.

---

*Drafted by: Giuseppe Karma (chair), with Hegarty (emotional truth), Fink (side-specific craft), Indigo Sato (downstream scene viability, silent observer), Phil Dusenberry (reproducibility, silent observer). Liaison: Nigel Bogle. For Davis to run through Higgsfield — not yet sent to Robert.*
*Second Chair × West Coast Trial Lawyers — Arizona Pilot — Phase 1 Reference Portraits — April 2026.*

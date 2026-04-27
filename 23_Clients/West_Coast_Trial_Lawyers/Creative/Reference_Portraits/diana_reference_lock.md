# Diana — Reference Portrait Lock Record

**Character:** Diana Nguyen, 42, Senior Office Manager, Chandler AZ
**Locked image:** `diana_reference_locked_v1.png`
**Date locked:** 2026-04-25
**Source filename:** `hf_20260425_204322_da4b24c5-e051-48b5-9c2b-b15eb51e71ea.png`
**Tool:** Higgsfield × ChatGPT Images 2.0
**Aspect ratio:** 3:4 (closest match to brief's 4:5; 4:5 unavailable in Higgsfield UI)
**Seed:** TBD (record from Higgsfield UI when available)
**Register:** UGC-Native (the only UGC asset in the Week 1 set — must stand alone)

---

## UGC discipline check (PASS — this is the harder lock)

ChatGPT Images 2.0 defaults toward cinematic vocabulary. This gen resisted that completely:

- ✅ Phone-sensor DEEP focus throughout (kitchen cabinetry receding sharply, NO bokeh, NO shallow DOF)
- ✅ Flat phone color, auto-white-balance feel — NO cinematic grade, NO desaturation, NO lifted blacks
- ✅ Natural window daylight from camera-right — NO studio illumination, NO motivated dramatic falloff
- ✅ NO film grain — clean digital phone-sensor capture
- ✅ Slightly off-center, mildly imperfect framing — head sits in upper-mid third, room around her, feels caught not composed
- ✅ NOT posed — eyes meet camera in a "just glanced up" register, slightly unguarded, NOT performing
- ✅ Coffee mug visible at bottom of frame at the table edge, kitchen cabinetry behind = "filmed by Ben from across the kitchen table" register landed
- ✅ NO 50mm cinematic lens look — reads as ~28mm phone-wide equivalent

This is the part of the brief where most UGC gens fail (cinematic reflex creeps in). This one didn't.

---

## Side-specific lock check (PASS)

- ✅ BLACK fabric arm sling cradling Diana's OWN RIGHT arm (viewer's LEFT side of frame)
- ✅ Sling strap diagonal LEFT shoulder → RIGHT hip — strap visible crossing the body cleanly
- ✅ Pale buttery YELLOW cardigan over plain white t-shirt — exactly the work-from-home outfit spec
- ✅ Loose low ponytail with face-framing pieces loose at the temples
- ✅ Subtle highlights in shoulder-length light-brown hair
- ✅ Warm blue-green eyes with slight undereye fatigue — "kept it together for her kids all month" register
- ✅ Composed, NOT pained, NOT pity-bait — competent at home, NOT a patient
- ✅ Wedding band on LEFT (hand not visible in this frame; will re-introduce explicitly in scene prompts where hand is in frame)

## Two minor reference misses (acceptable — handle in scene prompts)

- ⚠ **Reading glasses pushed up into hair** — NOT visible in this gen. Optional brief detail; will add explicitly in S5 scene prompts as *"reading glasses pushed up into her hair above the forehead"* where the work-from-home register matters.
- ⚠ **Faint yellowing healing bruise on RIGHT jawline** — not legibly visible at this resolution; right jaw partially obscured by hair / sling strap. Will add explicitly in scene prompts where the right jaw is more visible: *"a faint yellowing fading bruise visible along her RIGHT jawline, pale yellow-green tone, healing not fresh."*
- ⚠ **Small mole above LEFT upper lip** — not legible at portrait scale. Will add explicitly in close-up scene prompts where the face is large enough for the detail to read.

These three misses are best-handled scene-by-scene rather than re-rolling the lock — the UGC discipline is the hard part and this gen nailed it. Re-rolling risks losing the phone-camera authenticity to chase a small detail.

---

## Why this candidate

- **UGC discipline landed** — flat phone color, deep focus, natural light from camera-right, mildly off-center framing, NOT posed. Hardest part of the brief, cleanly executed.
- **Emotional register** — "competent, composed, quietly exhausted." The undereye fatigue is honest, NOT theatrical. She's tired but not sick. Caught being herself. Exactly Diana's register from `Audience/Deep_Personas/Diana/02_Emotional_Architecture.md`.
- **Side-prop legibility** — the sling and the diagonal strap are both unambiguously visible. The two most-critical Diana props locked.
- **Kitchen context** — coffee mug, cabinetry, "her own kitchen filmed by her husband" = the Ben-filmed-this aesthetic from the brief.
- **Wardrobe locked** — pale yellow cardigan over white tee, exactly to spec, not a yellow that drifts toward beige or mustard.

## Saved alternates

None — this was a winner gen. If we ever need a second-pose Diana for a non-kitchen scene (e.g., V4 2-4AM living-room couch), we'll generate a fresh UGC scene rather than re-using a portrait alternate.

---

## Downstream re-lightability notes

The UGC discipline means this reference is **already in scene-light** (Diana's own kitchen at her own table during the day). Unlike the Elevated Documentary references (Sarah, Laura, Ty), Diana's downstream scenes will NOT re-light her — they'll re-stage her in different UGC contexts:

- **S5 Primary kitchen island** — same kitchen, island angle, envelopes falling, paused laptop, kids' homework
- **S5-V1 family system frames** — UGC scene of objects (backpacks, calendar, bills) cut with Diana face shot
- **S5-V2 invisible labor** — UGC scene with calendar/permission slip props, optional Ben in frame
- **S5-V3 numeric shock** — same kitchen, prop documents (offer letter, ER bill) close-up
- **S5-V4 2-4AM low-light couch** — DIFFERENT lighting from the reference: phone-screen glow on Diana's face in low ambient living room, household dark. This is the trickiest re-light — must hold UGC discipline while shifting from daylight to phone-glow.
- **S5-V5 construction-family** — same kitchen UGC, plus paired pay-stub props + Ben's F-150 framed through window

Reference works for daylight UGC scenes natively. V4 (2-4AM low-light) will need explicit phone-screen glow lighting block to overcome the reference's daylight bias.

---

## Generation prompt (verbatim — Phase 1 Prompt 4 from Phase_1_Reference_Portrait_Prompts.md)

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

Do NOT generate any AI tells: no waxy or plastic skin, no symmetrical faces, no uncanny eyes, no extra or malformed fingers, no floating hair, no distorted hands, no over-saturated color, no HDR look, no over-sharpened edges, no airbrushed finish, no text in image, no watermark.
```

---

## Notes for downstream scene prompts

- **Wedding band** — not visible in reference (hand below frame). Add explicitly in scene prompts where hands are visible: *"thin silver wedding band on her LEFT ring finger visible."*
- **Reading glasses pushed up into hair** — not present in reference. Add explicitly when work-from-home register matters: *"a pair of reading glasses pushed up into her hair above the forehead."*
- **Yellowing bruise R jawline** — not legibly visible in reference. Add explicitly in scene prompts where the right jaw is in frame: *"a faint yellowing fading bruise visible along her RIGHT jawline, pale yellow-green tone, healing not fresh."*
- **Mole above LEFT upper lip** — not legible at portrait scale. Add explicitly in close-up scene prompts where the face is large enough to read it.
- **Wardrobe locked across S5:** pale yellow cardigan over white tee + jeans (or gray sweatpants for V4 2-4AM couch).
- **UGC discipline holds across all S5 scenes** — phone wide ~28mm, deep focus, flat phone color, NO film grain, NO cinematic, NO director references. Re-paste UGC discipline language in every scene prompt — ChatGPT Images 2.0 will drift toward cinematic if not held.

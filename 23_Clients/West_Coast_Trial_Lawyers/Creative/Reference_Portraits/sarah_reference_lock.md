# Sarah — Reference Portrait Lock Record

**Character:** Sarah Mitchell, 38, Trauma ICU Charge Nurse, Flagstaff Medical Center
**Locked image:** `sarah_reference_locked_v1.png`
**Date locked:** 2026-04-25
**Source filename:** `hf_20260425_034459_432d79d4-0164-4294-bf32-395db67d68f0.png`
**Tool:** Higgsfield × ChatGPT Images 2.0
**Aspect ratio:** 3:4 (4:5 unavailable in Higgsfield UI; 3:4 is closest match)
**Seed:** TBD (record from Higgsfield UI when available)

---

## Side-specific lock check (PASS)

- ✅ Black canvas arm brace on Sarah's OWN LEFT forearm (appears on viewer's RIGHT side of frame)
- ✅ Wedding band on LEFT hand (hidden by brace/table angle in this frame — fine; will be rendered explicitly in downstream scene prompts where hands are visible)
- ✅ Chin scar present
- ✅ Pale-blue scrubs under open beige zip-up jacket
- ✅ Neat low bun at nape
- ✅ Mixed white-Latina features, reads age 38 (not 28, not 48)
- ✅ Composed clinical-competent register — not crying, not pained, not seeking sympathy

---

## Why this candidate over the alternates

- **Strongest specific-person read** — clearly 38, mixed Latina specificity clean, NOT a generic working-class composite
- **Cleanest brace placement** — both Velcro straps visible, sits naturally on the wooden surface
- **Background dimensional depth** — kitchen softly suggested behind, gives downstream scene re-lighting more material to work with than a flat seamless background
- **Vermeer-quality directional falloff** from camera-right (window edge implied) — neutral enough to re-light into S1's warm kitchen beats AND cool boardroom beats
- **Eyes carry quiet clinical competence** — looks like she's about to give you an assessment, exact "she is the one others lean on" register from `Audience/Deep_Personas/Sarah/02_Emotional_Architecture.md`

## Rejected candidates (4 alternates)

1. **Image 2** (`hf_20260425_033033_4d7ebc61`) — strong second pick, slightly cooler mood, more world-weary read. Saved as fallback option but not locked. Cooler light may fight warm-scene re-lighting.
2. **Image 3** (`hf_20260425_032442_79d12fa9`) — too warm/soft, slight smile-edge undermines clinical composure. Body angle too far off-axis.
3. **Image 4** (`hf_20260425_030116_ee90cdf7`) — face reads younger (~32), wispy loose hair fights the "neat low bun" spec, too vulnerable for character lock.
4. **Image 1** (`hf_20260425_032442_a14a72ab`) — brace position obscures wedding band hand, cool blue-gray cast risks fighting warm-scene re-lighting, eyes feel distant. Most generic of the five.

---

## Downstream re-lightability notes

Reference is intentionally lit on the **slightly cool/neutral** side of the spec — this is correct. Per Phase 1 doc downstream-viability rule (Indigo): references must accept re-lighting into any scene context. Sarah's downstream scenes:

- **S1 Primary kitchen-table beats** — warm 5pm golden-hour window (kitchen lamp + dusk ambient outside)
- **S1 Primary boardroom-at-night beat** — cool corporate fluorescent
- **S1 Primary I-17 dusk wide** — Sarah not in this beat, but reference must accept her appearing in adjacent cuts
- **S1-V2** — late-night kitchen + boardroom-at-night cool fluorescent
- **S1-V3** — phone-camera UGC register (flat phone color, deep focus, auto-WB)
- **S1-V5** — evidence-led; Sarah appears only in final composed kitchen frame

Slight desaturation of locked reference is a feature — directional Vermeer light gives re-lighters something to work with; neutral grade lets each scene's light spec override cleanly.

---

## Generation prompt (verbatim)

```
A documentary photorealistic waist-up portrait of a specific middle-aged American woman, indistinguishable from a real digital camera photograph. Shot in the quiet naturalism of Paul Thomas Anderson's Phantom Thread interiors — a single large north-facing window as the only key light, positioned camera-right close to the frame with the window edge faintly visible at the right edge of the image, diffused warm afternoon light producing soft directional falloff across the face from bright camera-right to gently shadowed camera-left. Painterly Vermeer-quality natural interior light with warm afternoon tone. No three-point cinema setup, no soft-box glamour, no bounce fill — one window doing all the work.

Reference aesthetic: Alec Soth portraits of American working and middle-class subjects for the honest dignity, Nadav Kander portrait compositional rigor for the still weight. Every light source is one you could point to in the room (David Fincher's Mindhunter discipline on motivated-light-only).

Capture format: Fujifilm X-T5 or Sony A7R IV digital look, 50mm prime lens, f/2.8. Subtle-to-moderate 35mm Kodak Vision3-adjacent film grain, honest skin saturation, no HDR, no over-sharpening, no airbrushing. Skin texture must show pores, fine lines, subtle asymmetry — her face is not symmetrical. Eyes show a single soft catchlight from the window.

Focus plane: eyes sharp at f/2.8, ears already softening, background out-of-focus but legibly dimensional.

Framing: waist-up, seated at a simple wooden surface or table with body turned just slightly to camera-left at about fifteen to twenty degrees off-axis, head turned fully to camera, eyes looking DIRECTLY to camera with quiet present awareness — not off-camera, not averted, direct gaze. Subject inhabits the frame completely — composed, present, still. Neutral soft warm-grey or cream out-of-focus background with gentle depth, window edge suggesting at right edge of frame. Composition rule-of-thirds with eyes on upper third. Aspect ratio 3:4.

Blocking: seated at a simple wooden surface, both forearms resting gently on the surface in front of her, her LEFT forearm (with the black canvas brace) resting on the surface with the brace clearly visible and closest to the camera (on viewer's RIGHT side of the frame), her RIGHT hand resting over or beside her left wrist. Weight composed (not slumped, not braced, not leaned forward). Mouth closed or relaxed (no mid-word speech shape). Micro-movement only.

Subject: Sarah, 38, mixed white-Latina — reads clearly as Arizona-native Latina features with softer warmer undertones, a specific woman not a generic composite, 5'6", athletic-but-soft build of a working ICU nurse. Dark-brown hair pulled back into a NEAT LOW BUN at the nape of her neck with a few wispy pieces loose at the temples and at the nape — a practical hospital-ready bun, NOT a ponytail, NOT worn down, a proper low bun. Minimal makeup, small stud earrings, no watch. Warm hazel or warm brown eyes with quiet present awareness and faint fatigue in the undereye area — she has been running on four hours of sleep for months but she is fully here in this moment. A small scar on her chin from childhood. Pale-blue hospital scrubs visible under an open beige or tan zip-up jacket.

Injury / continuity prop: a soft BLACK canvas arm brace with Velcro straps worn on her LEFT forearm (Sarah's own left arm, which on a camera-facing portrait appears on the viewer's RIGHT side of the frame). The brace must be clearly visible, resting on the wooden surface in front of her. Her LEFT hand rests on the surface, showing a thin white-gold wedding band.

Emotional register: the woman who absorbs other people's crises for a living, now quietly absorbing her own. Present, composed, calmly returning the viewer's gaze — not performing, not asking for sympathy, not defeated. A nurse sitting at the end of a long week, looking you in the eye because she is the one who looks people in the eye. Quiet competence. Faint fatigue in the eyes and the set of the jaw, but composed — she is still the one others lean on.

Critical side-specific detail to lock: the black canvas arm brace is on Sarah's OWN LEFT forearm, resting on the surface in front of her closest to camera (viewer's RIGHT side of frame). Do not flip it to her right. The wedding band is on her LEFT hand, same arm as the brace. Do not flip it.

Do NOT generate: nurse stereotype (no stethoscope around neck, no clipboard, no scrub cap, no hospital hallway setting), no glamour lighting, no heavy makeup, no youthful model face — she is 38 and she has lived. No smiling, no pained expression, no hair worn down, no ponytail — only a proper low bun.

Do NOT generate any AI tells: no waxy or plastic skin, no symmetrical faces, no uncanny eyes, no extra or malformed fingers, no floating hair, no distorted hands, no over-saturated color, no HDR look, no over-sharpened edges, no airbrushed finish, no text in image, no watermark.
```

---

## Notes for downstream scene prompts

- **Wedding band** — not visible in this reference frame (hidden by brace/table angle). Add explicitly in scene prompts where hands are visible: *"thin white-gold wedding band on her left ring finger visible."*
- **L-temple fading bruise** — not visible in this reference (hair coverage). Per S1 brief, the L-temple bruise is also a continuity prop. Add explicitly in scene prompts: *"a faint yellowing fading bruise visible on her LEFT temple, healing not fresh, pale yellow-green tone."*
- **Hair stays in the low bun** for all S1 Elevated scenes (her clinical-competent register). UGC-Native S1-V3 may relax to a looser bun or partial down depending on home-context blocking.
- **Wardrobe in S1 scenes:** scrubs under zip-up holds across all variants per wardrobe rule.

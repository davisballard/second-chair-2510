# S5 Diana — Operator Motion Pass

**Date:** 2026-04-25
**Author:** Giuseppe Karma (AI Creative Director)
**Supersedes:** the camera-locked v1 hangup prompt
**Target models:** Kling 3.0 Pro (primary) / Seedance 2.0 (alternate)
**Anchored to:** `Style_Sheets/UGC_Native.md` §0 (no on-camera dialogue), §2 (image block), §3 (video block), §6 (motion discipline), §6.5 (failure flags)

---

## Diagnosis — why v1 is flat

The v1 hangup prompt locks the camera:

> *"Camera locked with subtle natural handheld micro-wobble. NO push-in, NO zoom, NO pan, NO orbit. Phone-camera deep focus, NO bokeh, NO film grain, NO cinematic motion. Lighting holds."*

This is the AI-faking-UGC failure mode. It produces a tripod-with-jitter. Real UGC isn't tripod — it's a **person holding a phone with a hand**. The hand moves WITH the moment because Ben's eyes move, his weight shifts, his wrist rotates when something happens.

The §6 motion-discipline rule "NO push-ins, NO dollies, NO whip pans, NO cinematic motion grammar" is correct — that bans **cinematic** motion. But the v1 prompt over-corrected and banned **all** motion, which is also wrong.

**The taxonomy that fixes it:**

| Cinematic motion (FORBIDDEN — §6 holds) | Operator motion (ENCOURAGED — this is the fix) |
|---|---|
| Smooth choreographed dolly | Ben takes a half-step closer; perspective compresses unevenly |
| Choreographed pan to a subject | Ben's eye flicks to where Diana looks, camera follows half a beat late |
| Smooth tilt down to action | Ben's wrist drops because Diana's hand drops; arrival is uneven, not eased |
| Whip pan / kinetic edit feel | Reframe-punctuation: small grip-adjust mid-clip, frame shifts 3–6 inches |
| Rack focus / shallow DOF | Deep focus throughout (phone sensors can't rack focus anyway) |
| Slow motion | Real-time, with ambient phone-mic sound |
| Crane / jib / orbit | Parallax-shift only (Ben's weight moves, not a track) |

**The mental model:** Ben is filming his wife on his iPhone with one hand while standing across the kitchen island with a coffee in the other. He's not a tripod. He's not a director. He's a husband with a phone whose hand reacts to what he sees.

---

## Operator-motion vocabulary (paste-in)

Replace v1's "Camera locked... NO push-in, NO zoom, NO pan, NO orbit... NO cinematic motion. Lighting holds" with this block. **This is the fix.** Tune the rung intensity per shot.

```
Camera: Ben-the-operator handheld phone camera, ~28mm phone-wide
equivalent, deep focus throughout. The camera is a hand, not a
tripod — it reacts to what he sees, half a beat late, never on
a beat. Operator motion is ENCOURAGED — frame-shift from grip
adjust, weight-shift parallax, eye-line follow, micro-pivot to
keep the action in frame. Cinematic motion is FORBIDDEN — no
smooth choreographed dolly, no eased pan, no rack focus, no
slow-motion, no whip pan, no crane, no orbit. Movement reads
as "Ben actually filming his wife," NOT as "shot."

Permitted operator gestures:
- Grip-adjust reframe: frame shifts 3–6 inches mid-clip as if
  Ben's wrist tightens or loosens; uneven, not eased.
- Eye-line follow: when Diana's eyes flick down to her hand,
  the camera tilts down half a beat LATE, not synchronized;
  arrival is slightly past the action, not anticipating it.
- Parallax shift: Ben's weight moves; foreground and background
  shift at different rates because his eye-line lowered or
  raised an inch or two. No smooth dolly path.
- Half-step / quarter-step: Ben may shift his stance once per
  clip — knees bend, hips rotate, perspective compresses
  unevenly. NOT a dolly track.
- Reframe-punctuation: between the camera's reactions, small
  grip drift continues — never tripod-still.

Phone-sensor optics throughout: deep focus (no bokeh),
auto-exposure (not motivated lighting), flat phone color (no
grade), no film grain, no cinematic LUT. Auto-WB. Ambient
domestic sound feel.
```

---

## Three energy ladder rungs — the recorded-statement hangup beat

Same beat as v1, three intensities. Generate Rung 2 first; if too tame, climb to Rung 3; if too active, drop to Rung 1.

**Beat:** ~4 seconds. Diana stands at the kitchen island holding her phone to her left ear with her LEFT hand. Right arm in sling. She listens with eyes downcast, mouth closed. Around 2s she lowers the phone in front of her chest, screen facing her, and her LEFT thumb taps the red end-call button. By 4s the call is ended — she lowers the phone toward the island with a slow exhale. She does not speak. She does not look at camera.

---

### RUNG 1 — Ben holds, breathes, adjusts (mild)

*Use when the editorial cut needs a quiet face-hold beat with minimum visual energy. This is the closest cousin to v1, but actually moves.*

```
[PASTE §0 SC NO-DIALOGUE BLOCK — UGC_Native.md §0]

[PASTE §3 VIDEO INJECTION BLOCK — UGC_Native.md §3]

[PASTE OPERATOR-MOTION VOCABULARY BLOCK — see above]

Scene: Diana at her own kitchen island, mid-morning, natural
window daylight from camera-right. Filmed by her husband Ben
from across the island with one hand on his iPhone. Diana wears
her pale buttery yellow cardigan over a plain white t-shirt,
shoulder-length light-brown hair in a loose low ponytail with
face-framing pieces loose at the temples, reading glasses pushed
up into her hair above the forehead. Black fabric arm sling
cradling her OWN RIGHT arm (viewer's LEFT side of frame), strap
diagonal LEFT shoulder to RIGHT hip. Faint yellowing healing
bruise visible along her RIGHT jawline. Small mole above her
LEFT upper lip. Wedding band on LEFT ring finger.

Action (~4 seconds, real-time): Diana stands holding her iPhone
to her LEFT ear with her LEFT hand. Eyes downcast, mouth closed,
listening — NOT speaking. At 2.0s she lowers the phone away
from her ear with her LEFT hand, bringing it down in front of
her chest with the screen facing her. Her LEFT thumb taps the
red end-call button on the iPhone screen. By 4.0s the call is
ended — she lowers the phone toward the kitchen island surface
with a slow exhale. RIGHT arm stays in sling throughout. She
does not speak, does not look at camera.

Camera (Rung 1 — mild): waist-up framing, Diana positioned
camera-left of center. Ben's hand holds steady but breathes —
small grip drift throughout, never tripod-still. At 2.0s when
Diana's hand drops, Ben's wrist drifts down maybe 3 inches,
half a beat late, NOT synchronized — uneven, not eased. One
small grip-adjust reframe at 3.0s, frame shifts ~4 inches
camera-right. Deep focus throughout. NO smooth dolly, NO
choreographed pan, NO rack focus.

Lighting: window daylight from camera-right, slight warm bias,
auto-WB. Fills shadow naturally. Phone-camera fill behavior, no
deep shadow falloff.

Audio (diegetic, in-frame): faint ambient kitchen room tone,
distant refrigerator hum, the small click of the end-call tap,
Diana's quiet exhale at 4.0s. NO music inside the clip (added
in CapCut post). NO dialogue from Diana.

[PASTE §8 NEGATIVE PROMPT BLOCK — UGC_Native.md §8]
```

---

### RUNG 2 — Ben follows the action (medium) — RECOMMENDED FIRST GENERATION

*Sweet spot for the recorded-statement beat. The camera tracks Diana's eye-line and hand, half a beat late, with operator-driven tilt-down then tilt-back-up.*

```
[PASTE §0 SC NO-DIALOGUE BLOCK — UGC_Native.md §0]

[PASTE §3 VIDEO INJECTION BLOCK — UGC_Native.md §3]

[PASTE OPERATOR-MOTION VOCABULARY BLOCK — see above]

Scene: Diana at her own kitchen island, mid-morning, natural
window daylight from camera-right. Filmed by her husband Ben
from across the island with one hand on his iPhone. Diana wears
her pale buttery yellow cardigan over a plain white t-shirt,
shoulder-length light-brown hair in a loose low ponytail with
face-framing pieces loose at the temples, reading glasses pushed
up into her hair above the forehead. Black fabric arm sling
cradling her OWN RIGHT arm (viewer's LEFT side of frame), strap
diagonal LEFT shoulder to RIGHT hip. Faint yellowing healing
bruise visible along her RIGHT jawline. Small mole above her
LEFT upper lip. Wedding band on LEFT ring finger.

Action (~4 seconds, real-time): Diana stands holding her iPhone
to her LEFT ear with her LEFT hand. Eyes downcast, mouth closed,
listening — NOT speaking. At 1.5s her eyes flick down toward
her left hand — anticipating the move. At 2.0s she lowers the
phone away from her ear with her LEFT hand, bringing it down
in front of her chest with the screen facing her. Her LEFT
thumb taps the red end-call button on the iPhone screen at
~2.7s. By 3.5s the call is ended; by 4.0s she lowers the phone
toward the kitchen island surface with a slow exhale. RIGHT arm
stays in sling throughout. She does not speak, does not look
at camera.

Camera (Rung 2 — medium): open chest-up framing, Diana
positioned slightly camera-left. At 1.5s Diana's eyes flick
down — Ben's camera follows half a beat late at ~1.8s, tilting
down operator-style (uneven, not eased) to widen and include
the phone screen in frame as her hand brings it to chest level
by 2.0s. Frame now waist-up — phone screen visible, red
end-call button readable, LEFT thumb hovering then tapping.
At 3.5s as Diana exhales and lowers the phone, Ben's camera
tilts back UP to chest-up framing — again half a beat late,
operator-driven. Two grip-adjust reframes punctuate the moves
(one at 1.0s, one at 3.0s) — frame shifts 3–5 inches each.
Deep focus throughout. NO smooth dolly, NO choreographed pan,
NO rack focus.

Lighting: window daylight from camera-right, slight warm bias,
auto-WB. Fills shadow naturally. Phone-camera fill behavior, no
deep shadow falloff.

Audio (diegetic, in-frame): faint ambient kitchen room tone,
distant refrigerator hum, the small click of the end-call tap
at ~2.7s, Diana's quiet exhale at 4.0s. NO music inside the
clip (added in CapCut post). NO dialogue from Diana.

[PASTE §8 NEGATIVE PROMPT BLOCK — UGC_Native.md §8]
```

---

### RUNG 3 — Ben moves with the moment (alive)

*Highest energy. Use if Rung 2 reads as still-tripoddy. Ben shifts stance once per clip; weight-shift parallax + eye-line follow + grip-adjust all stack.*

```
[PASTE §0 SC NO-DIALOGUE BLOCK — UGC_Native.md §0]

[PASTE §3 VIDEO INJECTION BLOCK — UGC_Native.md §3]

[PASTE OPERATOR-MOTION VOCABULARY BLOCK — see above]

Scene: Diana at her own kitchen island, mid-morning, natural
window daylight from camera-right. Filmed by her husband Ben
from across the island with one hand on his iPhone. Diana wears
her pale buttery yellow cardigan over a plain white t-shirt,
shoulder-length light-brown hair in a loose low ponytail with
face-framing pieces loose at the temples, reading glasses pushed
up into her hair above the forehead. Black fabric arm sling
cradling her OWN RIGHT arm (viewer's LEFT side of frame), strap
diagonal LEFT shoulder to RIGHT hip. Faint yellowing healing
bruise visible along her RIGHT jawline. Small mole above her
LEFT upper lip. Wedding band on LEFT ring finger.

Action (~4 seconds, real-time): Diana stands holding her iPhone
to her LEFT ear with her LEFT hand. Eyes downcast, mouth closed,
listening — NOT speaking. At 1.5s her eyes flick down toward
her left hand. At 2.0s she lowers the phone away from her ear
with her LEFT hand, bringing it down in front of her chest with
the screen facing her. Her LEFT thumb taps the red end-call
button on the iPhone screen at ~2.7s. By 3.5s the call is
ended; by 4.0s she lowers the phone toward the kitchen island
surface with a slow exhale. RIGHT arm stays in sling throughout.
She does not speak, does not look at camera.

Camera (Rung 3 — alive): open chest-up framing, Diana
positioned slightly camera-left. At 0.5s Ben takes a quarter-step
forward — knees bend, eye-line lowers an inch or two, parallax
shift on the kitchen cabinetry behind Diana (background slides
laterally a hair against her shoulder line). NOT a dolly path,
NOT smooth — uneven weight transfer. At 1.5s eye-line follow:
Ben's camera tracks Diana's downcast glance toward her LEFT
hand, half a beat late, tilting down operator-style. At 2.0s
the phone is mid-frame; Ben pivots his torso ~3 degrees
camera-right to keep both Diana's hand and her face in frame
as her arm extends. At 2.7s grip-adjust reframe — frame shifts
4 inches. At 3.5s Ben rocks back onto his heels — small
quarter-step retreat as Diana exhales — frame opens slightly
back to chest-up, kitchen island surface re-enters lower frame.
Deep focus throughout. NO smooth dolly, NO choreographed pan,
NO rack focus.

Lighting: window daylight from camera-right, slight warm bias,
auto-WB. Auto-exposure may shift a hair as Ben's stance changes
the angle to the window — that drift is permitted, even
welcome. Phone-camera fill behavior, no deep shadow falloff.

Audio (diegetic, in-frame): faint ambient kitchen room tone,
distant refrigerator hum, the small click of the end-call tap
at ~2.7s, Diana's quiet exhale at 4.0s, faint scuff of Ben's
foot on the kitchen floor as he shifts stance (optional —
remove if it reads distracting). NO music inside the clip
(added in CapCut post). NO dialogue from Diana.

[PASTE §8 NEGATIVE PROMPT BLOCK — UGC_Native.md §8]
```

---

## Failure-mode flags specific to operator-motion prompts

Add to the §6.5 failure-mode scan when reviewing output:

| Failure | Why it fails | Fix |
|---|---|---|
| **Camera moves on the beat / synchronized to action** | Ben's hand isn't a Steadicam — he reacts late, not on time | Reinforce "half a beat late, NOT synchronized" in prompt |
| **Smooth eased tilt-down** | Reads as cinematic dolly grammar | Reinforce "uneven, not eased; arrival is past the action, not anticipating it" |
| **Camera moves but Diana doesn't** | Operator-motion needs a REASON — Ben follows what HE sees | Keep eye-line / hand-action / weight-shift triggers explicit in prompt |
| **Background slides smoothly during a "step"** | That's a dolly track, not a half-step | Reinforce "parallax shift, NOT a dolly path; foreground and background shift at different rates" |
| **Frame perfectly still between motions** | Tripod-with-jitter failure mode returns | Reinforce "grip drift continues between reactions, never tripod-still" |

---

## Open-on-Diana beat (separate generation — Rung 2 default)

The hangup beat above is the recorded-statement / Peak Card moment (~6.5–10.5s of the spot). The opening beat (0–3s, "Broken bones. Bills don't stop." Hook Card) is its own generation. Same operator-motion vocabulary, different action and triggering events. Sketch:

- **Action:** Diana at the kitchen island, RIGHT arm in sling, sorting through a small stack of envelopes on the counter with her LEFT hand. She picks up an envelope, glances at the return address (insurance carrier, generic), sets it back down. Eyes downcast, mouth closed.
- **Camera (Rung 2):** waist-up open framing. At 1.0s Ben's camera tilts down half a beat late as Diana picks up the envelope — including the envelope and her LEFT hand in frame. At 2.0s tilts back up to chest-up as she sets it down. Grip-adjust reframe at 0.5s and 2.5s.
- **Why this opens cleanly into the hangup beat:** the envelope sets up "bills don't stop"; the phone-to-ear handoff (call rings at ~3.5s? or hard cut at 3.0s to phone-already-up?) is the Hook → Problem pivot.

When you want this beat, generate it as a separate prompt — same operator-motion block, same character lock, swap the Action and Camera paragraphs.

---

## Iteration log

*Paste seed + thumbnail observation here as you generate.*

```
### [Date] — [Rung] — [Beat]
**Kling seed:** [from UI]
**Full prompt used:** [paste verbatim]
**Output verdict:** [worked / too still / too cinematic / off-beat]
**Tune for next gen:** [specific edit to the operator-motion block]
```

---

## Cross-references

- `Style_Sheets/UGC_Native.md` §6 (motion discipline — the rule this v2 refines, NOT replaces)
- `Style_Sheets/UGC_Native.md` §6.5 (failure flags — extend with operator-motion flags above)
- `04_Production/Giuseppe_Karma_(AI_Creative_Director)/Prompting_Guides/Kling_3.md` §6 (camera vocabulary Kling 3.0 understands)
- `04_Production/Giuseppe_Karma_(AI_Creative_Director)/Prompting_Guides/Seedance_2.md` §6 (Seedance camera taxonomy — Handheld vs Fixed distinction)
- `Reference_Portraits/diana_reference_lock.md` (character lock — DO NOT re-describe; the ref image carries the face)
- `Renders/S5_Diana_MVA/Primary/overlay_spec.md` (Hook + Peak + CTA timing the video must serve)

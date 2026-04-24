# Style Sheet — Elevated Documentary (Luca Maxim × WCTL)
## Second Chair × West Coast Trial Lawyers — Arizona Pilot

**Prepared:** 2026-04-22
**Anchored to:** `Abracadabra/04_Production/Giuseppe_Karma_(AI_Creative_Director)/Influencer_Styles/Luca_Maxim_Style.md`
**Adapted for:** WCTL empathy-driven PI context (Barry Hott's theatrical emotion-dial explicitly rejected — see §6 Motion Discipline)
**Status:** v1 — living document. Paste working prompts into §9 and observations into §10 as you iterate.

---

## 0. CRITICAL SC DISCIPLINE — TWO LOAD-BEARING RULES

### 0.1 SC is short-form: extract VISUAL register from directors, not dialogue/temporal grammar

Second Chair ads are **10-20 seconds**. The directors named in §2a (Mindhunter / Tarantino / Villeneuve / Fincher / Coens / etc.) work in 90-200 minute runtimes. Their dialogue rhythm, long-take patience, and two-shots-held-for-minutes are scaled to feature-length — **none of that translates temporally to SC**.

From every director anchor, extract ONLY the visual register:
- **Light** (source, quality, direction, temperature, fall-off)
- **Color** (palette, grade, emotional register)
- **Composition** (framing, symmetry, negative space, focus plane)
- **Blocking-as-stillness** (pose, body language, eye-line, micro-movement)
- **Lens / camera / format** (focal length, grain, sensor / stock)
- **Prop specificity & Americana texture** (the objects, the era-accurate environment)
- **Emotional register** (identity / loss / injustice / grief / dignity)

**Do NOT extract temporal/dialogue grammar:**
- "Hold for the rhythm of a conversation"
- "Sustained dialogue-patience"
- "Long-take shared silence"
- "Two-shot held for the time a conversation would take"

A 10-second SC frame can FEEL like Mindhunter (institutional cool + single warm practical + 50mm locked + eye-line off-camera) without carrying the time-budget of a Mindhunter interview scene. The visual world transfers; the temporal grammar does not. If a draft prompt tries to encode long-take or conversation-rhythm language, strip it.

### 0.2 AI subjects do NOT speak on camera

Every SC ad is voiceover-narrated. AI-generated characters are THINKING, not SPEAKING. Project-level rule, applies to every prompt.

**Prompt-level enforcement (must appear in every Elevated image AND video prompt):**

```
SUBJECT DOES NOT SPEAK ON CAMERA. Mouth closed or slightly open
in natural breath only — NO lip movement, NO dialogue delivery,
NO mouthing words, NO mid-word speech shape, NO "talking head"
pose. The character is thinking, not speaking. Voiceover narration
is generated via ElevenLabs TTS in post (Ennio Morricone's
VO_Direction_Playbook — Bill voice primary), NOT delivered by
the AI subject. No dialogue from the subject, no spoken lines
inside the generated clip.
```

**Exception — requires Davis authorization per asset:** a specific SC asset may authorize one on-camera line (rare testimony moment). Never default to it.

### Failure flags (regenerate if present)

- Subject's mouth in mid-word / speech shape / "talking head" pose
- Eye-line direct to camera in authoritative "testimony" pose (chin-up, addressing viewer)
- Any prompt language about dialogue-rhythm, conversation-patience, long-take pacing, two-shot-held-for-minutes — strip it; SC time budget doesn't carry any of it.

---

## 1. Purpose & how to use

This style sheet is the source of truth for the **Elevated Documentary** treatment used on 5 of the 6 Phase 1 WCTL assets (M1, M2, M3, S1, S2 + the Ty Rivera / Sarah / Laura reference portraits). *Motorcycle persona renamed 2026-04-22 from Marco Reyes (cruiser archetype, archived) → Ty Rivera (supersport archetype, 29-yo Yamaha R6 rider). All M1/M2/M3 references below now refer to Ty, not Marco.*

**Workflow per generation:**

1. **Still image in Higgsfield (ChatGPT Images 2.0):** copy the §2 Image Injection Block into the top of your prompt. Then append the character brief + scene spec + side-specific detail reminders.
2. **Video animation in Kling 3.0 Pro / O1 or Seedance 2.0:** upload the locked reference still as the character image. Copy the §3 Video Injection Block. Append the scene's motion description (from `Creative/Week_1_Approval_Package/` — current canonical; `Archive/Week_1_Launch_Concepts_2026-04-21.md` is archive-only). Generate. See `Abracadabra/04_Production/Giuseppe_Karma_(AI_Creative_Director)/Prompting_Guides/Kling_3.md` and `Seedance_2.md` for full model-specific prompting references.
3. **After generation:** if the output worked, paste the full prompt + Higgsfield/Kling seed into §9 Examples That Worked so v2 of this sheet can absorb what's landing.

---

## 2. Image Injection Block — ChatGPT Images 2.0 (Higgsfield)

**Upgraded 2026-04-23** to director-anchored language. The older block is preserved at §2.5 as fallback; prefer the anchored block below.

### 2a. Director Anchor — which director(s) for which concept

Every prompt generated from this style sheet names AT LEAST ONE director anchor. See `Abracadabra/04_Production/Giuseppe_Karma_(AI_Creative_Director)/Director_Reference_Library/` for profiles.

| Concept | Emotional register | Primary anchor | Secondary anchor |
|---------|-------------------|----------------|------------------|
| **M1 Identity** (Ty garage) | Identity / intact / pre-event warmth | Coens/Fargo + PTA | Fargo TV (Hawley) for domestic ritual |
| **M2 Loss** (Ty kitchen) | Grief / weight / institutional cool | Mindhunter | Villeneuve (Prisoners) |
| **M3 Injustice** (Ty intersection dusk) | Question-without-answer / ambiguity | Lynch dusk | Villeneuve blue-hour + True Detective S1 sodium vapor |
| **S1 Trucking** (Sarah I-10 + kitchen) | Identity → corporate cold contrast | Sopranos domestic + Mindhunter corporate | Breaking Bad desert-sun for I-10 exterior |
| **S2 Pedestrian** (Laura crosswalk) | Suburban quiet / landscape-as-memory | Coens/Fargo + Sopranos | True Detective S1 for atmosphere |
| **Reference portraits (neutral)** | Character at rest, dignified | PTA portrait grammar + Mindhunter single-source light | (single anchor usually enough) |

### 2b. Image Injection Block — DIRECTOR-ANCHORED (paste verbatim at top of every Elevated image prompt)

```
Director anchor: [PICK FROM §2a — e.g., "Mindhunter dialogue-scene
grammar combined with Villeneuve's Prisoners grief-weight"].

Motivated single-source light — [NAME THE SOURCE: kitchen pendant
/ single bedside lamp / window-daylight from camera-left / garage
worklight / amber streetlight]. Deep shadow fall-off on opposite
side of subject's face; shadow side allowed to go to deep charcoal,
not pure black. NO bounce fill, NO three-point cinema lighting,
NO soft flattering studio light. Every light in the frame has a
pointable source in the room.

Color register: [PICK FROM §5 Color Arc — warm amber identity /
cool institutional green-cyan loss / dusk ambiguity / corporate
cold]. Desaturated skin pulled slightly cool or warm per register;
honest skin texture with pores, fine lines, subtle asymmetry;
hair has flyaways; eyes show catchlight.

Focus as directorial claim: shallow DOF at f/2.8, eyes sharp and
ears already softening, [NAME THE BLUR PLANE — e.g., "bike visible
but blurred in peripheral foreground as implied-absence" / "bills
in stacked foreground, sharp to blurred across stack" / "window
behind subject soft to draw attention to face"].

Capture format: Fujifilm X-T5 or Sony A7R IV digital look, 50mm
prime for dialogue / 27-35mm for environment, 35mm Kodak Vision3
film grain subtle-to-moderate, 2.20:1 or 2.39:1 aspect ratio
(crop to 4:5 for portraits, 9:16 for video-ready stills).

Blocking: subject still — placed not posed, hands at sides or on
table or holding a single object, micro-movement only (blink,
breath, slight lean), eye-line precisely [12 degrees off-camera
to implied listener / middle-distance unfocused / downward inward
contemplation], the stillness itself is the performance.

Negative space: [NAME THE ABSENCE — the empty motorcycle parking
spot / the unused second coffee cup / the passenger seat without
passenger / the place at the table no one sets anymore]. The
absence is in the frame.

Documentary seriousness — empathy-driven, quiet emotional weight,
"still eye of the storm" protagonist. Indistinguishable from real
digital camera footage. NO AI tells: no waxy skin, no symmetrical
face, no plastic finish, no over-sharpened edges, no HDR look,
no over-saturated color, no glowing skin, no airbrushed quality,
no text in image.
```

### 2c. How to use this block

1. **Pick the concept** from §2a. Note the director anchor(s).
2. **Load the anchor's profile** from `Director_Reference_Library/` — lift specific phrases from its Prompt Vocabulary section.
3. **Fill the bracketed slots** in the injection block above. Never leave a bracket un-filled; that's the failure mode.
4. **Append** the character brief + scene spec + side-specific detail reminders after this block.
5. **Scan for failure flags** (§6.5 below) before submitting.

### 2.5 — Legacy Image Injection Block (fallback only)

```
Cinematic color grading — desaturated with lifted blacks,
subtle film grain, shallow depth of field,
motivated natural lighting, hyperrealistic detail,
Roger Deakins atmospheric quality.
Documentary seriousness, not theatrical — empathy-driven,
quiet emotional weight, "still eye of the storm" protagonist.
Indistinguishable from real digital camera footage
(Fujifilm X-T5 or Sony A7R IV look, 50mm prime lens, f/2.8).
Skin texture shows pores, fine lines, subtle asymmetry.
Hair has flyaways. Eyes show catchlight. No AI tells —
no waxy skin, no symmetrical face, no plastic finish,
no over-sharpened edges, no HDR look, no over-saturated color,
no glowing skin, no airbrushed quality, no text in image.
```

This legacy block works but lacks director anchor, color register selection, focus specification, blocking detail, and negative space. Use the director-anchored block above by default; fall back to this only if the anchored block cannot be completed for some reason.

---

## 3. Video Injection Block — Kling 3.0 Pro / O1 or Seedance 2.0

**Upgraded 2026-04-23** to director-anchored language with diegetic audio prompting and blocking/pacing specification. Legacy block preserved at §3.5.

### 3a. Video Injection Block — DIRECTOR-ANCHORED

Copy the block between the fences verbatim and paste at the top of every Elevated video prompt. Kling and Seedance accept similar natural-language motion grammar — same block works for both.

```
Director anchor: [PICK FROM §2a — same director selection as the
Image Injection Block; the video carries the still's grammar
into motion.]

Camera movement: [CHOOSE ONE:
 - "Camera locked, no movement. Shot observes; does not push."
   (default — Mindhunter, Villeneuve, Sopranos, BCS)
 - "Imperceptible slow dolly push-in across the clip, 3-4 feet
   total. Used ONCE per asset maximum — typically the turn-of-
   the-line moment." (Mindhunter / PTA / Villeneuve monologue)
 - "Slow tracking alongside walking subject at exact walking
   pace, no acceleration, no handheld shake." (Fargo TV, BB
   domestic) ]

Subject blocking: still — placed not posed, hands at sides or
on table or holding a single object. Micro-movement only —
a blink, a slow exhale, a slight shift in weight, a finger tap,
a small specific gesture (pouring coffee, opening mail, setting
down a mug) performed once, not repeated. Eye-line precisely
[12 degrees off-camera to implied listener / middle-distance
unfocused / downward inward contemplation]. Body physically
[burdened — shoulders forward, head lowered / composed — weight
balanced]. The stillness is the performance. NO theatrical
action, NO slamming, NO exaggerated gestures, NO cackling.

Environment carries the motion: [PICK 1-3 SPECIFIC ENVIRONMENTAL
MOTIONS — "mail falling onto counter / coffee dripping once every
4 seconds / clock ticking / a door closing in adjacent room /
fabric shifting / wind through open window / dust moving across
floor in shaft of sunlight"]. The weight of time passing, rendered
through environment not through subject.

Negative space / implied-absence: [FROM §5d — the empty bike
spot / the unused second coffee cup / etc.]. The absence is
visible in the frame's composition.

Color register: [FROM §5 Color Arc — warm amber identity / cool
institutional loss / dusk ambiguity / corporate cold]. Grade
locked to register. Subtle film grain preserved. Shallow depth
of field maintained at the focus plane from §5c.

Audio register (Kling 3.0 / Seedance 2.0 co-gen): diegetic only.
Ambient — [NAME THE ROOM TONE: "refrigerator hum + clock ticking
once per second + distant highway through closed window" /
"HVAC at low volume + distant dog barking + clock" / etc.].
Foley — [NAME 2-3 SPECIFIC FOLEY MOMENTS: "coffee dripping once
every 4 seconds, subject's slow exhale once, envelope set on
counter"]. NO voiceover (added in post). NO music (added in
post). NO dialogue unless explicitly scripted. Silence between
the Foley moments is intentional — the silence carries the weight.

Character consistency: face / wardrobe / side-specific props
(scar, brace, cane, sling, bruise) consistent with uploaded
reference image — same face, same wardrobe, same sides.
```

### 3b. How to use

1. Pick same director anchor as the image block.
2. Choose camera movement option from bracket.
3. Specify subject blocking — don't let the model default to generic "natural motion."
4. Name 1-3 environmental motions that carry the scene's pacing.
5. Specify the implied-absence per §5d.
6. Lock color register per §5.
7. Specify diegetic audio per `../../../../../04_Production/Giuseppe_Karma_(AI_Creative_Director)/Audio_Prompting.md` — ambient, Foley, silence. No music or VO.
8. Reinforce character consistency.

### 3.5 Legacy Video Injection Block (fallback only)

```
Cinematic motion grammar — subtle slow push-in OR static hold
with gentle handheld micro-movement. Natural timing.
No snap cuts. No whip pans. No dramatic orbits.
Protagonist remains composed — the "still eye of the storm."
The environment carries the motion: mail falling, coffee cooling,
timer ticking, a door closing in the distance, fabric shifting,
the weight of time passing. No theatrical action,
no slamming, no exaggerated gestures, no cackling.
Color grade locked — desaturated with lifted blacks.
Subtle film grain preserved. Shallow depth of field maintained.
Character face consistent with the uploaded reference image —
same face, same wardrobe, same side-specific props
(scar, brace, cane, sling, bruise) as the reference.
```

Works but lacks director anchor, audio specification, focus-plane detail. Use the director-anchored block above by default.

---

## 4. Composition Rules

Shot types adapted from Luca Maxim's 12-shot library (`Luca_Maxim_Style.md` §405+) that fit WCTL. Pick the shot type per scene; do not mix more than 3 shot types in one ad.

**Used in WCTL:**

| Shot Type | When | WCTL Scenes |
|-----------|------|-------------|
| **Hero Medium Shot** | Protagonist introduction, emotional anchor | M1 Ty garage; M2 Ty kitchen; S1 Sarah kitchen; S1 Sarah in passenger seat |
| **Reaction Close-Up** | Emotional beat, held face | M1 Ty face push-in; M2 Ty final face hold; S1 Sarah quiet contemplation |
| **Over-Shoulder** | Point-of-view transition, document reveal | S1 paperwork reveal ($1M policy) |
| **Environmental Establishing** | Location anchor, mood set | M3 Ty at intersection; S2 Laura at crosswalk; S1 I-10 corridor open |
| **Absurdist Object Shot** (WCTL-adapted) | Single-detail reveal, documentary discovery | M1/M2 empty parking spot where bike used to be; M2 medical bills and paused timesheet; S1 empty corporate conference room |

**NOT used in WCTL** (wrong register for empathy-driven PI): Wide Crowd Shot, Selfie POV, Confrontation Two-Shot, God View / Miniature, Command Center.

**Aspect ratios:** 9:16 vertical for video (Meta feed + Reels). 1:1 or 4:5 for static images (M3, S2). For video-ready reference portraits, use 4:5 so the frame crops clean to both 9:16 and 1:1 downstream.

---

## 5. Lighting Lock Options + Color Arc (upgraded 2026-04-23)

Pick ONE lighting mood per scene. Commit. Do not mix within a single ad — the Luca Maxim principle is consistency across shots in the same piece.

**Upgrade vs. prior version:** lighting mood no longer stands alone. Each mood is anchored to a director reference + a color register from `Color_and_Grade_Vocabulary.md`. This ensures that "natural window light" never appears as a generic phrase; every prompt uses the director's specific language for that light.

| Mood | Director anchor | Director-specific light phrase | Color register | WCTL Scenes |
|------|----------------|-------------------------------|----------------|-------------|
| **Golden / Warm** (identity, intact) | Coens/Fargo + PTA | "Deakins-Coens naturalism, golden-hour low sun, Vision3 warmth, motivated practical + window" | Warm amber identity | M1 Ty garage |
| **Indoor Institutional Cool** (loss, weight) | Mindhunter + Villeneuve | "Mindhunter dialogue-scene motivated light — overhead pendant + single warm practical, deep charcoal shadow fall-off, 4500K institutional cool" | Loss cool green-cyan + warm practical accent | M2 Ty kitchen; S1 Sarah kitchen closing |
| **Corporate Fluorescent Cold** | Mindhunter + BCS institutional | "Flat cool fluorescent overhead, conference-room grey-blue, dead even illumination, drained of warmth, no practical accent" | Corporate institutional | S1 empty corporate conference room cut |
| **Suburban Overcast Daytime** | Coens/Fargo TV + Sopranos | "Fargo TV motivated interior — kitchen pendant + cool window daylight in honest mixed temperature, Vision3 warmth base, subtle grain" | Muted Midwest earth + single saturated accent | S2 Laura crosswalk (late afternoon) |
| **Dusk Ambiguity** (injustice) | Lynch dusk + Villeneuve blue hour + True Det S1 sodium vapor | "Warm-sand earth foreground + cyan-fade upper sky gradient, amber streetlight just switched on with electrical hum, transitional blue-hour ambiguity, atmospheric haze if available" | Injustice dusk | M3 intersection (dusk moment) |

### 5b. Color Arc across the M1/M2/M3 Ty sequence

Ty is a serialized character across three concepts. His palette SHOULD shift to reinforce the emotional arc:

- **M1 Identity** → Warm amber (Coens/Fargo + PTA). Life intact. Golden hour. Vision3 warmth. Wardrobe includes his signature color (navy + motorcycle red). The bike is present.
- **M2 Loss** → Cool institutional green-cyan (Mindhunter + Villeneuve). The world gone clinical. Kitchen pendant + cool window. Skin pulled cool. The bike is absent (empty spot, helmet set aside, wedding ring prominent in hand-on-table shot).
- **M3 Injustice** → Dusk transitional (Lynch + Villeneuve + True Det). Warm-sand + cyan-fade. Ambiguous. Ty may not appear in frame at all, OR appear in silhouette at the intersection's edge. The location carries the weight.

This color arc is NOT applied automatically by the model — it must be specified in each prompt. The point of this color-arc table is to make sure each scene's prompt names its own register explicitly.

### 5c. Focus plane guidance

Every Elevated prompt specifies what's in focus and why. Defaults:

- **Character close-up / portrait** — eyes sharp, ears already softening, background soft. f/2.8.
- **Domestic table scene (M2 Loss)** — eyes sharp, foreground objects (bills, coffee, keys) in stacked focus falling off, background soft. f/2.8-f/4.
- **Working environment (M1 garage)** — subject sharp, motorcycle visible but slightly softened in middle ground, garage interior soft deep background. f/4.
- **Environmental wide (M3 intersection)** — whole intersection in focus, subject if present small in frame, atmospheric haze handling depth. f/5.6-f/8.
- **Dialogue two-shot (S1 corporate / therapy-office)** — both characters in matched focus, room soft. f/4.

### 5d. Negative space / implied-absence checklist

Every M1/M2/M3 prompt specifies an absent-presence:

- **M1 Identity** — the bike is PRESENT, but the future-absence is foreshadowed (the clean helmet, the healthy body, the unbroken possessions). Implied-absence: the scar Ty doesn't have yet.
- **M2 Loss** — the bike is ABSENT (empty parking spot visible through kitchen window, or helmet set on counter gathering dust, or wedding ring on hand that's healing). Implied-absence: the life Ty had.
- **M3 Injustice** — Ty himself is absent or peripheral. The intersection is the subject. Implied-absence: where Ty was standing when the car came through. No memorial marker (too specific / compliance-risky); just the emptiness of the place itself.

---

## 6. Motion Discipline

**Luca Maxim's motion doctrine is set to 10 out of 10 on emotion — theatrical slamming, cackling, finger-jabbing.** We explicitly reject this for WCTL. Empathy-driven creative does not accept theatrical performance; it loses the audience and breaks AZ Bar compliance (ER 7.1 truthfulness).

**What we keep from Luca Maxim** (the "Still Center" principle, `Luca_Maxim_Style.md` lines 141–152):

> **Option A: The Still Eye of the Storm.** Everyone around them is in chaotic motion. They remain composed, watching with satisfaction. The CONTRAST between their stillness and the chaos = power.

This translates to WCTL perfectly: protagonist composed, the chaos of post-accident life (paused timesheet, stacked bills, empty garage spot, corporate boardroom cold light) carries the weight. The protagonist doesn't act the emotion. The environment does.

**What we reject:** "Option B: The Source of Drama" — slamming, cackling, theatrical gesture. Never in WCTL.

---

## 6.5 Failure Mode Flags (regenerate if present)

Scan every Elevated output for these. Any of them = regenerate with tighter prompt:

| Failure | Likely cause | Fix |
|---------|--------------|-----|
| **Flat even lighting** (no motivated source visible, no shadow fall-off) | Prompt said "natural window light" without director anchor | Add Mindhunter / Villeneuve / Coens director phrase; name the source precisely |
| **Everything in focus** | No focus plane specified | Add focus-plane clause: "eyes sharp, ears softening, [thing] in blurred foreground" |
| **Centered symmetric composition where asymmetric was needed** | Model defaulted to center-frame | Add rule-of-thirds language; specify asymmetry |
| **Waxy / plastic / airbrushed skin** | Insufficient "no AI tells" discipline OR no camera-body specified | Add "Fujifilm X-T5" or "Sony A7R IV" language; strengthen negative prompt |
| **HDR / over-sharpened / over-saturated** | Model defaulted to commercial-ad aesthetic | Reinforce grain + Vision3 + desaturation |
| **Emotion signaled by prop instead of frame** (tear-on-cheek, hand-on-chest) | Prompt said "emotional" or "sad" without blocking language | Remove emotion-words; use stillness + light + focus to do the work |
| **Theatrical performance** (slamming / cackling / gesture-heavy) | Prompt drifted toward Luca Maxim §6 Option B | Reinforce "still eye of the storm" and §6 Motion Discipline |
| **Stock-photo composition** | No director anchor in the prompt | Add director anchor from §2a; the single densest fix available |
| **No director name in prompt at all** | Generic prompt | **Stop. Go to §2a. Pick a director. Rewrite from there.** |

---

## 7. Character-as-Insight Principles

Adopted verbatim in spirit from `Luca_Maxim_Style.md` §"⚠️ THE SECRET SAUCE: CHARACTER-AS-INSIGHT" (lines 22–120).

**The "I Know That Person" Test.** Before generating, ask:

| Check | Question |
|-------|----------|
| **Recognition** | Would the target audience say "that's my neighbor / my boss / my mom"? |
| **Specificity** | Are there at least 10 specific visual details defined? |
| **Archetype** | What "starter pack" is this character from? |
| **Class Markers** | Do the accessories and environment show economic reality? |
| **Emotional State** | Is the expression arc defined for every beat? |
| **No Generic Details** | Have I replaced every "a suit" with "charcoal pinstripe with burgundy tie"? |

**Full Character Sheet Method — every significant character needs a complete breakdown across these categories:**

| Category | What to Define |
|----------|----------------|
| Demographics | Age (specific decade), ethnicity, body type |
| Face | Specific features, weathering, expression default |
| Hair | Style, color, condition, what it says about them |
| Clothing (Every Item) | Top, layer, bottom, shoes — brand-level specific |
| Accessories | Watch, jewelry, bag, glasses — class/identity markers |
| Props | What's in their hands? What objects define them? |
| Environment | Where they ARE when we meet them — every background detail |
| Psychological State | What are they feeling? What's their arc? |
| Expression Range | How does their face move through the piece? |
| Easter Eggs | Small details that reward close viewing |

**WCTL status check (updated 2026-04-23):** `Archive/Week_1_Launch_Concepts_2026-04-21.md` is archive-only (superseded by `Creative/Week_1_Approval_Package/`). For character-as-insight briefs, pull from the canonical `Audience/Deep_Personas/` folder — `Sarah/01_Life_World.md`, `Diana/01_Life_World.md`, `Laura/01_Life_World.md`, and `Ty/01_Life_World.md` (the motorcycle persona, renamed 2026-04-22 from Marco cruiser to Ty supersport). Deep_Personas is the authoritative source for all character specificity.

---

## 8. Negative Prompts — Elevated-specific

Append this to every Elevated image and video prompt:

```
NO theatrical emotion, NO slamming, NO cackling,
NO exaggerated gesture, NO scare-tactic imagery,
NO crash footage or simulated crash,
NO over-saturated color, NO HDR look,
NO over-sharpened edges, NO airbrushed finish,
NO plastic or waxy skin, NO symmetrical faces,
NO uncanny eyes, NO glowing skin, NO text in image,
NO watermark, NO logo.
```

---

## 9. Examples That Worked

*Davis pastes successful prompts here as he iterates in Higgsfield and Kling. Format:*

```
### [Date] — [Asset] — [Character]
**Higgsfield seed / Kling seed:** [capture from UI]
**Full prompt used:** [paste verbatim]
**What worked:** [1-2 lines — the specific thing this prompt got right]
**What to keep next time:** [takeaway for v2 of the Injection Block]
```

*(Section currently empty. Add entries after each successful generation.)*

---

## 10. Iteration Notes

*Free-text area. Observations about what's producing results and what isn't. Update as you go.*

*(Currently empty.)*

---

## 11. Asset Index

Live list of which WCTL assets use this style. Update when adding or removing an asset from the Elevated allocation.

| Asset | Format | Character | Scene | Status |
|-------|--------|-----------|-------|--------|
| M1 — Identity | Video 15–30s | Ty Rivera | Garage, golden hour | Pending reference lock |
| M2 — Loss | Video 15–30s | Ty Rivera | Kitchen morning | Pending reference lock |
| M3 — Injustice | Static 1:1 + 9:16 | Ty Rivera | Intersection dusk | Pending reference lock |
| S1 — Trucking | Video 15–30s | Sarah | I-10 passenger seat → kitchen | Pending reference lock |
| S2 — Pedestrian | Static 1:1 + 9:16 | Laura | Suburban crosswalk, late afternoon | Pending reference lock |
| Reference portrait — Ty Rivera | Still | Ty Rivera | Neutral | Prompt ready — see `Phase_1_Reference_Portrait_Prompts.md` |
| Reference portrait — Sarah | Still | Sarah | Neutral | Prompt ready — see `Phase_1_Reference_Portrait_Prompts.md` |
| Reference portrait — Laura | Still | Laura | Neutral | Prompt ready — see `Phase_1_Reference_Portrait_Prompts.md` |

---

*See also: `UGC_Native.md` for S5 Diana (the one UGC-allocated asset). `Phase_1_Reference_Portrait_Prompts.md` for the four ready-to-run reference portrait prompts built on these two sheets.*

---

## 12. Cross-references (upgraded 2026-04-23)

The 2026-04-23 upgrade of this style sheet anchors every prompt in Giuseppe's director library and companion knowledge. When writing or iterating prompts, load:

| Need | File |
|------|------|
| **Director anchor (start here)** | `Abracadabra/04_Production/Giuseppe_Karma_(AI_Creative_Director)/Director_Reference_Library/README.md` |
| **Color as emotional register** | `../../../../04_Production/Giuseppe_Karma_(AI_Creative_Director)/Color_and_Grade_Vocabulary.md` |
| **Film stock / format vocabulary** | `../../../../04_Production/Giuseppe_Karma_(AI_Creative_Director)/Film_Stock_and_Format.md` |
| **Blocking, gesture, eye-line, pacing, negative space** | `../../../../04_Production/Giuseppe_Karma_(AI_Creative_Director)/Blocking_and_Pacing.md` |
| **Diegetic audio for Kling 3.0 / Seedance 2.0** | `../../../../04_Production/Giuseppe_Karma_(AI_Creative_Director)/Audio_Prompting.md` |
| **Shot / lens / camera grammar** | `../../../../04_Production/Giuseppe_Karma_(AI_Creative_Director)/Cinematography_Direction.md` |
| **Luca Maxim original style sheet (this sheet extends)** | `../../../../04_Production/Giuseppe_Karma_(AI_Creative_Director)/Influencer_Styles/Luca_Maxim_Style.md` |

**The single most useful workflow:** before writing a prompt, open the relevant director profile from `Director_Reference_Library/`, lift specific phrases from its "Prompt Vocabulary" section, then fill the bracketed slots in §2b and §3a above. This produces prompts 5-10x denser than writing from scratch.

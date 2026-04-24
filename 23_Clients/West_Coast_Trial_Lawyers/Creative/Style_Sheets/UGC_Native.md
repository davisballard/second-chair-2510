# Style Sheet — UGC Native (Barry Hott Doctrine × WCTL)
## Second Chair × West Coast Trial Lawyers — Arizona Pilot

**Prepared:** 2026-04-22
**Anchored to:** Barry Hott Ugly Ads Doctrine (referenced in `Week_1_Launch_Concepts.md` line 38 + §"Production Standards (Hott)" line 343) + Giuseppe Karma's MODE B UGC framework (`Abracadabra/04_Production/Giuseppe_Karma_(AI_Creative_Director)/AGENT.md` §5 MODE B).
**Status:** v1 — living document. Paste working prompts into §9 and observations into §10 as you iterate.

---

## 0. CRITICAL SC DISCIPLINE — AI SUBJECTS DO NOT SPEAK ON CAMERA

**Every SC ad is voiceover-narrated. AI-generated characters are caught-being-themselves, NOT performing dialogue.** This applies to UGC Native as rigorously as to Elevated Documentary. Applies to every prompt generated from this sheet.

**Prompt-level enforcement (must appear in every UGC image AND video prompt):**

```
SUBJECT DOES NOT SPEAK ON CAMERA. Mouth closed or slightly open
in natural breath only — NO lip movement, NO dialogue delivery,
NO mouthing words, NO mid-word speech shape, NO "talking head
to camera" pose. The character is caught mid-moment (mid-exhale,
mid-glance, mid-thought), NOT performing or delivering.
Voiceover narration is generated via ElevenLabs TTS in post
(Ennio Morricone's VO_Direction_Playbook), NOT delivered by the
AI subject. No dialogue from the subject, no spoken lines inside
the generated clip.
```

**Why UGC-specific note:** UGC's default instinct is "selfie-cam testimonial" — a person talking directly to the phone camera. SC's UGC register explicitly rejects that. The UGC subject here is caught being herself while someone ELSE (spouse, sister, family friend) films her — she's not addressing the camera, not performing a monologue. The VO in post narrates her situation over the silent-on-camera observation.

**Failure flag (regenerate if present):**
- Subject talking directly to camera in a "selfie testimonial" pose → regen with "caught mid-moment, subject not aware of the camera's purpose, not performing for it."
- Mouth in mid-word / speech shape → regen with no-speech rule reinforced.

---

## 1. Purpose & how to use

This style sheet is the source of truth for the **UGC Native** treatment. In Phase 1 that means **one asset (S5 Diana MVA) + Diana's reference portrait.** This is the UGC test against 5 Elevated Documentary assets (see `Elevated_Documentary.md`). After 7–10 days of Meta data, Phase 2 decides whether UGC scales.

**Workflow per generation:**

1. **Still image in Higgsfield (ChatGPT Images 2.0):** copy the §2 Image Injection Block into the top of your prompt. Then append the character brief + scene spec + side-specific detail reminders.
2. **Video animation in Kling 3.0 Pro / O1 or Seedance 2.0:** upload the locked reference still as the character image. Copy the §3 Video Injection Block. Append the scene's motion description. Generate. See `Abracadabra/04_Production/Giuseppe_Karma_(AI_Creative_Director)/Prompting_Guides/Kling_3.md` and `Seedance_2.md` for full model-specific prompting references.
3. **After generation:** if the output worked, paste the full prompt + seed into §9 Examples That Worked.

**Core premise of this style** (Barry Hott): authenticity beats production on Meta feed. The ad blends into organic content. The viewer doesn't scroll past because it reads as someone's family member filmed it, not as an ad. UGC that ADMITS it's an ad in its aesthetic fails this test — which is why we reject "glossy UGC" and aim for actual phone-camera imperfection.

---

## 1.5 Director Anchor: explicit NONE (upgraded 2026-04-23)

**UGC rejects director references on principle.** Unlike `Elevated_Documentary.md`, this style sheet has NO director anchor. Every cinematographer / director reference phrase is FORBIDDEN inside UGC prompts:

- NO Fincher / Mindhunter / Villeneuve / Deakins / Arkapaw / Slovis / Coens / Hawley / Fukunaga / PTA / Sakharov / Lynch / Wong Kar-wai
- NO Alec Soth / Nadav Kander / cinematographer references
- NO director-specific lighting phrases ("Mindhunter dialogue light," "Prisoners weight," "Fargo TV warmth")
- NO color-register names from `Color_and_Grade_Vocabulary.md` ("loss cool institutional," "identity warm amber")
- NO film-stock / cinema-format phrases ("35mm Vision3," "Arri Alexa," "anamorphic 2.39:1")

**Why:** these phrases compress cinematic grammar, which is the OPPOSITE of what UGC wants. Adding them to a UGC prompt produces the "glossy UGC" failure — a phone-camera-looking image that still reads as "ad" because it's secretly cinematic underneath.

**Instead:** UGC prompts commit to phone-camera vocabulary — iPhone 14 Pro, auto-white-balance, deep focus, handheld wobble, flat phone color. The closest cinematic-adjacent reference allowed is "early handheld documentary" as a GRAMMAR reference only, never invoked in the prompt itself.

---

## 2. Image Injection Block — ChatGPT Images 2.0 (Higgsfield)

Copy the block between the fences verbatim and paste at the top of every UGC image prompt:

```
iPhone 14 Pro or Samsung Galaxy S24 phone camera photo,
natural daylight from a window or overhead domestic light
(no studio lighting, no motivated cinematic light).
Slightly shaky handheld feel, candid, authentic, casual.
Unposed, imperfect composition — slightly off-center,
subject occasionally glances off-camera or is caught mid-moment.
Looks like a real person filmed this themselves on their phone —
not an ad, not editorial, not studio. Feed-native composition.
No film grain (phone sensors don't produce cinematic grain).
No shallow depth of field (phone cameras have deep focus).
No cinematic color grading — natural flat phone color,
slightly compressed dynamic range, auto white-balance feel.
Skin texture shows pores, fine lines, subtle asymmetry.
Hair has flyaways. No AI tells — no waxy skin,
no symmetrical face, no plastic finish, no airbrushed quality,
no over-saturated color, no HDR, no text in image,
no watermark, no logo.
```

---

## 3. Video Injection Block — Kling 3.0 Pro / O1 or Seedance 2.0

Copy the block between the fences verbatim and paste at the top of every UGC video prompt:

```
Phone camera video handheld movement — natural subtle wobble,
organic re-frame mid-clip as if the filmer slightly adjusts grip,
subject moves naturally without choreography.
NO choreographed push-ins, NO dollies, NO whip pans,
NO cinematic motion grammar, NO slow motion,
NO color grading, NO film grain.
Natural daylight or domestic overhead light, flat phone color,
auto-exposure feel (slight shift if lighting changes mid-clip).
Subject may briefly glance off-camera, look down, re-settle.
Real-person energy — looks like someone's spouse, sibling,
or family friend filmed this on their iPhone from a chair
across the kitchen. Ambient domestic sound feel.
Character face consistent with the uploaded reference image —
same face, same wardrobe, same side-specific props
(sling on right arm, bruise on right jawline) as the reference.
```

---

## 4. Composition Rules

**Aspect ratios:** 9:16 vertical primary (Meta Reels, Stories feed). 1:1 secondary (Facebook feed). Reference portrait at 4:5 for flexibility.

**Shot types that fit UGC Native:**

| Shot Type | When | Example |
|-----------|------|---------|
| **Handheld waist-up** | Subject in their environment, relatable | Diana at kitchen table, envelopes stacked in foreground |
| **Tabletop down-on-phone** | Document reveal, letter close-up, bill stack | Medical bill close-up, timesheet paused on laptop |
| **Chest-up candid** | Face hold, micro-reaction | Diana's quiet face hold at the final beat |
| **Wide domestic** | Environment establishing, kitchen or living room | Diana's kitchen at morning, natural light from window |

**NOT used in UGC Native** (too cinematic): Hero Medium Shot (too composed), Reaction Close-Up Cinematic (too tight/moody), Environmental Establishing (too wide / location-prestige), Absurdist Object Shot (too discovered). UGC composition is naturalistic and imperfect on purpose.

---

## 5. Lighting Lock Options

Pick ONE per scene. UGC lighting is what the phone actually captures — natural, flat, not motivated.

| Mood | Keywords | WCTL Scene |
|------|----------|------------|
| **Indoor Natural (window daylight)** | diffused daylight through window, neutral white balance, no hard shadows | S5 Diana kitchen morning |
| **Kitchen Ambient** | overhead kitchen pendant + window mix, warm 3000K + 5500K blend | S5 Diana kitchen breakfast scene |
| **Domestic Warm Afternoon** | late-afternoon window light, slightly warm, slightly shadowed | S5 alternate time-of-day test if morning doesn't land |

---

## 6. Motion Discipline

UGC motion is the **opposite** of cinematic. Reject every instinct to compose, time, or dramatize motion.

**What works:**
- Natural handheld wobble throughout the clip.
- Subject moves on their own rhythm, not synchronized to beats.
- Camera operator (invisible) occasionally re-frames mid-clip as if adjusting grip — this is a *feature*, not a bug, because it reads as authentic.
- Subject may look off-camera briefly and return to the activity. No "performance."

**What fails:**
- Any slow-motion. Phones don't default to slow-motion; when they do, it's obvious.
- Any camera push-in or pull-back. UGC cameras are static or wandering, not intentional.
- Any "dramatic reveal" — UGC doesn't reveal, it captures.
- Any synchronized motion or kinetic editing feel. UGC is loose.

---

## 6.5 Failure Mode Flags (regenerate if present)

UGC has its own failure modes — distinct from Elevated. Scan every UGC output for:

| Failure | Why it fails | Fix |
|---------|--------------|-----|
| **Cinematic shallow depth of field** (blurred background behind subject) | Phone sensors physically can't do this; readers clock it as "fake" | Reinforce "deep focus, phone-sensor sharpness throughout" in prompt |
| **Desaturated / graded color** | Phones default to auto-white-balance, not cinematic grade; graded color = secretly-cinematic | Add "no color grading, flat phone color, auto-WB" language |
| **Motivated dramatic lighting / single-source with deep shadow** | Phone cameras fill shadows — they don't render deep charcoal shadow fall-off | Add "overall even room light, phone-camera fill behavior, no deep shadow" |
| **Film grain present** | Phone sensors don't produce cinematic grain — they produce digital noise, which looks different | Add "NO film grain — phone sensors don't produce grain; minor digital sensor noise acceptable if any" |
| **Composed / centered / rule-of-thirds framing** | UGC framing is imperfect — off-center, unposed, feed-native | Reinforce "imperfect framing, subject slightly off-center, caught mid-moment" |
| **Studio-clean sound or cinematic ambient** | UGC is filmed with phone on-board mic — room tone is honest, imperfect, includes the filmer's small sounds | Specify "phone on-board mic capture, natural imperfect room tone, no studio audio" |
| **Performed / posed subject** | UGC subjects don't perform — they're caught in a moment | Reinforce "unposed, caught mid-moment, subject may glance off-camera briefly" |
| **Any cinematographer / director reference** (even implicit — "like a documentary") | Named in §1.5; UGC rejects all director anchors | Remove every reference name; re-center on phone-camera vocabulary |
| **Subject's face too pretty / skin too clean / eyes too bright** | Cinematic skin treatment smuggled into UGC register | Reinforce "honest skin texture, pores visible, fine lines, no airbrushing, phone-camera skin capture" |

---

## 7. Character-as-Insight Principles

**Specificity is style-agnostic — the same character-as-insight standard from Luca Maxim applies here.** See `Elevated_Documentary.md` §7 for the full framework ("I Know That Person" test + Full Character Sheet Method). Do not re-describe per generation — paste the Diana character brief verbatim from `Week_1_Launch_Concepts.md` line 89.

**UGC-specific character notes:**
- Diana's props and side-specific details must survive the UGC style shift. The phone-camera look can flatten detail — call out the sling-on-RIGHT-arm, the bruise-on-RIGHT-jawline, the mole-above-LEFT-lip explicitly and twice in the prompt.
- Diana's emotional register in UGC should feel MORE intimate than Elevated — UGC earns the right to linger on a quiet face that an Elevated frame would compose around.

---

## 8. Negative Prompts — UGC-specific

Append this to every UGC image and video prompt:

```
NO film grain (phone cameras don't produce cinematic grain),
NO shallow depth of field (phones have deep focus),
NO cinematic color grading (no desaturated lifted blacks,
no orange-and-teal, no muted filters),
NO motivated dramatic lighting, NO studio lighting,
NO glamour lighting, NO editorial aesthetic,
NO "ad" quality, NO perfect framing, NO centered composition,
NO posed subject, NO performed emotion, NO scare-tactic imagery,
NO Deakins reference, NO Soth reference, NO Kander reference,
NO cinematographer reference of any kind,
NO over-saturated color, NO HDR, NO plastic or waxy skin,
NO symmetrical faces, NO uncanny eyes, NO text in image,
NO watermark, NO logo.
```

---

## 9. Examples That Worked

*Davis pastes successful prompts here as he iterates. Format:*

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

*Free-text area. UGC is harder than Elevated because the AI's instinct is to over-compose and over-light. Observations about what's producing a truly phone-candid result go here.*

*(Currently empty.)*

---

## 11. Asset Index

Live list of which WCTL assets use this style.

| Asset | Format | Character | Scene | Status |
|-------|--------|-----------|-------|--------|
| S5 — MVA | Video 15–30s | Diana | Kitchen, morning, envelopes falling | Pending reference lock |
| Reference portrait — Diana | Still | Diana | Neutral domestic (UGC framing) | Prompt ready — see `Phase_1_Reference_Portrait_Prompts.md` |

---

*See also: `Elevated_Documentary.md` for the 5 Elevated assets (M1, M2, M3, S1, S2) and the Marco/Sarah/Laura reference portraits. `Phase_1_Reference_Portrait_Prompts.md` for the four ready-to-run reference portrait prompts.*

---

## 12. Cross-references (upgraded 2026-04-23)

UGC Native deliberately does NOT load most of Giuseppe's director / color / film-stock knowledge — those files exist to build CINEMATIC output, which is the opposite of what UGC wants. However, some Giuseppe knowledge is still useful here:

| Use | File | Notes |
|-----|------|-------|
| UGC aesthetic reference | `../../../../04_Production/UGC_Aesthetic_Reference.md` | Phone eras, lo-fi, social platform aesthetics |
| Giuseppe's MODE B (UGC) framework | `../../../../04_Production/Giuseppe_Karma_(AI_Creative_Director)/AGENT.md` §5 MODE B | Phone-era selection table, prompt framework |
| Blocking discipline (stillness, gesture economy, eye-line) | `../../../../04_Production/Giuseppe_Karma_(AI_Creative_Director)/Blocking_and_Pacing.md` | Applies to UGC too — UGC subjects are unposed but still follow natural body-language grammar |
| Audio prompting (diegetic ambient for Kling 3.0 / Seedance 2.0) | `../../../../04_Production/Giuseppe_Karma_(AI_Creative_Director)/Audio_Prompting.md` | UGC uses phone on-board mic register — see "UGC phone-camera color" phrase in that doc |

**DO NOT load for UGC:**
- `Director_Reference_Library/` (explicitly forbidden — §1.5)
- `Color_and_Grade_Vocabulary.md` (color-register names = cinematic smuggling)
- `Film_Stock_and_Format.md` except for the iPhone / phone-camera section

The UGC discipline is SUBTRACTIVE — we remove cinematic language, not add it. When in doubt, ask "would a real person filming with their phone ever think of this phrase?" If no, don't use it.

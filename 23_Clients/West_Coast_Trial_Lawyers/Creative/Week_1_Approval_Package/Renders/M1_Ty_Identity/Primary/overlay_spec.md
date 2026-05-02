# M1 Ty Identity — Overlay Spec

**Unit:** M1 Ty Identity — Primary
**Register:** Elevated Documentary
**Audio:** `vo_v3_today_break_bill_padded.mp3` (Bill voice, padded 1.2s)
**Created:** 2026-04-25

Governed by `../../../../../../02_Visual/Designed_Overlay_System.md §6 Patterns 4 + 5` (Editorial register).

---

## VO Reference

```
Riders don't ask for sympathy. They ask for what's fair.
A driver didn't see him. The bills don't stop. The presumption doesn't either.
No fee unless we win. Find out what fair looks like. Today.
```

---

## Hook Card (0.0–3.0s)

| Element | Spec |
|---------|------|
| Sub-line | `M1 — MOTORCYCLE / ARIZONA` — Söhne Mono 11pt small caps, Cream `#FFF7F0`, letterspacing 80, position top 28% |
| Burgundy rule | 0.5pt Burgundy `#490A0A`, full-width, position top 33% |
| Headline | `Riders don't ask / for sympathy.` — Tiempos Headline 76pt, Cream `#FFF7F0`, two lines, position top 38–48% |
| Contrast device | 80% Warm Charcoal `#1C1917` scrim, gradient fade-down, top third (Ty's garage golden-hour footage is bright/warm — Cream-on-bright-warm needs the dark scrim) |
| Motion | Bass two-beat reveal: sub-line + rule fade up t=0.0–0.3s; headline blur-to-sharp t=0.0–0.4s. Hold to 3.0s. |
| Retire | Cross-fade out at 3.0s as VO transitions to "They ask for what's fair." (which becomes the Peak Card content) |

---

## Peak Card (~3.5–5.5s)

**Variant C — Quote Card.**

| Element | Spec |
|---------|------|
| Position in spot | At the VO line "They ask for what's fair" (~3.5s — early Peak; this VO frontloads the emotional core) |
| Quote text | `"They ask for / what's fair."` — Tiempos Headline 44pt italic, Warm Charcoal on Cream knockout chip, two lines |
| Knockout chip | Cream `#FFF7F0`, 90% width centered, padding 32px, anchored 60–80% Y |
| Burgundy rule | 0.5pt Burgundy below the quote, half-width left-aligned (echoes Hook Card rule, structural continuity) |
| Motion | Patrick Clair living-photograph reveal: blur-to-sharp 0.0–0.6s, tracking tightens 3%, holds 1.4s |
| Retire | Cross-fade out at 5.5s as VO transitions to "A driver didn't see him." |

**Why Quote, not Defined Term:** the line "They ask for what's fair" *is* Fair Case's brand thesis in one sentence. Letting it appear in print at the emotional peak doubles the brand resonance — the spot's headline and Fair Case's positioning collapse into the same statement.

**Why early Peak (3.5s vs typical 5–8s):** M1's VO frontloads the thesis ("Riders don't ask for sympathy. They ask for what's fair") in the first 4 seconds. The Peak Card lands on the hinge of those two sentences. The remaining 11s of VO ("A driver didn't see him...") plays against footage with captions only — no overlay competition.

---

## Always-on Captions (full duration)

CapCut auto-captions per `Giuseppe_Karma/Text_Overlay_System.md §1`. Inter Bold 22pt, white with 2px black stroke, bottom-center, 250px safe zone. Word-by-word reveal at VO pace.

**Caption coordination:** Peak Card retires at 5.5s. Captions continue uninterrupted through the back half of the spot.

---

## CTA Frame (13.5–15.0s)

| Element | Spec |
|---------|------|
| Background | Roman Navy `#0D1F3C` 80% scrim over closing footage of Ty's garage, OR diegetic finish per short-form rule |
| Headline | `Find out what fair looks like.` — Tiempos 32pt, Cream `#FFF7F0` |
| CTA chip | `Free Case Review` — Inter Semibold 16pt, Roman Navy on Torch Amber `#C8821A` chip |
| Torch mark | Fair Case torch (white wordmark, Torch Amber flame), bottom-left, 24% width |
| Source | Per `../../../../../../20_Fair_Case/04_Visual_Identity_Brief/BRAND_SYSTEM_BRIEF.md` Ad Creative Overlay Rule |

---

## CapCut Asset List

- Tiempos Headline (Medium + Italic) — load via Adobe Fonts sync into CapCut
- Söhne Mono — CapCut custom font upload
- Inter Bold + Inter Semibold — CapCut native
- 80% Warm Charcoal scrim PNG (top-third gradient) — generate once, reuse for M1/M2/S1 dark-scrim variants
- Cream knockout chip PNG (rounded rect, 90% width) — shared with S1
- Burgundy 0.5pt rule (PNG strip) — shared
- Fair Case torch mark (white wordmark + Torch Amber flame)

---

## Export Crops

- 9:16 (Reels native) — primary
- 4:5 (Feed)
- ~~1:1~~ — deprecated 2026-05-01 (Davis: "I never see them"); do not produce square crops

---

## Verification

- [ ] Mobile-mute scroll: Hook Card readable on iPhone in <0.5s. (Indigo)
- [ ] Footage-grade legibility: Cream-on-Warm-Charcoal-scrim holds against the garage golden-hour grade. (Massimo)
- [ ] Peak Card brand resonance: line `"They ask for what's fair."` reads as Fair Case thesis in print form. (Giuseppe + Indigo)
- [ ] No spatial collision: Peak Card (60–80% Y) and captions (90% Y) don't compete. (Graham)
- [ ] No Roman Navy or Torch Amber as letter-fill except CTA frame. (Massimo)

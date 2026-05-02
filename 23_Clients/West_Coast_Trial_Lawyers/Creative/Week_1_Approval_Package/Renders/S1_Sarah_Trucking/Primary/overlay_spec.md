# S1 Sarah Trucking — Overlay Spec

**Unit:** S1 Sarah Trucking — Primary
**Register:** Elevated Documentary
**Audio:** `vo_s1_primary_bill_padded.mp3` (Bill voice, padded 1.2s)
**Created:** 2026-04-25

Governed by `../../../../../../02_Visual/Designed_Overlay_System.md §6 Patterns 4 + 5` (Editorial register).

---

## VO Reference

```
Hit by a Freightliner on I-17?
Commercial insurance is different.
Their legal team was working before the ambulance arrived.
Arizona trial attorneys fight commercial carriers every day.
Start with a free case review.
Find out what fair looks like. Today.
```

---

## Hook Card (0.0–3.0s)

| Element | Spec |
|---------|------|
| Sub-line | `S1 — TRUCKING / I-17 PHOENIX` — Söhne Mono 11pt small caps, Cream `#FFF7F0`, letterspacing 80, position top 28% |
| Burgundy rule | 0.5pt Burgundy `#490A0A`, full-width, position top 33% |
| Headline | `HIT BY A FREIGHTLINER / ON I-17?` — Tiempos Headline 72pt, Warm Charcoal `#1C1917`, two lines, position top 38–48% |
| Contrast device | 60% Cream scrim, gradient fade-down, top third of frame |
| Motion | Bass two-beat reveal: sub-line + rule fade up t=0.0–0.3s; headline blur-to-sharp t=0.0–0.4s. Hold to 3.0s. |
| Retire | Cross-fade out at 3.0s as VO transitions to "Commercial insurance is different." |

---

## Peak Card (~6.5–8.5s)

**Variant C — Quote Card.**

| Element | Spec |
|---------|------|
| Position in spot | At the VO line "Their legal team was working before the ambulance arrived" (~6.5s) |
| Quote text | `"Their legal team was working / before the ambulance arrived."` — Tiempos Headline 40pt, italic on the second line, Warm Charcoal on Cream knockout chip |
| Knockout chip | Cream `#FFF7F0`, 90% width centered, padding 32px, anchored 60–80% Y |
| Burgundy rule | 0.5pt Burgundy below the quote, half-width left-aligned |
| Motion | Patrick Clair living-photograph reveal: blur-to-sharp 0.0–0.6s, tracking tightens 3%, holds 1.4s |
| Retire | Cross-fade out at 8.5s as VO transitions to "Arizona trial attorneys fight commercial carriers every day." |

**Why Quote, not Defined Term:** The dramatic line carries more conversion weight for sound-off viewers than a definitional anchor. Indigo's call: the line *is* the proof; let it be the proof in print.

---

## Always-on Captions (full duration)

CapCut auto-captions per `../../../../../../../04_Production/Giuseppe_Karma_(AI_Creative_Director)/Text_Overlay_System.md §1`. Inter Bold 22pt, white with 2px black stroke, bottom-center, 250px safe zone above UI controls. Word-by-word reveal at VO pace.

**Caption coordination:** Peak Card lives at 60–80% Y; captions live at 90% Y. No spatial collision.

---

## CTA Frame (13.5–15.0s)

| Element | Spec |
|---------|------|
| Background | Roman Navy `#0D1F3C` 80% scrim over closing footage, OR diegetic finish + Meta button per short-form rule |
| Headline | `Find out what fair looks like.` — Tiempos 32pt, Cream `#FFF7F0` |
| CTA chip | `Free Case Review` — Inter Semibold 16pt, Roman Navy on Torch Amber `#C8821A` chip |
| Torch mark | Fair Case torch (white wordmark, Torch Amber flame), bottom-left, 24% width |
| Source | Per `../../../../../../20_Fair_Case/04_Visual_Identity_Brief/BRAND_SYSTEM_BRIEF.md` Ad Creative Overlay Rule |

---

## CapCut Asset List

- Tiempos Headline (Medium + Italic) — load via Adobe Fonts sync into CapCut
- Söhne Mono — CapCut custom font upload
- Inter Bold + Inter Semibold — CapCut native
- 60% Cream scrim PNG (top-third gradient) — generate once, reuse across S1 variants
- Cream knockout chip PNG (rounded rect, 90% width)
- Burgundy 0.5pt rule (PNG strip)
- Fair Case torch mark (white wordmark + Torch Amber flame, transparent BG)

---

## Export Crops

- 9:16 (Reels native, 1080×1920) — primary
- 4:5 (Feed, 1080×1350) — center-crop hook headline
- ~~1:1~~ — deprecated 2026-05-01 (Davis: "I never see them"); do not produce square crops

---

## Verification

- [ ] Mobile-mute scroll test: open on iPhone, mute, scroll into the spot — Hook Card readable in <0.5s? (Indigo)
- [ ] Footage-grade legibility: Hook Card legible against the I-17 daylight footage. Test Warm Charcoal AND Cream variants. (Massimo)
- [ ] Peak Card timing: Quote Card lands at VO peak (~6.5s), retires before next line. (Giuseppe)
- [ ] Captions don't fight Peak Card. (Graham)
- [ ] No Roman Navy or Torch Amber as letter-fill anywhere except CTA frame. (Massimo)

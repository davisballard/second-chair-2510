# S5 Diana MVA — Overlay Spec

**Unit:** S5 Diana MVA — Primary
**Register:** UGC-Native
**Audio:** `vo_s5_primary_bill_padded.mp3` (Bill voice, padded 1.2s)
**Created:** 2026-04-25

Governed by `../../../../../../02_Visual/Designed_Overlay_System.md §6 Patterns 4 + 5` (UGC-Native register).

---

## VO Reference

```
[serious]
Broken bones.
Bills don't stop.
Insurance is already calling.
They want a recorded statement before you have a lawyer.
You don't have to give one.
Arizona trial attorneys fight insurance every day.
Get your free case review in sixty seconds.
No fee unless they win.
```

---

## Hook Card (0.0–3.0s)

| Element | Spec |
|---------|------|
| Headline | `Broken bones. / Bills don't stop.` — Inter Black 60pt, two lines, white `#FFFFFF` with 2px black `#000000` stroke |
| Position | Top-third, anchored 25% from top, 5% from left edge |
| Sub-line | (none — UGC tolerates Hook without sub-line) |
| Contrast device | 2px black stroke only — **NO scrim, NO Tiempos, NO Burgundy rule, NO Söhne** |
| Motion | Snap-cut on at frame 0. Holds to 3.0s. Snap-cut off at 3.0s. |

**Discipline note:** Resist the editorial instinct. The UGC failure mode is smuggling Tiempos / scrim / Burgundy rule into a UGC frame and producing "glossy UGC" — which fails `UGC_Native.md §6.5`. Inter Black + black stroke + iPhone-Notes register **is** the design.

---

## Peak Card (~7.0–9.0s)

**Variant B — Defined Term** (UGC adaptation: Inter, not Tiempos italic).

| Element | Spec |
|---------|------|
| Position in spot | At the VO line "They want a recorded statement before you have a lawyer" (~7.0s) |
| Term | `RECORDED STATEMENT` — Inter Black 36pt caps with letterspacing 60, white with 2px black stroke |
| Definition line | `WHAT INSURANCE ASKS FOR BEFORE YOU HAVE A LAWYER` — Inter Bold 14pt caps with letterspacing 80, white with 1px black stroke |
| Position on frame | Bottom-third, anchored 70% from top, centered |
| Knockout chip | None (UGC) — black stroke is the device |
| Burgundy rule | None (UGC) |
| Motion | Snap-cut on, hold 2.0s, snap-cut off. **No Patrick Clair reveal in UGC register** — that smuggles editorial in. |

**Why Defined Term, not Hero Number:** the 2026-04-25 VO rewrite (recorded-statement frame) replaced the prior "$18,000 they offered" anchor. Diana's audience needs the educational moment ("recorded statement = legal trap") more than a stat. Indigo's call: *the term is the conversion lever*.

**Why not a Quote Card on "You don't have to give one":** that line is the emotional peak, but a Quote Card on it reads as preachy in UGC register. The Defined Term lets the VO say it while the visual *teaches* the term — the sound-off viewer learns what's at stake without being told what to do.

---

## Always-on Captions (full duration)

CapCut auto-captions per `Giuseppe_Karma/Text_Overlay_System.md §1`. Inter Bold 22pt, white with 2px black stroke, bottom-center, 250px safe zone. Word-by-word reveal at VO pace.

**Caption coordination:** Hook owns top third; Peak owns mid-bottom (70% Y); captions own bottom 10% (90% Y). No spatial collision.

---

## CTA Frame (13.5–15.0s) — UGC EXCEPTION

UGC-mode CTA per `../../../../../../20_Fair_Case/04_Visual_Identity_Brief/BRAND_SYSTEM_BRIEF.md` UGC Branding Exception.

| Element | Spec |
|---------|------|
| Background | Diegetic finish — Diana sets phone down or returns to morning task; no graphical scrim |
| CTA text | `See Options` — Inter Bold 32pt, Torch Amber `#C8821A` on the word "Options", rest white with 2px black stroke |
| Torch mark | **NONE** in the ad creative itself. Torch mark + full Fair Case branding appear post-click on the landing page. |

---

## CapCut Asset List

- Inter Black, Inter Bold, Inter Semibold — CapCut native fonts
- **No Tiempos. No Söhne Mono. No Cream scrim. No Burgundy rule.** UGC discipline.
- Black stroke effect: CapCut Text → Stroke → 2px, color `#000000`
- Fair Case torch mark — **NOT used in ad creative**; loaded only on landing page

---

## Export Crops

- 9:16 (Reels native) — primary
- 4:5 (Feed) — Hook Card stays top-anchored
- ~~1:1~~ — deprecated 2026-05-01 (Davis: "I never see them"); do not produce square crops

---

## Verification

- [ ] Mobile-mute scroll: Hook Card readable on iPhone in <0.5s. (Indigo)
- [ ] UGC discipline check: NO Tiempos, NO scrim, NO Burgundy rule anywhere in the spot. (Massimo — UGC register gate)
- [ ] Peak Card educational anchor: a sound-off viewer who has never heard "recorded statement" understands the legal stakes by 9.0s. (Indigo)
- [ ] No torch mark in ad creative — torch mark only on landing page. (Brand compliance)
- [ ] Black stroke holds against Diana's kitchen footage (typically warm/well-lit). (Graham)

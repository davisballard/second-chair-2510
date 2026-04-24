# Second Chair - Creative Ideation Process

> Brand-specific creative workflow for PI lead generation ads.
> 
> This file extends the core `SKILL.md` with Second Chair context.
> 
> **For interactive image iteration, see:** `AD_IMAGE_ITERATION.md`

---

## Brand Context

**Second Chair** generates leads for personal injury law firms, focusing on motor vehicle accidents (MVA). The strategy emphasizes:

- **Unbranded/service-first** positioning (not firm-centric)
- **Lo-fi, authentic** creative that bypasses ad blindness
- **Behavioral science** hooks (loss aversion, self-reference, urgency)
- **AI-generated imagery** (P1 priority until creator partnerships active)

## Research Files to Reference

Load these for context during planning:

| File | What It Contains |
|------|------------------|
| `07_Research/Creative_Resources/Hooks_And_Angles.md` | Proven angle frameworks, hook categories, injury-type specifics |
| `07_Research/Strategic_Insights/Visual_Insights.md` | Image direction, prompt templates, what converts |
| `07_Research/Strategic_Insights/Content_Strategy.md` | Channel economics, strategic landscape, creative principles |
| `07_Research/Strategic_Insights/Funnel_Insights.md` | Conversion data, platform performance |

---

## The 80/20 Creative Split

- **80%** — Within the realm of what's proven to work
- **20%** — Novel, experimental, outside-the-box

> "The most important thing is that we're calling out our avatar... beyond that you could be as outlandish as you want."

---

## Priority Behavioral Triggers

Ranked by effectiveness for PI advertising:

| Rank | Trigger | Example Hook |
|------|---------|--------------|
| P1 | **Loss Aversion** | "Don't let the deadline cost you..." |
| P1 | **Self-Reference** | "If this happened to you in [City]..." |
| P1 | **Temporal Framing** | Before/after transformation visuals |
| P2 | **Authority (Earned)** | War room, visible work, document close-ups |
| P2 | **Moral Framing** | Insurance as villain, David vs Goliath |
| P2 | **Situational Priming** | Time/weather/location matching |

---

## Angle Categories (From Research)

### 1. The "Counterfactual" Angle
- **Psychology:** Regret aversion + loss framing
- **Visual:** Before/after comparisons, split-screen paths
- **Hook:** "5 years from now, will you wish you had called?"

### 2. The "Insider Exposé" Angle
- **Psychology:** Information asymmetry, conspiracy framing
- **Visual:** "Leaked document" aesthetics, green screen over documents
- **Hook:** "The internal memo adjusters don't want you to see..."

### 3. The "Pattern Recognition" Angle
- **Psychology:** Self-referencing effect
- **Visual:** Situational imagery matching viewer context
- **Hook:** "If you drive [Highway] in [City]..."

### 4. The "Asymmetric Knowledge" Angle
- **Psychology:** Competence signaling through revelation
- **Visual:** War room, behind-the-scenes, document close-ups
- **Hook:** "There's a document you can request that changes everything..."

### 5. The "Moral Inversion" Angle
- **Psychology:** Haidt's fairness/harm foundations
- **Visual:** Corporate coldness vs human warmth, scale imbalance
- **Hook:** "They profit when you accept less. We don't."

### 6. The "Temporal Pressure" Angle
- **Psychology:** Scarcity + loss aversion on time
- **Visual:** Clock/calendar imagery, countdown aesthetics
- **Hook:** "Your legal deadline and your evidence deadline are not the same."

---

## Image Prompt Templates

### POV / Self-Reference
```
POV perspective from inside a car, hands on steering wheel, 
looking through [damaged/cracked] windshield, 
[specific situation], natural daylight, 
hyper-realistic, shot on iPhone
```

### Transformation / Before-After
```
Split image: left side shows [negative state], 
right side shows [positive outcome], 
warm home environment, documentary style
```

### Authority / War Room
```
Attorney workspace shot from above, legal documents spread 
across desk, multiple monitors showing case files, coffee cup,
hand with pen making notes, natural office lighting, candid
```

### Metaphor / David vs Goliath
```
[Large corporate element] casting shadow over [small human element],
dramatic lighting, visual metaphor for power imbalance, 
editorial photography style
```

### Situational / Local
```
[Specific intersection/highway] in [City], daytime, 
clear view of traffic signals and street signs, 
documentary photography style, realistic lighting
```

---

## Text in Images (Updated 2026-04-23)

*ChatGPT Image 2 shipped 2026-04-21. The old "AI can't do text" rule is retired for stills generated through ChatGPT Image 2 in Higgsfield — it renders readable text at ~99% accuracy on typography, including handwriting and non-Latin scripts. See `Abracadabra/04_Production/Giuseppe_Karma_(AI_Creative_Director)/ChatGPT_Images_2_Capability_Report.md`.*

### What's Now Available in the SC Stills Pipeline

| Scenario | Status | How to prompt |
|----------|--------|---------------|
| **Close-up document with readable copy** | ✅ SUPPORTED | Quote the exact text: `reading exactly "[copy]"`. Specify font style, weight, color. Use `quality=high`. |
| **Handwritten notes / legal pad / prescription / signed cursive** | ✅ SUPPORTED | Anchor surface + tool ("pencil on yellow legal pad"), quote exact words, specify penmanship style. |
| **Packaging, signage, book covers, menus, posters** | ✅ SUPPORTED | Render in-frame with the scene's lighting. Much more believable than post-comp'd overlays. |
| **Phone screens with real UI labels** | ✅ SUPPORTED | Describe as if the product exists; specify status bar, buttons, native design (iOS / Android). |
| **Non-Latin signage (ZH/JA/KO/Hindi/Bengali/Arabic)** | ✅ SUPPORTED | Specifically called out as a model strength. Specify script type for Arabic ("thuluth," "naskh"). |

### When to Still Render Without Text (Creative / Pragmatic Reasons)

Not limitations — these are deliberate choices:

| Scenario | Why |
|----------|-----|
| Blurred-document aesthetic is the mood | The "quiet math of a bad situation" — text-out-of-focus IS the creative (e.g., Fair Case IG series) |
| Copy must be editable downstream | AI output is raster; can't change words without full re-render |
| Compliance-critical copy | Human-verify or set in real design tools |
| Running a non-ChatGPT-Image-2 model | FLUX, older Nano Banana, etc. still garble text — legacy workarounds below still apply |

### Legacy Workarounds (keep for non-ChatGPT-Image-2 runs)

```
# Distance/angle
Hands holding official-looking document, shot from behind 
the shoulder, document partially visible, warm office lighting

# Heavy blur
Stack of legal documents on desk, shallow depth of field, 
text intentionally blurred, focus on coffee cup in foreground

# Envelope/implication
Opened manila envelope with confidential stamp, papers 
partially pulled out, suggesting hidden information

# Context not content
Person surrounded by scattered paperwork and bills, 
stressed expression, documents visible but not readable
```

**Rule of Thumb (updated):** Decide whether the text is narratively *present* (part of the frame's meaning, now renderable) or narratively *implied* (out-of-focus mood prop, where blur IS the creative). Both are valid. Pre-2026-04-21 the choice was forced by the model; now it's a director's call.

---

## Platform Guidelines

### Meta (Primary)
- **Aspect Ratio:** `1:1` (feed) or `4:5` (feed, more real estate)
- Style: Behavioral science imagery, self-referential
- Text: Under 125 characters primary
- Focus: POV perspectives, transformation, metaphor

### TikTok/Reels (Future)
- **Aspect Ratio:** `9:16` (vertical)
- Style: Native platform fonts, lo-fi aesthetic
- Creator-dependent (P3 priority)

### Google Display
- **Aspect Ratio:** `16:9` (leaderboard), `4:3`, `1:1` (square)
- Style: Clean, readable, clear CTA
- Simpler imagery works better

### Fal.ai Settings by Platform

| Platform | Recommended Aspect Ratio | Resolution |
|----------|-------------------------|------------|
| Meta Feed | `1:1` or `4:5` | `1K` |
| Meta Stories | `9:16` | `1K` |
| TikTok/Reels | `9:16` | `1K` |
| Google Display | `16:9` or `4:3` | `1K` |
| Landing Page Hero | `16:9` | `2K` |

---

## Compliance Checkpoints

Before finalizing any ad, verify:

- [ ] "Attorney Advertising" disclaimer included where required
- [ ] No specific dollar guarantees
- [ ] No misleading claims about insurance companies
- [ ] Recovery amount claims have partner firm data (currently paused)
- [ ] "Dramatization" disclosure if actors used

Reference: `06_Legal/Saul.md` for full rulebook.

---

## Output Example

When ready for production, format like this:

```python
pending_jobs = [
    {
        "type": "image",
        "ad_title": "Deadline Urgency: Loss Aversion",
        "post_copy": "California accident victims have limited time to file. Your window is closing. See if you still qualify before it's too late.",
        "image_prompt": "POV from driver seat, hands gripping steering wheel tightly, looking at clock on dashboard showing 11:55, rain on windshield, anxious mood, natural daylight, photorealistic, shot on iPhone",
        "strategy": "Loss aversion - fear of missing statute deadline",
        "state": "CA",
        "client": "Jacoby & Meyers",
        "channel": "Meta",
        "variations": 3,  # Creates IMG, IMG 2, IMG 3
        "aspect_ratio": "1:1",
    },
    {
        "type": "image",
        "ad_title": "Insider Exposé: Adjuster Playbook",
        "post_copy": "Insurance adjusters follow a script designed to minimize your claim. Here's what they're trained to say—and what they won't tell you.",
        "image_prompt": "Close-up of official-looking document with 'INTERNAL TRAINING MANUAL' header, partially visible text about claim tactics, coffee ring stain on paper, office desk background, leaked document aesthetic, editorial photography",
        "strategy": "Information asymmetry - insider knowledge reveal",
        "state": "CA",
        "client": "Jacoby & Meyers",
        "channel": "Meta",
        "variations": 3,
        "aspect_ratio": "1:1",
    },
]
```

### Field Reference

| Field | Maps to Airtable | Notes |
|-------|------------------|-------|
| `ad_title` | Ad Title | Use format "Concept: Approach" for multiple similar ads |
| `post_copy` | Post Copy | The social post text |
| `image_prompt` | Image Prompt | Detailed Fal.ai prompt |
| `strategy` | Strategy | Short behavioral science rationale |
| `state` | State | Use abbreviations: CA, CO, NV, WA, NC, SC, GA, MS |
| `client` | Client | "Jacoby & Meyers" or "Think Law" |
| `channel` | Channel | Meta, TikTok, Google, YouTube, etc. |
| `aspect_ratio` | Aspect Ratio | 1:1, 4:5, 9:16, 16:9, etc. |
| `variations` | IMG, IMG 2, IMG 3 | 1-3 images per row |
| `record_id` | (updates row) | Optional - include to UPDATE existing row |

---

## Updating Existing Rows

To regenerate images for an existing ad, include the `record_id`:

```python
{
    "type": "image",
    "record_id": "recXXXXXXXXXXXXXX",  # From Airtable URL
    "image_prompt": "Revised prompt with better direction...",
    "variations": 3,
}
```

**Find record ID:** Open row in Airtable → URL ends with `recXXXXXXXXXXXXXX`

### Client → State Mapping

| Client | States |
|--------|--------|
| **Jacoby & Meyers** | CA, CO, NV, WA |
| **Think Law** | NC, SC, GA, MS (currently paused) |

### Channel → Aspect Ratio Defaults

| Channel | Recommended Aspect Ratio |
|---------|-------------------------|
| Meta Feed | 1:1 or 4:5 |
| Meta Stories | 9:16 |
| TikTok | 9:16 |
| Google Display | 16:9 or 1:1 |
| YouTube | 16:9 |

---

## Generating Multiple Concepts

When asked for multiple behavioral approaches to the same idea:
- Create **separate jobs** for each approach (each = 1 Airtable row)
- Use `variations` to control images per row

**Example:** "5 behavioral approaches with 3 images each" = 5 jobs × 3 variations = 15 images across 5 rows

**Ad Title Naming Convention:**
```
Base Concept: Behavioral Approach
```
Examples:
- "Deadline Urgency: Loss Aversion"
- "Deadline Urgency: Regret Aversion"
- "Deadline Urgency: Evidence Decay"
- "Deadline Urgency: Moral Framing"
- "Deadline Urgency: Social Proof"

This makes it easy to filter/group related concepts in Airtable.

---

## Quick Reference Commands

### Chat-First Workflow (Preferred)

```
# Generate images in chat
> "Generate 3 variations of a settlement gap infographic"

# Iterate
> "Make image 1 more aggressive"
> "Try image 2 with Nevada desert background"

# Push to Airtable when ready
> "Add images 1 and 3 to record recXXXXXXXXXXXXXX"
> "Create new row with all images"
```

**See `AD_IMAGE_ITERATION.md` for full interactive workflow.**

### Batch Production (Alternative)

```bash
# For bulk generation without iteration
cd Abracadabra/04_Production/_Ad_Factory
python production.py --brand Lead_Faucet

# Dry run (preview without generating)
python production.py --brand Lead_Faucet --dry-run
```

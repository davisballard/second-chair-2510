"""Generate M1 Ty Identity Primary music — Ennio direction, 2 variants A/B.

Ad = 15s. Per Ennio's 25% rule, generate 20s so Stable Audio's tail-off
zone (final ~20-25%) falls after the ad ends.

Per Ennio's Under-VO Bed Rule (locked 2026-04-24): use HOLD structure
(not build/peak), add "underscore bed for voiceover" to mood, and
auto-post-process with FFmpeg loudnorm LRA=5 to tame dynamics.
"""
import asyncio
import os
import subprocess
import sys
import urllib.request
from pathlib import Path

REPO_ROOT = Path("/Users/davisballard/Documents/claude-creative-work")

# Load FAL_KEY
env_file = REPO_ROOT / ".env"
if env_file.exists():
    for line in env_file.read_text().splitlines():
        if line.strip() and not line.startswith("#") and "=" in line:
            key, _, val = line.partition("=")
            os.environ.setdefault(key.strip(), val.strip().strip('"').strip("'"))

import fal_client  # type: ignore

OUT_DIR = Path(__file__).parent

# =========================================================================
# PIVOT (after Davis rejected A/B as "too filmy / too sparse"):
# Reference target = Lead Faucet's "Against the Machine" — David-vs-Goliath
# driving hybrid orchestral. Punch + gravitas. Fills and motivates.
#
# Moving from contemplative film-score composers (Morricone, Cave/Ellis) to
# the hybrid-orchestral-with-percussion lane where film score meets trailer
# underscore (Zimmer / Göransson). These composers anchor the model toward
# weight AND momentum.
# =========================================================================

# =========================================================================
# REGIONAL-LAYER VARIANTS (2026-04-24)
# Davis picked Göransson driving bed (D) as the spine. Adding 4 regional
# textures on top, each a distinct "Arizona rider at dawn" signature.
# All keep under-VO bed rule: hold structure, no peaks, post-processed.
# =========================================================================

# E — Calexico Borderlands (most Arizona-specific)
#   Göransson spine + Sonoran slide guitar + brushed trumpet + canyon reverb
VARIANT_E_PROMPT = (
    "Hybrid orchestral underscore bed, "
    "driving low tom drums and deep brass pulse under reverbed slide guitar and muted brushed trumpet echoing off canyon walls, "
    "Sonoran warmth and driving momentum sustained throughout, underscore bed for voiceover, "
    "intro 2s, hold 15s, tail 3s, "
    "in the style of Göransson driving percussion layered with Calexico Feast of Wire Arizona Sonoran Americana, "
    "no vocals no lyrics no choir no singing"
)

# F — Explosions in the Sky American-Road (wide emotional anthem)
#   Göransson spine + post-rock cascading reverb guitars
VARIANT_F_PROMPT = (
    "Hybrid orchestral underscore bed with post-rock guitars, "
    "driving low tom drums and deep brass pulse under cascading reverb electric guitar arpeggios and sustained atmospheric swell, "
    "wide American West open-road emotion and driving momentum sustained throughout, underscore bed for voiceover, "
    "intro 2s, hold 15s, tail 3s, "
    "in the style of Göransson driving percussion layered with Explosions in the Sky Your Hand in Mine, "
    "no vocals no lyrics no choir no singing"
)

# G — Daniel Hart Working-Class Folk-Minor (weathered gravitas)
#   Göransson spine + folk-ambient fiddle drone + plaintive guitar + harmonium
VARIANT_G_PROMPT = (
    "Hybrid orchestral underscore bed with American folk textures, "
    "driving low tom drums and deep brass pulse under distant fiddle drone and plaintive acoustic guitar and warm harmonium layer, "
    "working-class weathered gravitas and driving momentum sustained throughout, underscore bed for voiceover, "
    "intro 2s, hold 15s, tail 3s, "
    "in the style of Göransson driving percussion layered with Daniel Hart score for A Ghost Story and The Green Knight, "
    "no vocals no lyrics no choir no singing"
)

# H — Morricone-Ghost (rider mythology subtly invoked)
#   Göransson spine + Morricone textures BURIED deep in the mix
VARIANT_H_PROMPT = (
    "Hybrid orchestral underscore bed with Western mythology textures buried deep, "
    "driving low tom drums and deep brass pulse carrying the spine, with distant reverbed harmonica far back in the mix and wind atmospheric layer, "
    "lone rider lineage undertone and driving momentum sustained throughout, underscore bed for voiceover, "
    "intro 2s, hold 15s, tail 3s, "
    "in the style of Göransson driving percussion with Morricone Once Upon a Time in the West harmonica ghosted deep in the mix, "
    "no vocals no lyrics no choir no singing"
)

DURATION = 20  # 15s ad × 1.25 rounded up
GUIDANCE_SCALE = 4.0  # refine pass — stronger anchor now that register target is specific
NUM_STEPS = 8


async def generate_one(name: str, prompt: str) -> Path:
    print(f"\n[{name}] Generating 20s music cue...")
    print(f"         Prompt: {prompt[:80]}...")
    handler = await fal_client.submit_async(
        "fal-ai/stable-audio-25/text-to-audio",
        arguments={
            "prompt": prompt,
            "seconds_total": DURATION,
            "num_inference_steps": NUM_STEPS,
            "guidance_scale": GUIDANCE_SCALE,
        },
    )
    result = await handler.get()
    url = result.get("audio", {}).get("url")
    if not url:
        raise RuntimeError(f"No audio URL in response: {result}")
    raw_path = OUT_DIR / f"music_{name}_raw.mp3"
    bedded_path = OUT_DIR / f"music_{name}_bedded.mp3"
    urllib.request.urlretrieve(url, raw_path)
    print(f"         [OK] Raw saved: {raw_path.name}")
    print(f"         Source URL: {url}")

    # Under-VO Bed Rule post-processing (locked 2026-04-24):
    # loudnorm I=-16 TP=-1.5 LRA=5 compresses dynamics hard so cue
    # is audible from bar 1 and never drowns VO at peak.
    subprocess.run(
        ["ffmpeg", "-y", "-i", str(raw_path),
         "-af", "loudnorm=I=-16:TP=-1.5:LRA=5",
         "-c:a", "libmp3lame", "-q:a", "2", str(bedded_path)],
        check=True, capture_output=True,
    )
    print(f"         [OK] Bedded saved (LRA=5): {bedded_path.name}")
    return bedded_path


async def main() -> None:
    # Run all 4 regional-layer variants in parallel
    tasks = [
        asyncio.create_task(generate_one("E_calexico_sonoran", VARIANT_E_PROMPT)),
        asyncio.create_task(generate_one("F_explosions_road", VARIANT_F_PROMPT)),
        asyncio.create_task(generate_one("G_daniel_hart_folk", VARIANT_G_PROMPT)),
        asyncio.create_task(generate_one("H_morricone_ghost", VARIANT_H_PROMPT)),
    ]
    await asyncio.gather(*tasks)
    print("\nAll 4 regional variants generated. A/B/C/D and pick the winner.")


if __name__ == "__main__":
    asyncio.run(main())

"""Generate S5 Diana MVA Primary music — Reznor lane round 2.

Round 1 (2026-04-25): A=Hildur Chernobyl, B=Reznor Social Network, C=Martinez
Contagion. Davis confirmed B (Reznor) was closest but trailed off in the middle.
A and C didn't hit.

Round 2 fix: stay in the Reznor & Ross modern institutional cool lane, push
HARD on anti-fadeout language so energy stays locked through the middle.
The "trails off in middle" issue is Stable Audio's natural tendency to dip
intensity around the midpoint — kill it with explicit "sustained at constant
intensity throughout, NO energy dip in middle, ostinato runs continuously".

3 new variants:
- A — Reznor & Ross Gone Girl SUSTAINED (Sugar Storm + Empty Spaces blend,
      domestic dread fits Diana's kitchen UGC visual)
- B — Reznor & Ross THE KILLER methodical (Fincher 2023, very controlled
      repeating melodic cells, locked sustain, doesn't trail by design)
- C — Ben Salisbury & Geoff Barrow DEVS (modern corporate menace, Reznor-
      adjacent, sustained synth pad with consistent low pulse, the cleanest
      "institutional bureaucracy moving against you" register in modern
      film/TV scoring)

Per Ennio's Under-VO Bed Rule: HOLD structure, "underscore bed for
voiceover", FFmpeg loudnorm LRA=5 post-process. 25s target (19.3s VO × 1.25).
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
# S5 DIANA MVA PRIMARY — ROUND 2 (Reznor lane, anti-fadeout pushed)
# =========================================================================

# Universal anti-fadeout clause — paste in every prompt to kill the middle dip
ANTI_FADEOUT = (
    "sustained at constant intensity throughout the entire 25 seconds, "
    "NO energy dip in the middle, NO fadeout in the middle, "
    "underlying pad and low-end pulse sustain consistently from start to finish without diminishing, "
    "ostinato pattern repeats steadily without break, "
    "underscore intensity locked throughout"
)

# A — Reznor & Ross Gone Girl SUSTAINED (Sugar Storm + Empty Spaces domestic dread)
VARIANT_A_PROMPT = (
    "Cinematic minimalist underscore bed, "
    "sustained warm-cool synthesizer pad with slow repeating piano ostinato in minor key "
    "and processed string drone layered above and faint metallic shimmer textures and subtle low-end synth pulse, "
    "quiet domestic dread and house-full-of-ghosts uncanny tension, "
    f"{ANTI_FADEOUT}, underscore bed for voiceover, "
    "intro 2s, hold 18s, tail 5s, "
    "in the style of Trent Reznor and Atticus Ross Gone Girl \"Sugar Storm\" sustained domestic eerie tension "
    "and \"Empty Spaces\" locked quiet dread and \"Background Noise\" institutional pressure, "
    "no vocals no lyrics no choir no singing"
)

# B — Reznor & Ross THE KILLER methodical (Fincher 2023, controlled repeating cells)
VARIANT_B_PROMPT = (
    "Cinematic minimalist underscore bed, "
    "short repeating melodic cell on cool synthesizer that loops continuously throughout "
    "with sustained warm-cool pad layered underneath and faint processed string textures and steady low-end synth thrum, "
    "quiet methodical procedural tension and locked controlled menace, "
    f"{ANTI_FADEOUT}, underscore bed for voiceover, "
    "intro 2s, hold 18s, tail 5s, "
    "in the style of Trent Reznor and Atticus Ross The Killer 2023 \"Killer Theme\" repeating melodic cell discipline "
    "and The Social Network \"Hand Covers Bruise\" institutional cool restraint, "
    "no vocals no lyrics no choir no singing"
)

# C — Ben Salisbury & Geoff Barrow DEVS corporate menace (Reznor-adjacent institutional)
VARIANT_C_PROMPT = (
    "Cinematic minimalist underscore bed, "
    "sustained cool synthesizer pad with slow continuous arpeggiated synth sequence "
    "and processed string layer and constant low-end synth thrum and subtle digital noise floor, "
    "modern corporate institutional menace and quiet system-moving-against-you tension, "
    f"{ANTI_FADEOUT}, underscore bed for voiceover, "
    "intro 2s, hold 18s, tail 5s, "
    "in the style of Ben Salisbury and Geoff Barrow Devs \"Devs Theme\" sustained corporate menace "
    "and Annihilation alien institutional dread and Trent Reznor and Atticus Ross The Social Network institutional cool, "
    "no vocals no lyrics no choir no singing"
)

DURATION = 25
GUIDANCE_SCALE = 4.0
NUM_STEPS = 8


async def generate_one(name: str, prompt: str) -> Path:
    print(f"\n[{name}] Generating 25s music cue...")
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

    subprocess.run(
        ["ffmpeg", "-y", "-i", str(raw_path),
         "-af", "loudnorm=I=-16:TP=-1.5:LRA=5",
         "-c:a", "libmp3lame", "-q:a", "2", str(bedded_path)],
        check=True, capture_output=True,
    )
    print(f"         [OK] Bedded saved (LRA=5): {bedded_path.name}")
    return bedded_path


async def main() -> None:
    tasks = [
        asyncio.create_task(generate_one("R2_A_reznor_gone_girl_sustained", VARIANT_A_PROMPT)),
        asyncio.create_task(generate_one("R2_B_reznor_killer_methodical", VARIANT_B_PROMPT)),
        asyncio.create_task(generate_one("R2_C_devs_corporate_menace", VARIANT_C_PROMPT)),
    ]
    await asyncio.gather(*tasks)
    print("\nAll 3 S5 Round 2 variants generated. R2_A / R2_B / R2_C — pick the winner against the VO.")


if __name__ == "__main__":
    asyncio.run(main())

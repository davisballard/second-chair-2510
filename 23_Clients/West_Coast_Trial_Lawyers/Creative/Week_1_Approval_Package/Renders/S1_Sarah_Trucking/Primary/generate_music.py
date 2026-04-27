"""Generate S1 Sarah Trucking Primary music — Ennio direction, 3 variants A/B/D.

Ad VO came in at ~21s. Per Ennio's 25% rule, generate 25s so Stable Audio's
tail-off zone (final ~20-25%) falls after the VO ends.

Per Ennio's Under-VO Bed Rule (locked 2026-04-24): use HOLD structure
(not build/peak), add "underscore bed for voiceover" to mood, and
auto-post-process with FFmpeg loudnorm LRA=5 to tame dynamics.

Register: dusk highway DREAD + asymmetric power. Reference family =
Sicario / Jóhann Jóhannsson / Reznor & Ross. NOT M1's warm-amber gravitas.
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
# S1 SARAH TRUCKING PRIMARY — 3 VARIANTS
# Davis picked A, D, B from the 4 concepts. Skipping C (Reznor clinical).
# =========================================================================

# A — Jóhannsson Sicario "Beast" (industrial low-end pulse, most on-nose for dusk semi)
VARIANT_A_PROMPT = (
    "Cinematic industrial underscore bed, "
    "sustained deep synthesizer low-end drone and slow distant kick drum pulse at hypnotic tempo, "
    "with microtonal string drone layered above and faint metallic percussion textures, "
    "mounting oppressive looming weight and pre-incident dread sustained throughout, underscore bed for voiceover, "
    "intro 2s, hold 19s, tail 4s, "
    "in the style of Jóhann Jóhannsson Sicario \"The Beast\" sustained border-crossing tension "
    "and Trent Reznor Atticus Ross Bird Box industrial dread, "
    "no vocals no lyrics no choir no singing"
)

# B — Göransson Oppenheimer driving INTENSIFIED (M1 family, harder edge)
VARIANT_B_PROMPT = (
    "Hybrid orchestral underscore bed with relentless intensified percussion, "
    "driving synthesized string ostinato carrying a propulsive four-note pattern over deep brass "
    "and aggressive low tom drums and metallic industrial percussion at consistent intensity, "
    "mounting cold tension and asymmetric David-versus-Goliath momentum sustained throughout, underscore bed for voiceover, "
    "intro 2s, hold 19s, tail 4s, "
    "in the style of Ludwig Göransson score for Oppenheimer Trinity scene drone intensified "
    "with Black Panther sustained percussion and Sicario industrial weight, "
    "no vocals no lyrics no choir no singing"
)

# D — Truck-as-Beast diegetic-leaning (literal threat as score)
VARIANT_D_PROMPT = (
    "Cinematic industrial underscore bed blending tonal diesel-engine drone into orchestral textures, "
    "deep tuned diesel-truck engine rumble pitched to a low E note layered with sustained low brass pulse "
    "and slow distant kick drum and faint metallic chain-rattle percussion, "
    "relentless mechanical mounting weight and looming highway dread sustained throughout, underscore bed for voiceover, "
    "intro 2s, hold 19s, tail 4s, "
    "in the style of Jóhann Jóhannsson Sicario truck-corridor sequences and Hans Zimmer Dunkirk shepard-tone tension "
    "layered with diegetic semi-truck diesel rumble tuned to score key, "
    "no vocals no lyrics no choir no singing"
)

DURATION = 25  # 21s VO × 1.25 ≈ 26 → 25s
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

    # Under-VO Bed Rule post-processing (locked 2026-04-24):
    # loudnorm I=-16 TP=-1.5 LRA=5 compresses dynamics hard
    subprocess.run(
        ["ffmpeg", "-y", "-i", str(raw_path),
         "-af", "loudnorm=I=-16:TP=-1.5:LRA=5",
         "-c:a", "libmp3lame", "-q:a", "2", str(bedded_path)],
        check=True, capture_output=True,
    )
    print(f"         [OK] Bedded saved (LRA=5): {bedded_path.name}")
    return bedded_path


async def main() -> None:
    # Run 3 variants in parallel: A, B, D
    tasks = [
        asyncio.create_task(generate_one("A_johannsson_sicario_beast", VARIANT_A_PROMPT)),
        asyncio.create_task(generate_one("B_goransson_intensified", VARIANT_B_PROMPT)),
        asyncio.create_task(generate_one("D_truck_as_beast_diegetic", VARIANT_D_PROMPT)),
    ]
    await asyncio.gather(*tasks)
    print("\nAll 3 S1 variants generated. A/B/D — pick the winner against the VO.")


if __name__ == "__main__":
    asyncio.run(main())

"""Generate S2 Laura Pedestrian Primary music — Lonergan/Coens/PTA quiet lane.

Ennio's call (2026-04-27): the Reznor lane Diana ran is too sharp for Laura.
Laura is not a corporate-menace target — she is the suburban librarian who
walked the same three-mile loop for fifteen years. Her music is not attack;
it is settling. Documented truth coming to rest.

Three variants in the quiet-documentary composer lane:
- A — Lesley Barber Manchester by the Sea SUSTAINED (literal Lonergan composer,
      chamber strings + piano hymn restraint, dignified grief without melodrama)
- B — Carter Burwell Coens-quiet (Fargo + No Country sparse piano + low string
      drone, AZ-suburban-Americana documentary observation)
- C — Jonny Greenwood Phantom Thread restraint (chamber strings ostinato +
      minor-key piano figure, dignified PTA-elevated documentary discipline)

Anti-fadeout discipline locked from Diana Round 2: Stable Audio's natural
middle-dip is the enemy of any under-VO bed. Explicit "sustained at constant
intensity throughout, NO energy dip in middle, ostinato runs continuously"
clause in every prompt.

Per Ennio's Under-VO Bed Rule: HOLD structure (not build-and-peak),
"underscore bed for voiceover", FFmpeg loudnorm LRA=5 post-process.
20s target (15s ad × 1.33 with intro/tail breath).
"""
import asyncio
import os
import subprocess
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
# S2 LAURA PRIMARY — Lonergan/Coens/PTA quiet lane
# =========================================================================

# Universal anti-fadeout clause — every prompt gets this
ANTI_FADEOUT = (
    "sustained at constant intensity throughout the entire 20 seconds, "
    "NO energy dip in the middle, NO fadeout in the middle, "
    "underlying pad and low-end pulse sustain consistently from start to finish without diminishing, "
    "ostinato pattern repeats steadily without break, "
    "underscore intensity locked throughout"
)

# A — Lesley Barber Manchester by the Sea SUSTAINED (literal Lonergan composer)
VARIANT_A_PROMPT = (
    "Cinematic minimalist underscore bed, "
    "sustained warm chamber string pad in minor key with slow repeating piano figure "
    "and faint cello drone layered underneath and quiet brushed cymbal texture, "
    "dignified domestic grief and documented-truth-settling-in quiet weight, "
    "hymn-restraint emotional discipline without melodrama, "
    f"{ANTI_FADEOUT}, underscore bed for voiceover, "
    "intro 2s, hold 15s, tail 3s, "
    "in the style of Lesley Barber Manchester by the Sea \"Lee's Theme\" sustained chamber-string grief discipline "
    "and Manchester by the Sea \"Joe Dies\" quiet hymn-restraint, "
    "no vocals no lyrics no choir no singing"
)

# B — Carter Burwell Coens-quiet (Fargo + No Country)
VARIANT_B_PROMPT = (
    "Cinematic minimalist underscore bed, "
    "sparse repeating piano figure in minor key with sustained low string drone "
    "and faint Americana acoustic guitar texture and subtle low-end synth pulse layered underneath, "
    "AZ-suburban-Americana quiet documentary observation and small-town serious-things register, "
    "Coen-brothers warm interior register without cliche, "
    f"{ANTI_FADEOUT}, underscore bed for voiceover, "
    "intro 2s, hold 15s, tail 3s, "
    "in the style of Carter Burwell Fargo \"A Lot of Woe\" quiet Americana documentary "
    "and No Country for Old Men \"Blood Trail\" sustained low-string discipline "
    "and Carter Burwell True Grit \"The Wicked Flee\" sparse Americana piano restraint, "
    "no vocals no lyrics no choir no singing"
)

# C — Jonny Greenwood Phantom Thread restraint (PTA-elevated documentary)
VARIANT_C_PROMPT = (
    "Cinematic minimalist underscore bed, "
    "sustained chamber string ostinato in minor key with occasional repeating minor-key piano figure "
    "and faint processed string layer and subtle low-end thrum underneath, "
    "dignified PTA-elevated documentary discipline and quiet contemplative observation, "
    "restraint as the emotional structure, "
    f"{ANTI_FADEOUT}, underscore bed for voiceover, "
    "intro 2s, hold 15s, tail 3s, "
    "in the style of Jonny Greenwood Phantom Thread \"House of Woodcock\" sustained chamber-string ostinato "
    "and There Will Be Blood \"Open Spaces\" quiet sustained string drone "
    "and Phantom Thread \"For the Hungry Boy\" minor-key piano figure restraint, "
    "no vocals no lyrics no choir no singing"
)

DURATION = 20
GUIDANCE_SCALE = 4.0
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
        asyncio.create_task(generate_one("A_barber_manchester_sustained", VARIANT_A_PROMPT)),
        asyncio.create_task(generate_one("B_burwell_coens_quiet", VARIANT_B_PROMPT)),
        asyncio.create_task(generate_one("C_greenwood_phantom_restraint", VARIANT_C_PROMPT)),
    ]
    await asyncio.gather(*tasks)
    print("\nAll 3 S2 Laura music variants generated. A / B / C — pick the winner against the VO.")


if __name__ == "__main__":
    asyncio.run(main())

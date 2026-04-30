"""Generate M3 Ty Injustice V4 Video Primary music — 4 distinct lanes.

Ennio's call: M3-V4 is the INJUSTICE frame. Ty's emotional arc through the
script is melancholy/dignified → determined → vindicated → forward — NOT
angry, NOT theatrical. The music must carry "they blamed him, the record
proves otherwise" without leaning combat or institutional-cold.

Four lanes:
- A — Nick Cave / Warren Ellis (Jesse James) SUSTAINED. M1 continuity, the
      proven Ty register — sparse violin + sustained piano + low drone.
      Working-class lone-rider grief lifting into determined vindication.
- B — Jonny Greenwood (Phantom Thread / TWBB) restraint. Chamber-string
      ostinato + minor-key piano. PTA-elevated forensic discipline,
      "the record speaks" register.
- C — Calexico Sonoran Americana. Sustained acoustic + faint trumpet +
      low desert drone. Geographic AZ-specific — lone rider in the
      Chandler/Phoenix desert dusk.
- D — Daniel Hart (A Ghost Story) folk-determined. Sustained string pad +
      repeating folk guitar + warm low-end pulse. Warmer than Cave/Ellis,
      same dignified-vindication arc, more Americana register.

Anti-fadeout discipline locked from Diana Round 2 + Laura S2 — Stable
Audio's natural middle-dip kills under-VO beds. Explicit "sustained at
constant intensity throughout, NO energy dip in middle, ostinato runs
continuously" clause in every prompt.

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

env_file = REPO_ROOT / ".env"
if env_file.exists():
    for line in env_file.read_text().splitlines():
        if line.strip() and not line.startswith("#") and "=" in line:
            key, _, val = line.partition("=")
            os.environ.setdefault(key.strip(), val.strip().strip('"').strip("'"))

import fal_client  # type: ignore

OUT_DIR = Path(__file__).parent

ANTI_FADEOUT = (
    "sustained at constant intensity throughout the entire 20 seconds, "
    "NO energy dip in the middle, NO fadeout in the middle, "
    "underlying pad and low-end pulse sustain consistently from start to finish without diminishing, "
    "ostinato pattern repeats steadily without break, "
    "underscore intensity locked throughout"
)

# A — Nick Cave / Warren Ellis (Jesse James) SUSTAINED — M1 continuity, proven Ty lane
VARIANT_A_PROMPT = (
    "Cinematic minimalist underscore bed, "
    "sparse solo violin carrying a slow ascending three-note motif over sustained piano "
    "and distant low string drone and faint warm low-end pulse layered underneath, "
    "working-class lone-rider grief lifting toward determined vindication, "
    "documented-truth-emerging quiet weight without melodrama, "
    f"{ANTI_FADEOUT}, underscore bed for voiceover, "
    "intro 2s, hold 15s, tail 3s, "
    "in the style of Nick Cave and Warren Ellis score for The Assassination of Jesse James "
    "\"Song for Jesse\" sustained violin discipline "
    "and \"Cowgirl\" sparse piano + low drone restraint "
    "and \"Falling\" warm Americana lone-rider register, "
    "no vocals no lyrics no choir no singing"
)

# B — Jonny Greenwood (Phantom Thread / TWBB) restraint — forensic discipline lane
VARIANT_B_PROMPT = (
    "Cinematic minimalist underscore bed, "
    "sustained chamber string ostinato in minor key with occasional repeating minor-key piano figure "
    "and faint processed string layer and subtle low-end thrum underneath, "
    "PTA-elevated forensic discipline and the-record-speaks documentary observation, "
    "restraint as the emotional structure, dignified factual vindication without theatrics, "
    f"{ANTI_FADEOUT}, underscore bed for voiceover, "
    "intro 2s, hold 15s, tail 3s, "
    "in the style of Jonny Greenwood Phantom Thread \"House of Woodcock\" sustained chamber-string ostinato "
    "and There Will Be Blood \"Open Spaces\" quiet sustained string drone "
    "and There Will Be Blood \"Future Markets\" minor-key restraint, "
    "no vocals no lyrics no choir no singing"
)

# C — Calexico Sonoran Americana — geographic AZ-specific, Chandler dusk lone rider
VARIANT_C_PROMPT = (
    "Cinematic minimalist underscore bed, "
    "sustained warm acoustic guitar drone with sparse repeating fingerpicked figure "
    "and distant faint solo trumpet whispered note motif and low desert pad layered underneath "
    "and faint brushed-snare pulse texture, "
    "Sonoran-desert AZ-suburban lone-rider dusk register, "
    "Tex-Mex restraint without cliche, dignified working-class vindication, "
    f"{ANTI_FADEOUT}, underscore bed for voiceover, "
    "intro 2s, hold 15s, tail 3s, "
    "in the style of Calexico \"Crystal Frontier\" sustained acoustic + trumpet desert restraint "
    "and Calexico \"Across the Wire\" lone-rider Sonoran ambiance "
    "and Calexico \"Convict Pool\" sparse Americana low-end discipline, "
    "no vocals no lyrics no choir no singing"
)

# D — Daniel Hart (A Ghost Story) folk-determined — warmer Americana, same arc
VARIANT_D_PROMPT = (
    "Cinematic minimalist underscore bed, "
    "sustained warm string pad in minor key with slow repeating fingerpicked folk guitar figure "
    "and faint solo violin counterline and warm low-end pulse layered underneath, "
    "folk-determined dignified vindication and quiet documentary-truth-emerging weight, "
    "Americana lone-rider warmth without sentimentality, "
    f"{ANTI_FADEOUT}, underscore bed for voiceover, "
    "intro 2s, hold 15s, tail 3s, "
    "in the style of Daniel Hart A Ghost Story \"Safe Safe Safe\" sustained string pad and folk-guitar figure "
    "and Daniel Hart The Green Knight \"Yet I Am Here\" warm low-end Americana restraint "
    "and Daniel Hart A Ghost Story \"I Get Overwhelmed\" dignified folk-determined arc, "
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
        asyncio.create_task(generate_one("A_cave_ellis_jesse_sustained", VARIANT_A_PROMPT)),
        asyncio.create_task(generate_one("B_greenwood_pta_restraint", VARIANT_B_PROMPT)),
        asyncio.create_task(generate_one("C_calexico_sonoran", VARIANT_C_PROMPT)),
        asyncio.create_task(generate_one("D_hart_folk_determined", VARIANT_D_PROMPT)),
    ]
    await asyncio.gather(*tasks)
    print("\nAll 4 M3-V4 Ty music variants generated. A / B / C / D — pick the winner against the VO.")


if __name__ == "__main__":
    asyncio.run(main())

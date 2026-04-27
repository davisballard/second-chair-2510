"""Generate iPhone vibration SFX for the Diana S5 missed-call → incoming-call clip.

Usage:
    python3 generate_sfx_iphone_vibration.py <path_to_video_clip>

Workflow:
1. Take the local 5s Kling 3.0 clip (missed calls → incoming call transition)
2. Upload to fal storage to get a public URL
3. Run MMAudio v2 against the URL — it auto-syncs SFX to visible motion
4. Download the resulting SFX-augmented video / audio file
5. Davis combines with VO + music in CapCut

iPhone "Default" call vibration pattern: ~0.35s buzz → ~0.1s pause → ~0.35s buzz
→ ~2s pause → repeat. Deep low bass mechanical buzz.

The visible phone-buzz jolts in the video (one at the 1.5s transition, plus
small continuous micro-shake during incoming-call phase) will guide MMAudio's
synchronization automatically — that's the whole point of using MMAudio over
a generic SFX generator.
"""
import asyncio
import os
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

# iPhone Default call vibration pattern, tightly scoped
PROMPT = (
    "iPhone vibration sound only, classic iOS default call vibration pattern, "
    "two short staccato vibration buzzes back to back followed by a brief pause "
    "then repeating, deep low bass mechanical buzz, loud and clear, "
    "recorded close to the phone, "
    "NO ambient room tone, NO music, NO voices, NO breathing, NO kitchen sounds, "
    "ONLY the iPhone vibration buzz"
)


async def generate(video_path: Path) -> Path:
    if not video_path.exists():
        raise FileNotFoundError(f"Video not found: {video_path}")

    print(f"[1/3] Uploading {video_path.name} to fal storage...")
    video_url = await fal_client.upload_file_async(str(video_path))
    print(f"      [OK] Uploaded: {video_url[:60]}...")

    print(f"\n[2/3] Running MMAudio v2 — auto-syncing iPhone vibration SFX to video motion...")
    print(f"      Prompt: {PROMPT[:80]}...")
    handler = await fal_client.submit_async(
        "fal-ai/mmaudio-v2",
        arguments={
            "video_url": video_url,
            "prompt": PROMPT,
        },
    )
    result = await handler.get()

    # MMAudio returns a video with audio attached, OR just an audio track
    # Check both response shapes
    if "video" in result:
        out_url = result["video"]["url"]
        suffix = ".mp4"
    elif "audio" in result:
        out_url = result["audio"]["url"]
        suffix = ".mp3"
    else:
        raise RuntimeError(f"Unexpected MMAudio response: {result}")

    print(f"      [OK] Generated: {out_url[:60]}...")

    print(f"\n[3/3] Downloading...")
    out_path = OUT_DIR / f"sfx_iphone_vibration_synced{suffix}"
    urllib.request.urlretrieve(out_url, out_path)
    print(f"      [OK] Saved: {out_path}")
    return out_path


async def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 generate_sfx_iphone_vibration.py <path_to_video_clip>")
        sys.exit(1)
    video_path = Path(sys.argv[1]).expanduser().resolve()
    await generate(video_path)


if __name__ == "__main__":
    asyncio.run(main())

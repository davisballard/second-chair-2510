#!/usr/bin/env python3
"""
DMA → Market global rename script for Second Chair.

Run from the SC root: python3 _tools/dma_to_market_rename.py [--dry-run] [--phase N]

Applies smart find/replace with Nielsen carve-outs. Does NOT do file renames
(those happen via git mv elsewhere — see plan).

Skip list defined inline. Phases defined inline.
"""
import argparse
import re
import sys
from pathlib import Path

SC_ROOT = Path(__file__).resolve().parent.parent  # Second_Chair/

# Files/folders to NEVER touch (per Davis 2026-04-23 directive)
SKIP_PATHS = {
    # Jacoby (entire prospect package — skip)
    "22_Outreach/07_Prospects/Jacoby_Meyers",
    # WCTL signed/sent client deliverables
    "23_Clients/West_Coast_Trial_Lawyers/WCTL_Arizona_Pilot_Proposal_Client_Facing.md",
    "23_Clients/West_Coast_Trial_Lawyers/WCTL_Arizona_Pilot_Proposal.md",
    "23_Clients/West_Coast_Trial_Lawyers/WCTL_Client_Proposal.md",
    "23_Clients/West_Coast_Trial_Lawyers/In_Depth/DMA_Pricing_Table_Client_Facing.md",
    # Tofer — signed agreement and invoice (legal/financial docs already executed)
    "23_Clients/Tofer_and_Associates/Tofer_Service_Agreement.md",
    "23_Clients/Tofer_and_Associates/Tofer_Invoice_001.md",
    # Archive (stale)
    "00_Archive",
    # Tooling, dependencies
    "24_Document_Templates/.venv",
    "_tools",  # this script itself
    # The framework's own DMA reference (intentionally about Nielsen)
    "04_Audience/Geo_Framework/Cross_State_DMA_Reference.md",
}

# File extensions to process
ALLOWED_EXTS = {".md", ".py", ".csv", ".txt", ".json", ".yaml", ".yml"}

# Carve-out patterns — these phrases stay as-is.
# We protect them with placeholders before find/replace, restore after.
CARVE_OUTS = [
    # Nielsen-product references — must NOT become "Nielsen Market"
    (re.compile(r"\bNielsen DMAs\b"), "{{N_DMAS}}"),
    (re.compile(r"\bNielsen DMA\b"), "{{N_DMA}}"),
    (re.compile(r"\bNielsen's DMAs\b"), "{{N_S_DMAS}}"),
    (re.compile(r"\bNielsen's DMA\b"), "{{N_S_DMA}}"),
    (re.compile(r"\bNielsen ®DMA®"), "{{N_RDMA}}"),
    # Nielsen count references (210 is Nielsen's universe, not ours)
    (re.compile(r"\b210 DMAs\b"), "{{N_210_DMAS}}"),
    (re.compile(r"\b210 Nielsen DMAs\b"), "{{N_210_NDMAS}}"),
    # The framework file name itself
    (re.compile(r"Cross_State_DMA_Reference"), "{{CSDR_FILE}}"),
    (re.compile(r"DMA_Comparison_AZ_vs_WA\.md"), "{{WCTL_DMA_AZWA}}"),  # placeholder for renamed file
    (re.compile(r"DMA_Selection_Full_Analysis\.md"), "{{WCTL_DMA_SFA}}"),  # placeholder for renamed file
]

# Restoration map (placeholders back to original)
RESTORE = {
    "{{N_DMAS}}": "Nielsen DMAs",
    "{{N_DMA}}": "Nielsen DMA",
    "{{N_S_DMAS}}": "Nielsen's DMAs",
    "{{N_S_DMA}}": "Nielsen's DMA",
    "{{N_RDMA}}": "Nielsen ®DMA®",
    "{{N_210_DMAS}}": "210 DMAs",
    "{{N_210_NDMAS}}": "210 Nielsen DMAs",
    "{{CSDR_FILE}}": "Cross_State_DMA_Reference",
    "{{WCTL_DMA_AZWA}}": "Market_Comparison_AZ_vs_WA.md",  # post-rename name
    "{{WCTL_DMA_SFA}}": "Market_Selection_Full_Analysis.md",  # post-rename name
}

# Replacement rules (after carve-out protection)
REPLACEMENTS = [
    # Filenames: "DMA_*.md" → "Market_*.md" — handled by separate git mv calls,
    # but if we see a stale reference inside a file, it should match new name.
    (re.compile(r"DMA_Ranked_List"), "Market_Ranked_List"),
    (re.compile(r"DMA_Baseline_Pricing_Framework"), "Market_Baseline_Pricing_Framework"),
    (re.compile(r"Top_10_DMA_Targets"), "Top_10_Market_Targets"),
    (re.compile(r"Why_100_Leads_Per_DMA"), "Why_100_Leads_Per_Market"),
    (re.compile(r"08_DMA_Prospect_Lists"), "08_Market_Prospect_Lists"),
    (re.compile(r"03_DMA_Analysis"), "03_Market_Analysis"),
    # Count update: SC's "121 DMAs" → "109 Markets" (NOT Nielsen's 210)
    (re.compile(r"\b121 DMAs\b"), "109 Markets"),
    (re.compile(r"\b121 viable DMAs\b"), "109 viable Markets"),
    (re.compile(r"\b121-DMA\b"), "109-Market"),
    # Hyphenated forms
    (re.compile(r"\bDMA-based\b"), "Market-based"),
    (re.compile(r"\bDMA-shaped\b"), "Market-shaped"),
    (re.compile(r"\bDMA-level\b"), "Market-level"),
    (re.compile(r"\bDMA-by-DMA\b"), "Market-by-Market"),
    (re.compile(r"\bper-DMA\b"), "per-Market"),
    (re.compile(r"\bsub-DMA\b"), "sub-Market"),
    (re.compile(r"\bcross-DMA\b"), "cross-Market"),
    # Generic "DMA" → "Market" (caught LAST, only what carve-outs missed)
    # Only match standalone DMA, not part of bigger word
    (re.compile(r"\bDMAs\b"), "Markets"),
    (re.compile(r"\bDMA\b"), "Market"),
    # CSV/code column names (lowercase)
    (re.compile(r"\bdma_origin\b"), "nielsen_dma_origin"),
    # Don't replace "dma" lowercase elsewhere — too risky
]


def is_skipped(path: Path) -> bool:
    """Check if path is in skip list."""
    rel = path.relative_to(SC_ROOT).as_posix()
    for skip in SKIP_PATHS:
        if rel == skip or rel.startswith(skip + "/"):
            return True
    return False


def transform(text: str) -> tuple[str, int]:
    """Apply carve-outs, replacements, restore. Return (new_text, change_count)."""
    original = text
    # Protect carve-outs
    for pattern, placeholder in CARVE_OUTS:
        text = pattern.sub(placeholder, text)
    # Apply replacements
    changes = 0
    for pattern, repl in REPLACEMENTS:
        new_text, n = pattern.subn(repl, text)
        if n > 0:
            changes += n
            text = new_text
    # Restore carve-outs
    for placeholder, original_phrase in RESTORE.items():
        text = text.replace(placeholder, original_phrase)
    # Did anything actually change?
    if text == original:
        return original, 0
    return text, changes


def find_files(root: Path, restrict_to: list[str] | None = None) -> list[Path]:
    """Find all files matching ALLOWED_EXTS, respecting skip list."""
    files = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in ALLOWED_EXTS:
            continue
        if is_skipped(path):
            continue
        if restrict_to:
            rel = path.relative_to(SC_ROOT).as_posix()
            if not any(rel.startswith(prefix) for prefix in restrict_to):
                continue
        files.append(path)
    return files


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Show changes without writing")
    parser.add_argument("--paths", nargs="*", help="Restrict to specific path prefixes (relative to SC root)")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    files = find_files(SC_ROOT, restrict_to=args.paths)
    print(f"Scanning {len(files)} files (skip-list applied)...")
    print(f"Mode: {'DRY-RUN' if args.dry_run else 'WRITE'}")
    print()

    total_files_changed = 0
    total_changes = 0
    files_changed = []

    for path in files:
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            print(f"SKIP (not UTF-8): {path.relative_to(SC_ROOT)}")
            continue
        new_content, n_changes = transform(content)
        if n_changes > 0:
            total_files_changed += 1
            total_changes += n_changes
            files_changed.append((path.relative_to(SC_ROOT), n_changes))
            if not args.dry_run:
                path.write_text(new_content, encoding="utf-8")
            if args.verbose:
                print(f"  {path.relative_to(SC_ROOT)}: {n_changes} changes")

    print()
    print(f"Files changed: {total_files_changed}")
    print(f"Total replacements: {total_changes}")
    if args.dry_run:
        print()
        print("DRY-RUN — no files written. Top 20 files by change count:")
        for rel, n in sorted(files_changed, key=lambda x: -x[1])[:20]:
            print(f"  {n:5}  {rel}")


if __name__ == "__main__":
    main()

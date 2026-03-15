#!/usr/bin/env python3
"""
Keyword Search CLI Tool
-----------------------
Searches for keyword occurrences in large text files with real-time statistics.

Usage:
  python keyword_tool.py                     # interactive mode
  python keyword_tool.py --config config.md  # load file paths from Markdown config
  python keyword_tool.py file1.txt file2.txt # load file paths from CLI args
"""

import argparse
import os
import re
import sys
from collections import defaultdict


# ── ANSI colour helpers ──────────────────────────────────────────────────────

RESET  = "\033[0m"
BOLD   = "\033[1m"
CYAN   = "\033[96m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
DIM    = "\033[2m"


def _c(text: str, *codes: str) -> str:
    """Wrap text in ANSI escape codes (stripped when stdout is not a tty)."""
    if not sys.stdout.isatty():
        return text
    return "".join(codes) + text + RESET


# ── Config / file loading ────────────────────────────────────────────────────

def parse_markdown_config(path: str) -> list[str]:
    """
    Extract file paths from a Markdown config file.

    Recognised patterns:
      - Bullet items:  - /some/path.txt
      - Numbered items: 1. /some/path.txt
      - Bare lines that look like file paths (no leading markup)
      - Code-block lines: `path.txt`
    """
    paths: list[str] = []
    try:
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                line = line.rstrip()
                # bullet / numbered list item
                m = re.match(r"^\s*(?:[-*+]|\d+\.)\s+(.+)$", line)
                if m:
                    candidate = m.group(1).strip().strip("`").strip("'\"")
                    paths.append(candidate)
                    continue
                # backtick-wrapped inline code
                m = re.match(r"^\s*`([^`]+)`\s*$", line)
                if m:
                    paths.append(m.group(1).strip())
                    continue
                # bare line that looks like a path (contains / or \ or ends with extension)
                stripped = line.strip()
                if stripped and not stripped.startswith("#") and (
                    "/" in stripped or "\\" in stripped or "." in stripped
                ):
                    paths.append(stripped)
    except OSError as exc:
        print(_c(f"  Error reading config '{path}': {exc}", RED), file=sys.stderr)
    return paths


def validate_files(raw_paths: list[str]) -> tuple[list[str], list[str]]:
    """Return (valid_paths, invalid_paths)."""
    valid, invalid = [], []
    for p in raw_paths:
        if os.path.isfile(p):
            valid.append(os.path.abspath(p))
        else:
            invalid.append(p)
    return valid, invalid


def prompt_for_files() -> list[str]:
    """Interactively ask the user to enter file paths one by one."""
    print()
    print(_c("  No files specified. Enter file paths to analyse.", CYAN))
    print(_c("  Type '/done' when finished, or '/quit' to exit.", DIM))
    print()
    raw: list[str] = []
    while True:
        try:
            entry = input(_c("  File path: ", BOLD)).strip()
        except (EOFError, KeyboardInterrupt):
            print()
            sys.exit(0)

        if entry.lower() == "/quit":
            print(_c("\n  Goodbye!\n", GREEN))
            sys.exit(0)
        if entry.lower() == "/done":
            break
        if entry:
            raw.append(entry)

    return raw


# ── Text indexing ────────────────────────────────────────────────────────────

def build_index(file_paths: list[str]) -> dict[str, dict[str, int]]:
    """
    Build a word-frequency index for each file.

    Returns:
      { filepath: { word_lower: count, … }, … }
    """
    index: dict[str, dict[str, int]] = {}
    total = len(file_paths)
    for i, path in enumerate(file_paths, 1):
        print(_c(f"  [{i}/{total}] Indexing: {path}", DIM))
        freq: dict[str, int] = defaultdict(int)
        try:
            with open(path, encoding="utf-8", errors="replace") as fh:
                for line in fh:
                    for word in re.findall(r"[a-zA-Z0-9'_-]+", line):
                        freq[word.lower()] += 1
        except OSError as exc:
            print(_c(f"  Warning – could not read '{path}': {exc}", YELLOW),
                  file=sys.stderr)
            continue
        index[path] = dict(freq)
    return index


# ── Statistics display ───────────────────────────────────────────────────────

def word_stats(keyword: str, index: dict[str, dict[str, int]]) -> None:
    """Print per-file and aggregate occurrence counts for *keyword*."""
    kw = keyword.lower()
    total = 0
    results: list[tuple[str, int]] = []

    for path, freq in index.items():
        count = freq.get(kw, 0)
        results.append((path, count))
        total += count

    # Sort by count descending
    results.sort(key=lambda x: x[1], reverse=True)

    print()
    print(_c(f'  Results for "{keyword}"', BOLD))
    print(_c("  " + "─" * 56, DIM))

    any_found = False
    for path, count in results:
        filename = os.path.basename(path)
        bar = _build_bar(count, max(r[1] for r in results) if results else 1)
        if count > 0:
            any_found = True
            print(
                f"  {_c(filename, CYAN):<40s}  "
                f"{_c(str(count).rjust(6), GREEN)}  {bar}"
            )
        else:
            print(f"  {_c(filename, DIM):<40s}  {_c('     0', DIM)}")

    print(_c("  " + "─" * 56, DIM))
    colour = GREEN if any_found else YELLOW
    print(f"  {_c('Total occurrences:', BOLD)} {_c(str(total), colour)}")
    print()


def _build_bar(count: int, max_count: int, width: int = 20) -> str:
    """Return a simple ASCII bar proportional to count/max_count."""
    if max_count == 0:
        return ""
    filled = round((count / max_count) * width)
    bar = "█" * filled + "░" * (width - filled)
    return _c(bar, CYAN) if count > 0 else _c(bar, DIM)


# ── Main interactive loop ────────────────────────────────────────────────────

def keyword_loop(index: dict[str, dict[str, int]]) -> None:
    """Enter an infinite keyword-search loop until the user types /quit."""
    file_count = len(index)
    total_words = sum(sum(f.values()) for f in index.values())

    print()
    print(_c("  ┌─────────────────────────────────────────┐", CYAN))
    print(_c("  │   Keyword Search Tool  — ready          │", CYAN))
    print(_c("  └─────────────────────────────────────────┘", CYAN))
    print(f"  Files loaded : {_c(str(file_count), GREEN)}")
    print(f"  Total words  : {_c(f'{total_words:,}', GREEN)}")
    print(_c("  Type a keyword to search, or /quit to exit.", DIM))
    print()

    while True:
        try:
            keyword = input(_c("  Keyword: ", BOLD + CYAN)).strip()
        except (EOFError, KeyboardInterrupt):
            print()
            keyword = "/quit"

        if not keyword:
            continue

        if keyword.lower() == "/quit":
            print(_c("\n  Goodbye!\n", GREEN))
            break

        if len(keyword) < 1:
            print(_c("  Please enter at least one character.", YELLOW))
            continue

        word_stats(keyword, index)


# ── Entry point ──────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        prog="keyword_tool",
        description="Real-time keyword occurrence stats for large text files.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python keyword_tool.py                      # interactive mode\n"
            "  python keyword_tool.py --config config.md   # Markdown config\n"
            "  python keyword_tool.py file1.txt file2.txt  # direct paths\n"
        ),
    )
    parser.add_argument(
        "--config", "-c",
        metavar="CONFIG.md",
        help="Markdown file listing target file paths (one per bullet / line).",
    )
    parser.add_argument(
        "files",
        nargs="*",
        metavar="FILE",
        help="One or more text files to analyse.",
    )
    args = parser.parse_args()

    # ── Collect raw paths ────────────────────────────────────────────────────
    raw_paths: list[str] = []

    if args.config:
        if not os.path.isfile(args.config):
            print(_c(f"  Config file not found: '{args.config}'", RED), file=sys.stderr)
            sys.exit(1)
        print(_c(f"\n  Loading paths from config: {args.config}", CYAN))
        raw_paths.extend(parse_markdown_config(args.config))

    if args.files:
        raw_paths.extend(args.files)

    # ── Interactive path prompt if nothing provided ──────────────────────────
    if not raw_paths:
        raw_paths = prompt_for_files()

    # ── Validate ─────────────────────────────────────────────────────────────
    valid, invalid = validate_files(raw_paths)

    if invalid:
        print()
        print(_c("  The following paths could not be found:", YELLOW))
        for p in invalid:
            print(_c(f"    ✗ {p}", RED))

    if not valid:
        print(_c("\n  No valid files to analyse. Exiting.\n", RED), file=sys.stderr)
        sys.exit(1)

    print()
    print(_c("  Files to analyse:", BOLD))
    for p in valid:
        print(_c(f"    ✓ {p}", GREEN))

    # ── Build index ───────────────────────────────────────────────────────────
    print()
    index = build_index(valid)

    if not index:
        print(_c("\n  No files could be indexed. Exiting.\n", RED), file=sys.stderr)
        sys.exit(1)

    # ── Search loop ───────────────────────────────────────────────────────────
    keyword_loop(index)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
AOC Scaffolding Tool
Usage:
    python gen.py --year <year> --day <day> --lang <lang>

Supported languages: python, rust

The script will:
  1. Fetch puzzle input from AoC (requires AOC_SESSION env var)
  2. Create the directory: <lang>/<year>/day<day>/
  3. Scaffold language-specific solution files with Part 1 / Part 2 structure
"""

import os
import sys
import shutil
import argparse
from pathlib import Path

SUPPORTED_LANGS = ["python", "rust"]

# Resolve paths relative to this script's location (tools/)
TOOLS_DIR = Path(__file__).parent.resolve()
ROOT_DIR = TOOLS_DIR.parent


def main():
    args = parse_args()
    year, day, lang = args.year, args.day, args.lang

    dest_dir = ROOT_DIR / lang / str(year) / f"day{day}"

    print(f"[AOC] Scaffolding {lang.capitalize()} solution for {year} Day {day}")
    print(f"[AOC] Destination: {dest_dir}")

    dest_dir.mkdir(parents=True, exist_ok=True)

    # Fetch input
    input_path = dest_dir / "input.txt"
    if input_path.exists():
        print(f"[AOC] input.txt already exists, skipping fetch.")
    else:
        fetch_input(year, day, input_path)

    # Scaffold solution files
    scaffold(lang, day, dest_dir)

    print(f"[AOC] Done! Open {dest_dir} to get started.")


def parse_args():
    parser = argparse.ArgumentParser(description="AOC scaffolding tool")
    parser.add_argument("--year", "-y", type=int, required=True, help="Puzzle year")
    parser.add_argument("--day",  "-d", type=int, required=True, help="Puzzle day")
    parser.add_argument(
        "--lang", "-l",
        type=str,
        required=True,
        choices=SUPPORTED_LANGS,
        help=f"Language to scaffold ({', '.join(SUPPORTED_LANGS)})"
    )
    return parser.parse_args()


def fetch_input(year: int, day: int, dest: Path):
    try:
        from aocd import get_data
    except ImportError:
        print("[AOC] Warning: 'aocd' not installed. Skipping input fetch.")
        print("       Install with: pip install advent-of-code-data")
        dest.touch()
        return

    env_var = "AOC_SESSION"
    if not os.getenv(env_var):
        print(f"[AOC] Warning: ${env_var} not set. Skipping input fetch.")
        dest.touch()
        return

    print(f"[AOC] Fetching input for {year} day {day}...")
    data = get_data(day=day, year=year)
    dest.write_text(data, encoding="utf-8")
    print(f"[AOC] Input saved to {dest}")


def scaffold(lang: str, day: int, dest_dir: Path):
    template_dir = TOOLS_DIR / "templates" / lang

    if not template_dir.exists():
        print(f"[AOC] Error: No template found for language '{lang}' at {template_dir}")
        sys.exit(1)

    if lang == "python":
        scaffold_python(template_dir, dest_dir)
    elif lang == "rust":
        scaffold_rust(template_dir, dest_dir, day)
    else:
        print(f"[AOC] Unknown language: {lang}")
        sys.exit(1)


def scaffold_python(template_dir: Path, dest_dir: Path):
    solution_dest = dest_dir / "solution.py"
    if solution_dest.exists():
        print(f"[AOC] solution.py already exists, skipping.")
        return
    shutil.copy(template_dir / "solution.py", solution_dest)
    print(f"[AOC] Created solution.py")


def scaffold_rust(template_dir: Path, dest_dir: Path, day: int):
    # Create src/ dir
    src_dir = dest_dir / "src"
    src_dir.mkdir(exist_ok=True)

    # main.rs
    main_dest = src_dir / "main.rs"
    if not main_dest.exists():
        shutil.copy(template_dir / "src" / "main.rs", main_dest)
        print(f"[AOC] Created src/main.rs")
    else:
        print(f"[AOC] src/main.rs already exists, skipping.")

    # Cargo.toml (with day name substituted)
    cargo_dest = dest_dir / "Cargo.toml"
    if not cargo_dest.exists():
        cargo_template = (template_dir / "Cargo.toml").read_text(encoding="utf-8")
        cargo_content = cargo_template.replace("{{DAY}}", str(day))
        cargo_dest.write_text(cargo_content, encoding="utf-8")
        print(f"[AOC] Created Cargo.toml")
    else:
        print(f"[AOC] Cargo.toml already exists, skipping.")


if __name__ == "__main__":
    main()

"""
Taxonomy auto-sync script.

Scans problem READMEs for `pattern:` metadata and updates
the Pattern Taxonomy table in README.md accordingly.

Features:
- Idempotent (safe to run multiple times)
- Adds missing problem links
- Creates new pattern rows if needed
"""

from __future__ import annotations

import logging
import re
import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Tuple

# ===== CONFIG =====
TABLE_FILE = Path("README.md")
PROBLEMS_DIR = Path("problems")
PATTERN_MARKER = "### **Documented Patterns**"

DEFAULT_CORE_PRINCIPLE = "—"
DEFAULT_NOTES_LINK = "[🚧 Coming soon](patterns/two_pointers)"

logging.basicConfig(level=logging.INFO, format="%(message)s")


# ===== DOMAIN MODEL =====
@dataclass(frozen=True)
class ProblemEntry:
    """Represents a problem mapped to a pattern."""

    title: str
    rel_path: str
    pattern: str


# ===== FILE HELPERS =====
def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


# ===== PARSING HELPERS =====
def extract_pattern(md: str) -> Optional[str]:
    match = re.search(r"(?im)^\s*pattern\s*:\s*(.+?)\s*$", md)
    return match.group(1).strip() if match else None


def extract_title(folder_name: str, md: str) -> str:
    match = re.search(r"(?m)^\s*#\s+(.+?)\s*$", md)
    if match:
        return match.group(1).strip()
    return folder_name.replace("-", " ").title()


def build_link(title: str, rel_path: str) -> str:
    return f"[{title}]({rel_path}/)"


# ===== TABLE PARSING =====
def parse_table_region(full_md: str) -> Tuple[int, int]:
    marker_idx = full_md.find(PATTERN_MARKER)
    if marker_idx == -1:
        raise RuntimeError("Pattern taxonomy marker not found")

    after_marker = full_md[marker_idx:]
    header_match = re.search(r"(?m)^\|\s*Pattern Category\s*\|.*$", after_marker)
    if not header_match:
        raise RuntimeError("Table header not found")

    table_start = marker_idx + header_match.start()

    lines = full_md[table_start:].splitlines(keepends=True)
    end_offset = 0
    seen_row = False

    for line in lines:
        if line.lstrip().startswith("|"):
            seen_row = True
            end_offset += len(line)
            continue
        if seen_row:
            break
        end_offset += len(line)

    table_end = table_start + end_offset
    return table_start, table_end


def split_lines(table_md: str) -> List[str]:
    return [ln.rstrip("\n") for ln in table_md.splitlines() if ln.strip()]


def join_lines(lines: List[str]) -> str:
    return "\n".join(lines) + "\n"


def is_separator(line: str) -> bool:
    return bool(re.match(r"^\|\s*:?-{2,}", line.strip()))


def parse_cells(line: str) -> List[str]:
    raw = line.strip().strip("|")
    return [c.strip() for c in raw.split("|")]


def format_row(cells: List[str]) -> str:
    return "| " + " | ".join(cells) + " |"


# ===== TABLE MANIPULATION =====
def find_pattern_row(lines: List[str], pattern: str) -> Optional[int]:
    for i, line in enumerate(lines):
        if is_separator(line):
            continue
        cells = parse_cells(line)
        if not cells:
            continue
        if re.fullmatch(rf"\*\*{re.escape(pattern)}\*\*", cells[0]):
            return i
    return None


def ensure_pattern_row(lines: List[str], pattern: str) -> int:
    idx = find_pattern_row(lines, pattern)
    if idx is not None:
        return idx

    sep_idx = next(i for i, ln in enumerate(lines) if is_separator(ln))

    new_row = format_row(
        [
            f"**{pattern}**",
            DEFAULT_CORE_PRINCIPLE,
            "",
            DEFAULT_NOTES_LINK,
        ]
    )

    insert_at = sep_idx + 1
    lines.insert(insert_at, new_row)
    return insert_at


def add_problem_link(row: str, link: str) -> str:
    cells = parse_cells(row)
    if len(cells) < 4:
        return row

    signature = cells[2]
    if link in signature:
        return row

    cells[2] = link if not signature else signature + " • " + link
    return format_row(cells)


# ===== PROBLEM SCANNING =====
def collect_problem_entries() -> List[ProblemEntry]:
    entries: List[ProblemEntry] = []

    if not PROBLEMS_DIR.exists():
        return entries

    for folder in sorted(PROBLEMS_DIR.iterdir()):
        if not folder.is_dir():
            continue

        readme = folder / "README.md"
        if not readme.exists():
            continue

        md = read_text(readme)
        pattern = extract_pattern(md)
        if not pattern:
            continue

        title = extract_title(folder.name, md)
        entries.append(
            ProblemEntry(
                title=title,
                rel_path=str(folder).replace("\\", "/"),
                pattern=pattern,
            )
        )

    return entries


# ===== PIPELINE =====
def update_taxonomy(dry_run: bool = False) -> bool:
    full_md = read_text(TABLE_FILE)
    start, end = parse_table_region(full_md)

    table_lines = split_lines(full_md[start:end])
    entries = collect_problem_entries()

    if not entries:
        logging.info("No pattern metadata found.")
        return False

    changed = False
    changes = []

    for entry in entries:
        row_idx = ensure_pattern_row(table_lines, entry.pattern)
        link = build_link(entry.title, entry.rel_path)

        new_row = add_problem_link(table_lines[row_idx], link)
        if new_row != table_lines[row_idx]:
            changes.append(
                f"Added problem '{entry.title}' -> pattern '{entry.pattern}'"
            )
            table_lines[row_idx] = new_row
            changed = True

    if not changed:
        return False

    new_table = join_lines(table_lines)
    updated = full_md[:start] + new_table + full_md[end:]
    if dry_run:
        logging.info("🧪 Dry run — preview of changes:\n")
        for c in changes:
            logging.info(f"  + {c}")
        return True

    write_text(TABLE_FILE, updated)
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync taxonomy table")
    parser.add_argument(
        "--dry-run", action="store_true", help="Preview changes without writing"
    )
    args = parser.parse_args()

    if update_taxonomy(dry_run=args.dry_run):
        logging.info("✔ Changes detected")
    else:
        logging.info("✔ Already up to date")


if __name__ == "__main__":
    main()

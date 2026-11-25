"""Entry for make.fun competition: u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3.

Running this program writes the entry line to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

OPENING = "Every night the streetlight outside my window practices "
MIDDLE = "being the moon for an audience of one moth, and the moth, "
LANDING = "every night, believes it completely."

ENTRY = OPENING + MIDDLE + LANDING


def write_entry(text: str, path: Path) -> None:
    """Write *text* to *path* as UTF-8, with no trailing newline added."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    """Write the entry line to the fixed output path."""
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()

from pathlib import Path
from datetime import datetime

NOTES_DIR = Path("notes")
NOTES_DIR.mkdir(exist_ok=True)


def save_note(title: str, content: str) -> Path:
    """
    Save a note as a Markdown file.
    """
    safe_title = "".join(
        c for c in title if c.isalnum() or c in (" ", "-", "_")
    ).strip()

    if not safe_title:
        safe_title = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"{safe_title}.md"
    filepath = NOTES_DIR / filename

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(f"# {title}\n\n{content.rstrip()}\n")

    return filepath

    
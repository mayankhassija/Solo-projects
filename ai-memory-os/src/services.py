from pathlib import Path

from src.storage import save_note

def create_note (title: str, content: str) -> Path:
    """
    Create a new note.

    Future validation and business logic will go here.

    """
    return save_note(title,content)

    
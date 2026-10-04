# File handling module

import json
import os

from config import DATA_FILE


def load_complaints():
    """Read complaints from JSON file."""

    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return []


def save_complaints(complaints):
    """Save complaints to JSON file."""

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(complaints, file, indent=4)
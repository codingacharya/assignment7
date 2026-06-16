# utils/text_cleaner.py

import re


def clean_text(text):
    """
    Clean complaint text.
    """

    if not text:
        return ""

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Remove special characters except punctuation
    text = re.sub(
        r"[^a-zA-Z0-9.,!?@\- ]",
        "",
        text
    )

    return text.strip()


def normalize_text(text):
    """
    Convert text to lowercase.
    """

    return text.lower().strip()


def remove_extra_lines(text):
    """
    Remove unnecessary blank lines.
    """

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    return "\n".join(lines)
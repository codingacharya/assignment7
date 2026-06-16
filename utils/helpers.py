# utils/helpers.py

from datetime import datetime


def current_timestamp():
    """
    Return current date and time.
    """

    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


def truncate_text(
    text,
    max_length=100
):
    """
    Truncate long text.
    """

    if len(text) <= max_length:
        return text

    return text[:max_length] + "..."


def format_category(category):
    """
    Format category string.
    """

    return category.title()


def format_priority(priority):
    """
    Format priority string.
    """

    return priority.upper()
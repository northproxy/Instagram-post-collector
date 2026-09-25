"""Filename generation utilities for archived Instagram posts."""

import re
from datetime import date

from pathlib import Path

def make_metadata_path(
    published_date: date,
    caption: str,
) -> Path:
    """Create the relative archive path for normalized post metadata."""

    return make_archive_directory(published_date) / make_metadata_filename(
        published_date,
        caption,
    )


def make_media_path(
    published_date: date,
    caption: str,
    position: int,
    extension: str,
) -> Path:
    """Create the relative archive path for one media item."""

    return make_archive_directory(published_date) / make_media_filename(
        published_date,
        caption,
        position,
        extension,
    )


def make_archive_directory(published_date: date) -> Path:
    """Create the relative archive directory for a publication date."""

    return Path("archive") / f"{published_date:%Y}" / f"{published_date:%m}"


def make_caption_prefix(caption: str) -> str:
    """Create a filesystem-friendly prefix from an Instagram caption."""

    caption = caption.strip()

    if not caption:
        return "post"

    # Keep letters, numbers, whitespace, underscores and hyphens.
    caption = "".join(
        char
        for char in caption
        if char.isalnum() or char.isspace() or char in "_-"
    )

    # Normalize whitespace before applying the length limit.
    caption = re.sub(r"\s+", " ", caption).strip()

    if not caption:
        return "post"

    # Use the first 14 normalized characters.
    caption = caption[:14].rstrip()

    # Make the prefix filename-friendly.
    caption = caption.replace(" ", "_")

    return caption or "post"


def make_metadata_filename(published_date: date, caption: str) -> str:
    """Create the archive filename for normalized post metadata."""

    prefix = make_caption_prefix(caption)

    return f"{published_date:%y%m%d}_{prefix}.json"


def make_media_filename(
    published_date: date,
    caption: str,
    position: int,
    extension: str,
) -> str:
    """Create the archive filename for one media item."""

    if position < 1:
        raise ValueError("Media position must be 1 or greater.")

    extension = extension.lstrip(".").lower()

    if not extension:
        raise ValueError("File extension must not be empty.")

    prefix = make_caption_prefix(caption)

    return f"{published_date:%y%m%d}_{prefix}-{position:02d}.{extension}"
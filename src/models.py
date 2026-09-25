"""Domain models for normalized IPcoll metadata."""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Author:
    """Normalized Instagram author metadata."""

    id: str
    username: str

@dataclass
class MediaItem:
    """Normalized metadata for one archived media item."""

    position: int
    filename: str

@dataclass
class MediaItem:
    """Normalized metadata for one archived media item."""

    position: int
    filename: str

    def __post_init__(self):
        if self.position < 1:
            raise ValueError("Media position must be 1 or greater.")

@dataclass
class PostMetadata:
    """Normalized metadata for one archived Instagram post."""

    schema_version: int
    shortcode: str
    source_url: str
    published_at: datetime
    author: Author
    post_type: str
    caption: str
    media: list[MediaItem]

    def __post_init__(self):
    if self.post_type not in {"image", "carousel"}:
        raise ValueError("Post type must be 'image' or 'carousel'.")

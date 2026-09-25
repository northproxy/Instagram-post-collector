"""Tests for normalized IPcoll metadata models."""

from src.models import Author, MediaItem, PostMetadata
from datetime import datetime, timezone

import pytest


def test_author_stores_id_and_username():
    author = Author(
        id="3320679817",
        username="filmarchivaustria",
    )

    assert author.id == "3320679817"
    assert author.username == "filmarchivaustria"

def test_media_item_stores_position_and_filename():
    media = MediaItem(
        position=1,
        filename="260809_Eine_neue_Woch-01.jpg",
    )

    assert media.position == 1
    assert media.filename == "260809_Eine_neue_Woch-01.jpg"

def test_media_item_position_must_be_positive():
    with pytest.raises(
        ValueError,
        match="Media position must be 1 or greater.",
    ):
        MediaItem(
            position=0,
            filename="260809_Eine_neue_Woch-00.jpg",
        )

def test_post_metadata_stores_normalized_post_data():
    author = Author(
        id="3320679817",
        username="filmarchivaustria",
    )

    media = [
        MediaItem(
            position=1,
            filename="260809_Eine_neue_Woch-01.jpg",
        ),
        MediaItem(
            position=2,
            filename="260809_Eine_neue_Woch-02.jpg",
        ),
    ]

    post = PostMetadata(
        schema_version=1,
        shortcode="Db07NdYD_Jx",
        source_url="https://www.instagram.com/p/Db07NdYD_Jx/",
        published_at=datetime(
            2026,
            8,
            9,
            17,
            0,
            14,
            tzinfo=timezone.utc,
        ),
        author=author,
        post_type="carousel",
        caption="Eine neue Woche",
        media=media,
    )

    assert post.schema_version == 1
    assert post.shortcode == "Db07NdYD_Jx"
    assert post.author.username == "filmarchivaustria"
    assert post.media[0].position == 1
    assert post.media[1].filename == "260809_Eine_neue_Woch-02.jpg"

def test_post_type_must_be_supported():
    with pytest.raises(
        ValueError,
        match="Post type must be 'image' or 'carousel'.",
    ):
        PostMetadata(
            schema_version=1,
            shortcode="Db07NdYD_Jx",
            source_url="https://www.instagram.com/p/Db07NdYD_Jx/",
            published_at=datetime(
                2026,
                8,
                9,
                17,
                0,
                14,
                tzinfo=timezone.utc,
            ),
            author=Author(
                id="3320679817",
                username="filmarchivaustria",
            ),
            post_type="video",
            caption="Eine neue Woche",
            media=[
                MediaItem(
                    position=1,
                    filename="260809_Eine_neue_Woch-01.jpg",
                ),
            ],
        )
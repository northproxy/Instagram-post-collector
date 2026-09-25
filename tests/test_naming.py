"""Tests for IPcoll archive filename generation."""

from datetime import date

from pathlib import Path

import pytest

from src.naming import (
    make_archive_directory,
    make_caption_prefix,
    make_media_filename,
    make_media_path,
    make_metadata_filename,
    make_metadata_path,
)

def test_metadata_path():
    assert (
        make_metadata_path(
            date(2026, 8, 9),
            "Eine neue Woche",
        )
        == Path("archive")
        / "2026"
        / "08"
        / "260809_Eine_neue_Woch.json"
    )


def test_media_path():
    assert (
        make_media_path(
            date(2026, 8, 9),
            "Eine neue Woche",
            1,
            "jpg",
        )
        == Path("archive")
        / "2026"
        / "08"
        / "260809_Eine_neue_Woch-01.jpg"
    )

def test_archive_directory():
    assert make_archive_directory(
        date(2026, 8, 9),
    ) == Path("archive") / "2026" / "08"

def test_normal_caption():
    assert make_caption_prefix("Eine neue Woche") == "Eine_neue_Woch"


def test_leading_emoji():
    assert make_caption_prefix("🍿 Kino im Park") == "Kino_im_Park"


def test_special_characters():
    assert make_caption_prefix("Hello!!! World") == "Hello_World"


def test_leading_and_trailing_spaces():
    assert make_caption_prefix("   Sommer Wien   ") == "Sommer_Wien"


def test_empty_caption():
    assert make_caption_prefix("") == "post"


def test_normalization_happens_before_length_limit():
    assert make_caption_prefix("🍿 Eine neue Woche") == "Eine_neue_Woch"


def test_repeated_spaces_do_not_consume_prefix_length():
    assert make_caption_prefix("Eine    neue Woche") == "Eine_neue_Woch"


def test_metadata_filename():
    assert (
        make_metadata_filename(
            date(2026, 8, 9),
            "Eine neue Woche",
        )
        == "260809_Eine_neue_Woch.json"
    )


def test_media_filename():
    assert (
        make_media_filename(
            date(2026, 8, 9),
            "Eine neue Woche",
            1,
            "jpg",
        )
        == "260809_Eine_neue_Woch-01.jpg"
    )


def test_media_filename_normalizes_extension():
    assert (
        make_media_filename(
            date(2026, 8, 9),
            "Eine neue Woche",
            9,
            ".JPG",
        )
        == "260809_Eine_neue_Woch-09.jpg"
    )


def test_media_position_must_be_positive():
    with pytest.raises(
        ValueError,
        match="Media position must be 1 or greater.",
    ):
        make_media_filename(
            date(2026, 8, 9),
            "Eine neue Woche",
            0,
            "jpg",
        )


def test_media_extension_must_not_be_empty():
    with pytest.raises(
        ValueError,
        match="File extension must not be empty.",
    ):
        make_media_filename(
            date(2026, 8, 9),
            "Eine neue Woche",
            1,
            "",
        )
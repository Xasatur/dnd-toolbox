import pytest

from src.core.spellbook import (
    search_by_name,
    filter_by_level,
    filter_by_class,
    filter_by_school,
)


def test_search_by_name():
    result = search_by_name("Fireball")
    assert result is None or isinstance(result, dict)
    if result:
        assert result["name"].lower() == "fireball"


def test_filter_by_level():
    results = filter_by_level("3")
    assert isinstance(results, list)
    assert all(spell["level"] == "3" for spell in results)


def test_filter_by_class():
    results = filter_by_class("wizard")
    assert isinstance(results, list)
    assert all("wizard" in [tag.lower() for tag in spell["tags"]] for spell in results)


def test_filter_by_school():
    results = filter_by_school("evocation")
    assert isinstance(results, list)
    assert all(spell["school"] == "evocation" for spell in results)

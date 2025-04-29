import pytest
from src.core.looter import get_loot_by_rarity

def test_get_loot_valid_rarity():
    result = get_loot_by_rarity("common", 2)
    assert isinstance(result, list)
    assert len(result) <= 2
    assert all(isinstance(name, str) for name in result)

def test_get_loot_invalid_rarity():
    with pytest.raises(ValueError):
        get_loot_by_rarity("mythic", 1)

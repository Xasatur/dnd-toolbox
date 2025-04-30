import pytest

from src.core.combat import load_monsters, MonsterInstance

def test_load_monsters_returns_list():
    monsters = load_monsters()
    assert isinstance(monsters, list)
    assert all(callable(cls) for cls, _ in monsters)
    assert len(monsters) > 0

def test_monster_instance_creation():
    monsters = load_monsters()
    monster_class, name = monsters[0]
    instance = MonsterInstance(monster_class, "test123")
    assert instance.name == monster_class().name
    assert isinstance(instance.actions(), dict)

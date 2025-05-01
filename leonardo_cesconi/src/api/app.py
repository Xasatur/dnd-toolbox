from fastapi import FastAPI, Query
from typing import Optional
from src.core.looter import get_loot_by_rarity
from src.core.spellbook import search_by_name, filter_by_level, filter_by_class, filter_by_school
from src.core.combat import load_monsters

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Willkommen in der DnD Toolbox API!"}


@app.get("/spells")
def get_spells(name: Optional[str] = None, level: Optional[str] = None, klass: Optional[str] = None, school: Optional[str] = None):
    if name:
        spell = search_by_name(name)
        return {"spells": [spell] if spell else []}
    elif level:
        return {"spells": filter_by_level(level)}
    elif klass:
        return {"spells": filter_by_class(klass)}
    elif school:
        return {"spells": filter_by_school(school)}
    else:
        return {"error": "Bitte gib mindestens einen Filterparameter an (name, level, klass, school)."}


@app.get("/loot")
def get_loot(rarity: str = "common", amount: int = 1):
    try:
        items = get_loot_by_rarity(rarity, amount)
        return {"rarity": rarity, "items": items}
    except ValueError as e:
        return {"error": str(e)}


# Monster-Endpoint
@app.get("/monsters")
def get_monsters():
    try:
        monsters = load_monsters()
        return {
            "monsters": [
                {"name": monster_class().name, "icon": monster_class().icon}
                for monster_class, _ in monsters
            ]
        }
    except Exception as e:
        return {"error": str(e)}

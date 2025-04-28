from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Willkommen in der DnD Toolbox API!"}

@app.get("/spells")
def get_spells(name: Optional[str] = Query(None)):
    # Fake Example (wird später ersetzt durch JSON-Parsing)
    if name:
        return {"spells": [f"Zauber gefunden: {name}"]}
    return {"spells": ["Feuerball", "Magie entdecken", "Teleport"]}

@app.get("/loot")
def get_loot(rarity: int = 1, amount: int = 1):
    # Fake Example (wird später mit echter Loot-Liste ersetzt)
    rarities = {1: "gewöhnlich", 2: "selten", 3: "episch"}
    return {"rarity": rarities.get(rarity, "unbekannt"), "items": [f"Gegenstand {i+1}" for i in range(amount)]}

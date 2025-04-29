import random
import os
import json
from dotenv import load_dotenv

load_dotenv()

LOOT_FILE = os.getenv("LOOT_FILE", "data/loot.json")

# Lade Loot-Daten aus JSON
with open(LOOT_FILE, "r", encoding="utf-8") as f:
    loot = json.load(f)

mapping = {1: "common", 2: "uncommon", 3: "rare", 4: "very rare", 5: "legendary"}

def get_loot_by_rarity(rarity: str, count: int) -> list[str]:
    """Draw random loot items from the pool based on rarity."""
    if rarity not in loot:
        raise ValueError(f"Rarity '{rarity}' not found.")
    sampled_items = random.sample(loot[rarity], min(count, len(loot[rarity])))
    return [item["name"] for item in sampled_items]


def start():
    while True:
        try:
            wahl = int(input("Wähle Seltenheit (1=common, 2=uncommon, 3=rare, 4=very rare, 5=legendary, 9=beenden): "))
        except ValueError:
            print("❌ Bitte gib eine gültige Zahl ein.")
            continue

        if wahl == 9:
            print("Looter beendet.")
            break

        if wahl not in mapping:
            print("❌ Ungültige Auswahl.")
            continue

        try:
            anzahl = int(input("Wie viele Gegenstände?: "))
        except ValueError:
            print("❌ Bitte gib eine gültige Zahl ein.")
            continue

        seltenheit = mapping[wahl]

        try:
            item_names = get_loot_by_rarity(seltenheit, anzahl)
        except ValueError as e:
            print(f"⚠️ {e}")
            continue

        print("\n🎁 Du bekommst:")
        for name in item_names:
            print(f'- {name}')

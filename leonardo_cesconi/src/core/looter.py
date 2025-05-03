import random
import os
import json
from dotenv import load_dotenv

load_dotenv()

LOOT_FILE = os.getenv("LOOT_FILE")

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


def start(rarity=None, count=None):
    if rarity and count:
        print("\n🎁 Du bekommst:")
        for item in get_loot_by_rarity(rarity, count):
            print(f"- {item}")
        print("Looter beendet.\n")
        return

    # Interaktiver Modus, falls keine Argumente übergeben wurden
    while True:
        print("Wähle Seltenheit (1=common, 2=uncommon, 3=rare, 4=very rare, 5=legendary, 9=beenden): ", end="")
        auswahl = input()

        if auswahl == "9":
            print("Looter beendet.")
            break

        mapping = {
            "1": "common",
            "2": "uncommon",
            "3": "rare",
            "4": "very rare",
            "5": "legendary"
        }

        if auswahl not in mapping:
            print("Ungültige Eingabe.")
            continue

        rarity = mapping[auswahl]
        count = int(input("Wie viele Gegenstände?: "))

        print("\n🎁 Du bekommst:")
        for item in get_loot_by_rarity(rarity, count):
            print(f"- {item}")

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

        if seltenheit not in loot:
            print(f"⚠️ Keine Gegenstände für Seltenheit '{seltenheit}' gefunden.")
            continue

        item = random.sample(loot[seltenheit], min(anzahl, len(loot[seltenheit])))
        print("\n🎁 Du bekommst:")
        for i in item:
            print(f'- {i["name"]}')

import json
import os

# Pfad zur JSON-Datei relativ zu diesem Python-Script
SPELLS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data", "spells.json"))

with open(SPELLS_PATH, "r", encoding="utf-8") as file:
    spells = json.load(file)


def start():
    # The code snippet `while True: wahl= int(input(""" Was möchtest du tun? 1. Zauber nach Namen suchen
    # 2. Zauber nach Level filtern 3. Zauber nach Klasse filtern 4. Zauber nach Schule filtern 5. Beenden
    # """))` is creating a loop that continuously prompts the user to input a choice of action. The user
    # is presented with a menu of options (search spell by name, filter spell by level, filter spell by
    # class, filter spell by school, or exit). The input is then converted to an integer and stored in the
    # variable `wahl` for further processing based on the selected option.
    while True:
        wahl = int(
            input(
                """
        Was möchtest du tun?
        1. Zauber nach Namen suchen
        2. Zauber nach Level filtern
        3. Zauber nach Klasse filtern
        4. Zauber nach Schule filtern
        5. Beenden
        """
            )
        )

        match wahl:
            case 1:
                name = input("Bitte gib den Namen eines Spells ein: ")

                for spell in spells:
                    if spell["name"].lower() == name.lower():
                        print("══════════════════════════════════════")
                        print(f"🪄 {spell['name']}")
                        print("══════════════════════════════════════")
                        print(f"🔢 Level:         {spell['level']}")
                        print(f"📚 Schule:        {spell['school'].capitalize()}")
                        print(f"⏱  Cast Time:     {spell['casting_time']}")
                        print(f"⏳ Dauer:          {spell['duration']}")
                        print(f"🎯 Reichweite:    {spell['range']}")
                        print("\n📖 Beschreibung:")
                        print(spell["description"])
                        print("══════════════════════════════════════")
            case 2:
                level = input("Bitte gib den Level eines Spells ein: ")

                for spell in spells:
                    if spell["level"] == level:
                        print(spell["name"])

            case 3:
                tags = input("Bitte gib die Klasse eines Spells ein: ")

                for spell in spells:
                    if spell["tags"] == tags:
                        print(spell["name"])

            case 4:
                school = input("Bitte gib die Schule eines Spells ein: ")

                for spell in spells:
                    if spell["school"] == school:
                        print(spell["name"])

            case 5:
                print("Bye bye bye")
                break
            case _:
                print("Ungültige Eingabe")

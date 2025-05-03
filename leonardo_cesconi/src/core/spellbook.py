import json
import os
import argparse

# Pfad zur JSON-Datei relativ zu diesem Python-Script
SPELLS_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "data", "spells.json")
)

with open(SPELLS_PATH, "r", encoding="utf-8") as file:
    spells = json.load(file)


def search_by_name(name: str):
    for spell in spells:
        if spell["name"].lower() == name.lower():
            return spell
    return None


def filter_by_level(level: str):
    return [spell for spell in spells if spell["level"] == level]


def filter_by_class(tag: str):
    return [spell for spell in spells if spell["tags"] == tag]


def filter_by_school(school: str):
    return [spell for spell in spells if spell["school"] == school]


def start():
    while True:
        wahl = input(
            """
        Was möchtest du tun?
        1. Zauber nach Namen suchen
        2. Zauber nach Level filtern
        3. Zauber nach Klasse filtern
        4. Zauber nach Schule filtern
        5. Beenden
        """
        )

        match wahl:
            case "1":
                name = input("Bitte gib den Namen eines Spells ein: ")
                spell = search_by_name(name)
                if spell:
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
            case "2":
                level = input("Bitte gib den Level eines Spells ein: ")
                filtered_spells = filter_by_level(level)
                for spell in filtered_spells:
                    print(spell["name"])
            case "3":
                tags = input("Bitte gib die Klasse eines Spells ein: ")
                filtered_spells = filter_by_class(tags)
                for spell in filtered_spells:
                    print(spell["name"])
            case "4":
                school = input("Bitte gib die Schule eines Spells ein: ")
                filtered_spells = filter_by_school(school)
                for spell in filtered_spells:
                    print(spell["name"])
            case "5":
                print("Bye bye bye")
                break
            case _:
                print("Ungültige Eingabe")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Spellbook CLI Tool")

    parser.add_argument("--search", type=str, help="Search spell by name")
    parser.add_argument("--level", type=str, help="Filter spells by level")
    parser.add_argument("--class_", type=str, help="Filter spells by class (tag)")
    parser.add_argument("--school", type=str, help="Filter spells by school")

    args = parser.parse_args()

    if args.search:
        spell = search_by_name(args.search)
        if spell:
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
        else:
            print("Spell not found.")
    elif args.level:
        spells_filtered = filter_by_level(args.level)
        print(f"Spells with level {args.level}:")
        for s in spells_filtered:
            print(f"- {s['name']}")
    elif args.class_:
        spells_filtered = filter_by_class(args.class_)
        print(f"Spells for class {args.class_}:")
        for s in spells_filtered:
            print(f"- {s['name']}")
    elif args.school:
        spells_filtered = filter_by_school(args.school)
        print(f"Spells from school {args.school}:")
        for s in spells_filtered:
            print(f"- {s['name']}")
    else:
        start()

import argparse
import spellbook
import looter
import combat


def main_menu():
    while True:
        print("Willkommen in deiner DnD-Toolbox!")
        print(
            """wähle ein tool:
                1. Zauberbuch
                2. Loot Generator
                3. Combat helper
                4. Beenden
                """
        )

        wahl = input(">")

        match wahl:
            case "1":
                spellbook.start()
            case "2":
                looter.start()
            case "3":
                combat.run_combat()
            case "4":
                print("Beenden..")
                break
            case _:
                print("ungülige Eingabe")


def main():
    parser = argparse.ArgumentParser(description="DnD Toolbox CLI")
    parser.add_argument(
        "--module",
        choices=["spellbook", "looter", "combat"],
        help="Modul, das direkt gestartet werden soll",
    )
    parser.add_argument("--rarity", type=str, help="Seltenheit (für Loot Generator)")
    parser.add_argument(
        "--count",
        type=int,
        help="Number of loot items to draw (only for looter module)",
    )
    parser.add_argument("--search", type=str, help="Search spell by name")
    parser.add_argument("--level", type=int, help="Filter spells by level")
    parser.add_argument("--class_", type=str, help="Filter spells by class")
    parser.add_argument("--school", type=str, help="Filter spells by school")

    args = parser.parse_args()

    if args.module == "spellbook":
        if args.search or args.level or args.class_ or args.school:
            spellbook.main(
                search=args.search,
                level=args.level,
                class_filter=args.class_,
                school=args.school,
            )
        else:
            spellbook.start()
    elif args.module == "looter":
        looter.start(rarity=args.rarity, count=args.count)
    elif args.module == "combat":
        combat.run_combat()
    else:
        main_menu()


if __name__ == "__main__":
    main()

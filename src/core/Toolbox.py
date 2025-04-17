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


if __name__ == "__main__":
    main_menu()

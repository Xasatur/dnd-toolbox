import spellbook
import Looter
import Combat


def main_menu():
    while True:
        print("Willkommen in deiner DnD-Toolbox!")
        print(
            """wähle ein tool:
                1. Zauberbuch
                2. Loot Generator
                3. Combat helper
                """
        )

        wahl = input(">")

        match wahl:
            case "1":
                spellbook.start()
            case "2":
                Looter.start()
            case "3":
                run_combat()
            case "4":
                print("beenden..")
                break
            case _:
                print("ungülige Eingabe")


if __name__ == "__main__":
    main_menu()

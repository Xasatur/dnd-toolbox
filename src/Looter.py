import random

loot = {
    "gewöhnlich": [{"name": "Rostiges Schwert"}, {"name": "kapute Stiefel"}],
    "selten": [
        {"name": "Magisches Schwert"},
        {"name": "gute Stiefel"},
        {"name": "Heiltrank"},
    ],
    "episch": [{"name": "Konny, der Drachentöter"}, {"name": "Stiefel des Hermes"}],
}

mapping = {1: "gewöhnlich", 2: "selten", 3: "episch"}


def start():
    while True:
        wahl = int(input("Gib gegendstand ein mann:"))
        anzahl = int(input("Wieviele Gegenstände?:"))

        if wahl in mapping:
            seltenheit = mapping[wahl]
            item = random.sample(loot[seltenheit], anzahl)
            print("Du bekommst: ")
            for i in item:
                print(f'- {i["name"]}')
        elif wahl == 9:
            break
        else:
            print("nö")

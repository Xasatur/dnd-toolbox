# engine/combat.py
import os
import importlib.util
import uuid
import random


# Helper to dynamically load a monster class from a Python file
def load_monsters(folder=None):
    if folder is None:
        folder = os.path.join(os.path.dirname(__file__), "monsters")
        folder = os.path.abspath(folder)

    monsters = []
    for filename in os.listdir(folder):
        if filename.endswith(".py"):
            path = os.path.join(folder, filename)
            name = filename[:-3]
            spec = importlib.util.spec_from_file_location(name, path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "Monster"):
                monster_class = module.Monster
                monsters.append((monster_class, name))
    return monsters


class MonsterInstance:
    def __init__(self, monster_class, instance_id):
        self.id = instance_id
        self.instance = monster_class()
        self.name = self.instance.name
        self.icon = self.instance.icon
        self.recharge = getattr(self.instance, "recharge_actions", {})
        self.bfa = (
            self.instance.battlefield_actions()
            if hasattr(self.instance, "battlefield_actions")
            else []
        )

    def actions(self):
        return self.instance.actions()

    def battlefield_actions(self):
        return self.bfa

    def attempt_recharge(self):
        for action, data in self.recharge.items():
            roll = random.randint(1, 6)
            data["available"] = roll in data["recharge_on"]
            print(
                f"🔄 Recharge Check for {action}: Rolled {roll} → {'Ready' if data['available'] else 'Still Recharging'}"
            )


# Display actions and resolve input
def run_combat():
    available_monsters = load_monsters()
    print("\n=== MONSTER SELECTION ===")
    for i, (monster_class, name) in enumerate(available_monsters):
        print(f"{i+1}. {monster_class().icon} {monster_class().name} ({name})")

    chosen = input("\nEnter comma-separated numbers to spawn monsters (e.g. 1,2,2): ")
    indexes = [int(i.strip()) - 1 for i in chosen.split(",")]

    active_monsters = []
    for idx in indexes:
        monster_class, _ = available_monsters[idx]
        instance_id = str(uuid.uuid4())[:4]
        active_monsters.append(MonsterInstance(monster_class, instance_id))

    round_counter = 1
    battlefield_queue = []  # tracks active battlefield actions

    while True:
        print(f"\n=== ROUND {round_counter} - ACTIVE MONSTERS ===")
        for i, m in enumerate(active_monsters):
            print(f"{i+1}. {m.icon} {m.name} [ID: {m.id}]")

        print("q. Quit")
        selection = input("\nChoose a monster to act: ").strip().lower()

        if selection == "q":
            print("Exiting...\n")
            break

        if not selection.isdigit() or not (1 <= int(selection) <= len(active_monsters)):
            print("Invalid selection.")
            continue

        current = active_monsters[int(selection) - 1]

        # Recharge Check
        if current.recharge:
            current.attempt_recharge()

        # Resolve any pending Battlefield Actions
        for bfa in battlefield_queue[:]:
            if bfa["round"] == round_counter and bfa["monster_id"] == current.id:
                print(
                    f"\n⚠️ Battlefield Action Resolution for {bfa['name']}: {bfa['resolution']}"
                )
                battlefield_queue.remove(bfa)

        # Action Menu
        print(f"\n=== {current.icon} {current.name} Actions ===")
        actions = current.actions()
        for i, action_name in enumerate(actions):
            note = (
                " [Ready]"
                if action_name in current.recharge
                and current.recharge[action_name]["available"]
                else ""
            )
            if (
                action_name in current.recharge
                and not current.recharge[action_name]["available"]
            ):
                note = " [Recharging]"
            print(f"{i+1}. {action_name}{note}")

        if current.battlefield_actions():
            print("b. ⚔️  Trigger Battlefield Action Tell")
        print("x. Back")

        action_choice = (
            input("Choose one or more actions (e.g. 1,2,3): ").strip().lower()
        )
        if action_choice == "x":
            continue
        elif action_choice == "b" and current.battlefield_actions():
            print("\n📣 Battlefield Actions:")
            for bfa in current.battlefield_actions():
                print(f"🌪️ {bfa['name']}: {bfa['tell']}")
                battlefield_queue.append(
                    {
                        "name": bfa["name"],
                        "monster_id": current.id,
                        "round": round_counter + 1,
                        "resolution": bfa["resolution"],
                    }
                )
        else:
            action_indexes = [
                s.strip() for s in action_choice.split(",") if s.strip().isdigit()
            ]
            for a in action_indexes:
                i = int(a)
                if 1 <= i <= len(actions):
                    action_name = list(actions.keys())[i - 1]
                    if (
                        action_name in current.recharge
                        and not current.recharge[action_name]["available"]
                    ):
                        print(f"⛔ {action_name} is still recharging.")
                        continue
                    result = actions[action_name]()
                    print(f"\n🎯 {action_name}:\n{result}\n")
                else:
                    print(f"Invalid action number: {a}")

        round_counter += 1

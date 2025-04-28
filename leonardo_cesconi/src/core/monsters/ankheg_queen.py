# monsters/ankheg_queen.py
import random
import re

# Dice roller for damage strings like "2d6+3"
def roll_dice(expression):
    match = re.match(r"(\d+)d(\d+)([+-]\d+)?", expression)
    if not match:
        return f"Invalid expression: {expression}"
    num_dice, dice_type, modifier = match.groups()
    rolls = [random.randint(1, int(dice_type)) for _ in range(int(num_dice))]
    total = sum(rolls) + int(modifier) if modifier else sum(rolls)
    return f"{total} ({rolls})"

class Monster:
    
    name = "Ankheg Brood Queen"
    icon = "🐛"
    recharge_actions = {
        "Acid Spray": {
            "recharge_on": [6],
            "available": True
        }
    }


    def actions(self):
        return {
            "Claw Attack": self.claw_attack,
            "Bite Attack": self.bite_attack,
            "Flurry of Legs": self.flurry_of_legs,
            "Acid Spray": self.acid_spray,
            "Acid Glob (Reaction)": self.acid_glob_reaction,
            "Pressurized Carapace (on Death)": self.pressurized_carapace,
            "Legendary: Burrow": lambda: self.legendary_action("burrow"),
            "Legendary: Pull": lambda: self.legendary_action("pull"),
            "Legendary: Acid Expulsion": lambda: self.legendary_action("acid expulsion"),
        }

    def battlefield_actions(self):
        return [
            {
                "name": "Summoning Circles",
                "tell": "Two glowing summoning circles pulse with energy...",
                "neutralize": "Stand on the circles to stop the summoning.",
                "resolution": "If not neutralized, two Ankheg minions are summoned."
            },
            {
                "name": "Eruption",
                "tell": "The ground cracks beneath the Queen's weight, glowing with heat...",
                "neutralize": "Move more than 20 feet from the center to reduce damage.",
                "resolution": "The ground erupts. Creatures within 20ft take full damage. Others take less."
            }
        ]

    def claw_attack(self):
        to_hit = random.randint(1, 20) + 10
        damage = roll_dice("2d6+6")
        return f"To Hit: {to_hit} | Damage: {damage}"

    def bite_attack(self):
        to_hit = random.randint(1, 20) + 10
        damage = roll_dice("4d6+6")
        return f"To Hit: {to_hit} | Damage: {damage}"

    def flurry_of_legs(self):
        to_hit = random.randint(1, 20) + 10
        piercing = roll_dice("6d6+6")
        acid = roll_dice("4d6")
        return f"To Hit: {to_hit} | Piercing: {piercing}, Acid: {acid}"

    def acid_spray(self):
        damage = roll_dice("8d6")
        return f"DC 17 Dex Save | Acid Damage: {damage}"

    def acid_glob_reaction(self):
        damage = roll_dice("3d6")
        return f"DC 15 Con Save | Damage: {damage} | Target speed reduced to 0"

    def pressurized_carapace(self):
        bludgeon = roll_dice("1d6")
        acid = roll_dice("5d6")
        total = int(bludgeon.split()[0]) + int(acid.split()[0])
        return f"DC 16 Dex Save | Total: {total} | Bludgeoning: {bludgeon}, Acid: {acid}"

    def legendary_action(self, action):
        if action == "burrow":
            return "The Ankheg burrows 20ft underground."
        elif action == "pull":
            return "Bite at advantage, pulls a creature underground (restrained)."
        elif action == "acid expulsion":
            damage = roll_dice("6d6")
            return f"DC 15 Dex Save | Acid Damage: {damage} | Speed = 0"
        else:
            return "Unknown legendary action."

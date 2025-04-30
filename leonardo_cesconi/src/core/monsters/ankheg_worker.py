# monsters/ankheg_worker.py
import random
import re


# Use the same roll_dice utility
def roll_dice(expression):
    match = re.match(r"(\d+)d(\d+)([+-]\\d+)?", expression)
    if not match:
        return f"Invalid expression: {expression}"
    num_dice, dice_type, modifier = match.groups()
    rolls = [random.randint(1, int(dice_type)) for _ in range(int(num_dice))]
    total = sum(rolls) + int(modifier) if modifier else sum(rolls)
    return f"{total} ({rolls})"


class Monster:
    name = "Ankheg Worker"
    icon = "🪲"

    def actions(self):
        return {
            "Bite": self.bite,
            "Acid Spit": self.acid_spit,
        }

    def bite(self):
        to_hit = random.randint(1, 20) + 5
        damage = roll_dice("2d6+2")
        return f"To Hit: {to_hit} | Piercing Damage: {damage}"

    def acid_spit(self):
        damage = roll_dice("3d6")
        return f"DC 13 Dex Save | Acid Damage: {damage}"

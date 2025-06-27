# monsters/flesh_golem_timewarped.py
import random
import re

def roll_dice(expression):
    match = re.match(r"(\d+)d(\d+)([+-]\d+)?", expression)
    if not match:
        return f"Invalid expression: {expression}"
    num_dice, dice_type, modifier = match.groups()
    rolls = [random.randint(1, int(dice_type)) for _ in range(int(num_dice))]
    total = sum(rolls) + int(modifier) if modifier else sum(rolls)
    return f"{total} ({rolls})"

class Monster:
    name = "Time-Warped Flesh Golem"
    icon = "🧟‍♂️"
    recharge_actions = {"Time Skip": {"recharge_on": [5, 6], "available": True}}

    def actions(self):
        return {
            "Slam Attack": self.slam_attack,
            "Time Skip": self.time_skip,
            "Delayed Punch": self.delayed_punch,
            "Temporal Backlash (on Death)": self.temporal_backlash,
        }

    def battlefield_actions(self):
        return [
            {
                "name": "Temporal Ripple",
                "tell": "The air shimmers as time warps around the golem...",
                "neutralize": "Stand still to avoid phase displacement.",
                "resolution": "Moving creatures are teleported 10ft in a random direction.",
            }
        ]

    def slam_attack(self):
        to_hit = random.randint(1, 20) + 7
        damage = roll_dice("2d8+4")
        return f"To Hit: {to_hit} | Bludgeoning Damage: {damage}"

    def time_skip(self):
        return "The golem phases out. Until its next turn, it cannot be targeted. Recharges on 5–6."

    def delayed_punch(self):
        damage = roll_dice("3d10")
        return f"DC 16 Con Save | Delayed Force Punch hits at end of next round | Damage: {damage}"

    def temporal_backlash(self):
        damage = roll_dice("5d6")
        return f"DC 15 Int Save | Psychic Damage: {damage} | If failed, stunned for 1 round"

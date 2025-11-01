# monsters/aelor_thran.py
import random
import re


def roll_dice(expression: str) -> str:
    match = re.match(r"(\d+)d(\d+)([+-]\d+)?", expression)
    if not match:
        return f"Invalid expression: {expression}"
    num_dice, dice_type, modifier = match.groups()
    rolls = [random.randint(1, int(dice_type)) for _ in range(int(num_dice))]
    total = sum(rolls)
    if modifier:
        total += int(modifier)
    roll_display = ", ".join(str(r) for r in rolls)
    return f"{total} ({roll_display}{modifier or ''})"


class Monster:

    name = "Aelor Thran, Magister of Dominion"
    icon = "👑"

    def __init__(self):
        self.hp = {"magister": 170, "vessel": 170}
        self.current_hp = self.hp["magister"]
        self.form = "magister"
        self.transformed = False
        self.legendary_resistances_remaining = {"magister": 3, "vessel": 3}
        self.recharge_actions = {}
        self._enter_magister_form(initial=True)

    # --- Form Management -------------------------------------------------
    def _enter_magister_form(self, initial: bool = False) -> None:
        self.form = "magister"
        self.name = "Aelor Thran, Magister of Dominion"
        self.icon = "👑"
        if initial:
            self.current_hp = self.hp["magister"]
        self._set_recharge_actions(
            {
                "Eldritch Surge": {"recharge_on": [5, 6], "available": True},
                "Legendary: Dominize": {"recharge_on": [5, 6], "available": True},
            }
        )

    def _enter_vessel_form(self) -> str:
        if self.transformed:
            return "Aelor Thran is already channeling the Vessel of Dominion."

        self.transformed = True
        self.form = "vessel"
        self.name = "Aelor Thran, Vessel of Dominion"
        self.icon = "💎"
        self.current_hp = self.hp["vessel"]
        # Mythic transformation restores legendary resistances for the new form.
        self.legendary_resistances_remaining["vessel"] = 3
        self._set_recharge_actions(
            {
                "Golden Pulse": {"recharge_on": [5, 6], "available": True},
                "Legendary: Domain": {"recharge_on": [5, 6], "available": True},
            }
        )
        return (
            "✨ Mythic Transformation! Aelor shatters into radiant motes before reforming as the "
            "Vessel of Dominion. Legendary Resistances are restored for the new form."
        )

    def _set_recharge_actions(self, new_data):
        self.recharge_actions.clear()
        for key, value in new_data.items():
            self.recharge_actions[key] = value.copy()

    # --- Utility Actions --------------------------------------------------
    def actions(self):
        shared = {
            "Form & HP Tracker": self.adjust_hp,
            "Trait: Scepter of Dominion": self.scepter_of_dominion_trait,
            "Legendary Resistance": self.use_legendary_resistance,
        }
        if self.form == "magister":
            return {
                "Multiattack (Magister)": self.magister_multiattack,
                "Scepter Strike": self.magister_scepter_strike,
                "Ocular Ray": self.magister_ocular_ray,
                "Eldritch Surge": self.magister_eldritch_surge,
                "Bonus: Tearing Dominate Person": self.bonus_dominate_person,
                "Bonus: Rary's Telepathic Bond": self.bonus_telepathic_bond,
                "Reaction: Restore Order": self.reaction_restore_order,
                "Legendary: Dominize": self.legendary_dominize,
                "Legendary: Restore": self.legendary_restore,
                "Utility: Manually Trigger Vessel Form": self.manual_transformation,
                **shared,
            }
        return {
            "Multiattack (Vessel)": self.vessel_multiattack,
            "Scepter Strike (Mythic)": self.vessel_scepter_strike,
            "Golden Pulse": self.vessel_golden_pulse,
            "Reaction: Golden Backlash": self.reaction_golden_backlash,
            "Legendary: Golden Grasp": self.legendary_golden_grasp,
            "Legendary: Domain": self.legendary_domain,
            "Legendary: Restore": self.legendary_restore,
            "Mythic Action: Misty Step": self.mythic_misty_step,
            **shared,
        }

    # --- Shared Utilities -------------------------------------------------
    def adjust_hp(self):
        prompt = (
            f"Enter damage to apply to {self.name} (positive) or healing (negative). "
            "Leave blank to only view status: "
        )
        raw = input(prompt).strip()
        if raw:
            try:
                amount = int(raw)
            except ValueError:
                return "❌ Invalid number provided."
            self.current_hp -= amount
            max_hp = self.hp[self.form]
            if self.form == "magister" and self.current_hp <= 0:
                transform_text = self._enter_vessel_form()
                status = self.form_status()
                return f"{transform_text}\n{status}"
            # Clamp HP within bounds for the active form.
            self.current_hp = max(min(self.current_hp, max_hp), 0)
        return self.form_status()

    def manual_transformation(self):
        if self.transformed:
            return "Aelor is already in his Vessel of Dominion form."
        text = self._enter_vessel_form()
        return f"Manual override engaged. {text}"

    def form_status(self):
        max_hp = self.hp[self.form]
        remaining_lr = self.legendary_resistances_remaining[self.form]
        return (
            f"{self.name} ({self.form.title()} Form) — HP: {self.current_hp}/{max_hp}. "
            f"Legendary Resistances Remaining: {remaining_lr}."
        )

    def use_legendary_resistance(self):
        remaining = self.legendary_resistances_remaining[self.form]
        if remaining <= 0:
            return "No legendary resistances remain for this form."
        self.legendary_resistances_remaining[self.form] -= 1
        return (
            f"Legendary Resistance expended. {self.legendary_resistances_remaining[self.form]} "
            "use(s) left for this form."
        )

    def scepter_of_dominion_trait(self):
        details = (
            "Once per round when Aelor hits or a creature fails a save against him, "
            "choose: Hinder (disadvantage on next attack), Dominize (DC 18 Wis save or "
            "Charmed until end of Aelor's next turn), or Destabilize (DC 18 Con save for "
            "2d6 force on a failure)."
        )
        choice = input(
            "Select an option — [h]inder, [d]ominate, [s]hatter (destabilize), or blank for summary: "
        ).strip().lower()
        if choice.startswith("h"):
            return "Hinder: Target has disadvantage on its next attack roll."
        if choice.startswith("d"):
            return "Dominate: Target must succeed on a DC 18 Wisdom save or become charmed."
        if choice.startswith("s"):
            damage = roll_dice("2d6")
            return (
                f"Destabilize: Target makes a DC 18 Constitution save or takes {damage} force damage; "
                "half on success."
            )
        return details

    def legendary_restore(self):
        temp_hp = 10 if self.form == "magister" else 20
        return (
            f"Restore (Legendary, cost 3). Aelor or an ally he can see gains {temp_hp} temporary HP."
        )

    # --- Magister Form ----------------------------------------------------
    def magister_multiattack(self):
        return (
            "Make two Scepter Strikes and cast one at-will spell (typically Ocular Ray)."
        )

    def magister_scepter_strike(self):
        to_hit = random.randint(1, 20) + 10
        bludgeoning = roll_dice("1d8+5")
        radiant = roll_dice("1d8")
        return (
            f"To Hit: {to_hit} | Damage: {bludgeoning} bludgeoning + {radiant} radiant.\n"
            "Trigger Scepter of Dominion to impose Hinder, Dominize, or Destabilize."
        )

    def magister_ocular_ray(self):
        to_hit = random.randint(1, 20) + 9
        radiant = roll_dice("3d8")
        return (
            f"To Hit: {to_hit} | Damage: {radiant} radiant. Target glows with golden light, giving "
            "advantage to the next attacker until the start of Aelor's next turn."
        )

    def magister_eldritch_surge(self):
        radiant = roll_dice("8d6")
        return (
            "Eldritch Surge (Recharge 5-6): 60-ft line (5 ft wide), DC 17 Dex save. "
            f"Failed save: {radiant} radiant damage, pushed 10 ft, restrained by crackling force until the end of Aelor's next turn. "
            "Successful save: half damage and no push or restraint."
        )

    def bonus_dominate_person(self):
        return (
            "Bonus Action — Tearing Dominate Person: Cast *dominate person* (DC 18 Wis). "
            "The spell does not require concentration while Aelor wields the Scepter."
        )

    def bonus_telepathic_bond(self):
        return (
            "Bonus Action — Rary's Telepathic Bond: Creates a telepathic link for up to 1 hour "
            "between Aelor and up to eight willing allies he can see."
        )

    def reaction_restore_order(self):
        return (
            "Reaction — Restore Order: When a creature Aelor can see succeeds on a saving throw, "
            "he can force it to reroll, potentially turning the tide back to his favor."
        )

    def legendary_dominize(self):
        return (
            "Legendary Action (cost 1, Recharge 5-6) — Dominize: One creature Aelor can see "
            "must succeed on a DC 18 Wisdom save or become charmed (dominated) until the end of "
            "its next turn."
        )

    # --- Vessel Form ------------------------------------------------------
    def vessel_multiattack(self):
        return (
            "Make two Scepter Strikes or one Scepter Strike and one Golden Pulse."
        )

    def vessel_scepter_strike(self):
        to_hit = random.randint(1, 20) + 10
        radiant = roll_dice("3d8+5")
        return (
            f"To Hit: {to_hit} | Damage: {radiant} radiant. Target is pushed 10 ft and is restrained "
            "in golden shackles until the end of its next turn on a failed DC 18 Strength save."
        )

    def vessel_golden_pulse(self):
        radiant = roll_dice("3d10")
        psychic = roll_dice("3d10")
        return (
            "Golden Pulse (Recharge 5-6): Each creature of Aelor's choice within 30 ft makes a "
            f"DC 17 Dex save. Failed save: {radiant} radiant + {psychic} psychic damage and the target "
            "is pulled 10 ft toward Aelor. Successful save: half damage and no pull."
        )

    def reaction_golden_backlash(self):
        radiant = roll_dice("2d10")
        return (
            f"Reaction — Golden Backlash: When struck by a melee attack, the attacker takes {radiant} "
            "radiant damage and must succeed on a DC 18 Strength save or be knocked prone."
        )

    def legendary_golden_grasp(self):
        to_hit = random.randint(1, 20) + 10
        radiant = roll_dice("2d8")
        return (
            f"Legendary Action (cost 1) — Golden Grasp: To Hit {to_hit}; on a hit {radiant} radiant "
            "damage and the target is restrained by luminous chains (escape DC 18)."
        )

    def legendary_domain(self):
        radiant = roll_dice("4d8")
        psychic = roll_dice("4d8")
        return (
            "Legendary Action (cost 2, Recharge 5-6) — Domain: Creatures of Aelor's choice within 20 ft "
            f"take {radiant} radiant + {psychic} psychic damage (DC 18 Wis save for half) and are pulled "
            "10 ft toward him on a failed save."
        )

    def mythic_misty_step(self):
        return (
            "Mythic Action (cost 2) — Misty Step: Aelor teleports up to 30 ft to an unoccupied space "
            "he can see and becomes wreathed in radiant sigils until the start of his next turn, "
            "granting him half cover."
        )

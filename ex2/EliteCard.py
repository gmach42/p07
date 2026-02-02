from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        combat_type: str,
        attack_power: int,
        defense: int,
        health: int,
        mana: int,
        knowned_spells: dict[str, int],
    ):
        # initialize Card and Magical explicitly (avoid double super() misuse)
        Card.__init__(self, name, cost, rarity)
        Magical.__init__(self, mana, knowned_spells)
        self.combat_type = combat_type
        # only these must be strictly positive
        for charac in [attack_power, defense, health]:
            if charac <= 0:
                raise ValueError(f"{charac} must be a positive integer!")
        self.attack_power = attack_power
        self.defense = defense
        self.health = health

    # Card's methods
    def play(self, game_state: dict) -> dict:
        if not self.is_playable(game_state["mana"]):
            print()
            return
        result = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }
        game_state["mana"] -= self.cost
        game_state['played_cards'].append(self)
        return f"Play result: {result}\n"

    # Combatable's methods
    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": self.combat_type,
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_taken = incoming_damage - self.defense
        self.health -= damage_taken
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": self.defense,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self):
        # d1 = super().get_card_info()
        # d2 = super().get_combat_stats()
        # res = d1.update(d2)
        return super().get_combat_stats()

    # Magic-related methods
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        if spell_name not in self.knowned_spells:
            return f"Spell not knowned by {self.name}!"
        spell_cost = self.knowned_spells[spell_name] * len(targets)
        if self.mana - spell_cost < 0:
            return f"{self.name} has not enough mana to use {spell_name}"
        self.mana -= spell_cost
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": spell_cost,
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana,
        }

    def get_magic_stats(self) -> dict:
        # d1 = super().get_card_info()
        # d2 = super().get_magic_stats()
        # res = d1.update(d2)
        return super().get_magic_stats()

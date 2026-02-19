from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """
    Class representing an elite card with combat and magical abilities

    Attributes:
        name (str): The name of the card
        cost (int): The mana cost to play the card
        rarity (str): The rarity of the card
        combat_type (str): The type of combat (Melee, Ranged, etc.)
        attack_power (int): The attack power of the card
        defense (int): The defense value of the card
        health (int): The health points of the card
        mana (int): The mana available for spells
        knowned_spells (dict[str, int]): Known spells and their costs
    """

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
        """
        Initialize an EliteCard with all attributes

        Args:
            name (str): The name of the card
            cost (int): The mana cost to play the card
            rarity (str): The rarity of the card
            combat_type (str): The type of combat
            attack_power (int): The attack power (must be positive)
            defense (int): The defense value (must be positive)
            health (int): The health points (must be positive)
            mana (int): The mana available for spells
            knowned_spells (dict[str, int]): Known spells and costs
        """
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
        self._check_mana(game_state)
        result = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }
        game_state["active_player"].spend_mana(self.cost)
        return result

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

    def get_combat_stats(self) -> dict:
        return {
            "combat_type": self.combat_type,
            "attack_power": self.attack_power,
            "defense": self.defense,
            "health": self.health,
        }

    # Magic methods
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
            "targets": [target.name for target in targets],
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

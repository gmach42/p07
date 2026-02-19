from ex0.Player import Player
from .Card import Card


class CreatureCard(Card):
    """
    Class representing a creature card in the game

    Attributes:
        name (str): The name of the creature card
        cost (int): The mana cost to play the card
        rarity (str): The rarity of the card
            (Common, Uncommon, Rare, Legendary)
        attack (int): The attack value of the creature
        health (int): The health value of the creature
    """

    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int) -> None:
        """
        Initialize a CreatureCard with its attributes

        Args:
            name (str): The name of the creature card
            cost (int): The mana cost to play the card
            rarity (str): The rarity of the card
                (Common, Uncommon, Rare, Legendary)
            attack (int): The attack value of the creature
            health (int): The health value of the creature
        """
        super().__init__(name, cost, rarity)
        if attack > 0:
            self.attack = attack
        else:
            raise ValueError(f"Please enter a non-zero positive value "
                             f"to set the attack of {self.name}")
        if attack > 0:
            self.health = health
        else:
            raise ValueError(f"Please enter a non-zero positive value "
                             f"to set the health of {self.name}")

    def play(self, game_state: dict) -> dict:
        """Play the creature card and return the result of the action"""
        self._check_mana(game_state)
        result = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }
        return result

    def attack_target(self, target: "CreatureCard | Player") -> dict:
        """Attack a target and return the result of the action"""
        if isinstance(target, Player):
            if self.attack >= target.lifepoints:
                target.lifepoints = 0
                combat_resolved = True
            else:
                target.lifepoints -= self.attack
                combat_resolved = False
        else:
            if self.attack >= target.health:
                target.health = 0
                combat_resolved = True
            else:
                target.health -= self.attack
                combat_resolved = False

        result = {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": combat_resolved,
        }
        return result

    @classmethod
    def fire_dragon(cls) -> "CreatureCard":
        """Create a Fire Dragon creature card"""
        return cls("Fire Dragon", 5, "Legendary", 7, 5)

    @classmethod
    def goblin_warrior(cls) -> "CreatureCard":
        """Create a Goblin Warrior creature card"""
        return cls("Goblin Warrior", 3, "Rare", 2, 7)

    @classmethod
    def gnome_scout(cls) -> "CreatureCard":
        """Create a Gnome Scout creature card"""
        return cls("Gnome Scout", 2, "Common", 1, 2)

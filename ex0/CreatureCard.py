from .Card import Card


class CreatureCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int
    ):
        super().__init__(name, cost, rarity)
        if attack > 0:
            self.attack = attack
        else:
            raise ValueError(
                f"Please enter a non-zero positive value "
                f"to set the attack of {self.name}"
            )
        if attack > 0:
            self.health = health
        else:
            raise ValueError(
                f"Please enter a non-zero positive value "
                f"to set the health of {self.name}"
            )

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
        print(f"Play result: {result}\n")

    def attack_target(self, target) -> dict:
        result = {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }
        print(f"Attack result: {result}\n")

    @classmethod
    def fire_dragon(cls):
        return cls("Fire Dragon", 5, "Legendary", 7, 5)

    @classmethod
    def goblin_warrior(cls):
        return cls("Goblin Warrior", 3, "Rare", 2, 7)

    @classmethod
    def gnome_scout(cls):
        return cls("Gnome Scout", 2, "Common", 1, 2)

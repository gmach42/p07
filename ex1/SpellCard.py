from ex0.Card import Card


class SpellCard(Card):
    """
    Class representing a spell card in the game

    Attributes:
        name (str): The name of the spell card
        cost (int): The mana cost to play the card
        rarity (str): The rarity of the card
            (Common, Uncommon, Rare, Legendary)
        effect_type (str): The type of effect (Damage, Heal, etc.)
    """

    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        """
        Initialize a SpellCard with its attributes

        Args:
            name (str): The name of the spell card
            cost (int): The mana cost to play the card
            rarity (str): The rarity of the card
            effect_type (str): The type of effect
        """
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        """Play the spell card and return the result of the action"""
        self._check_mana(game_state)
        result = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect":
            self.resolve_effect(game_state.get("enemy_creatures", [])),
        }
        self.resolve_effect(game_state.get("enemy_creatures", []))
        return result

    def resolve_effect(self, targets: list) -> dict:
        """Resolve the spell effect on the given targets"""
        for target in targets:
            target.health -= 3
        names = [target.name for target in targets]
        return {"Effect Type": self.effect_type, "Targets": names}

    @classmethod
    def fireball(cls) -> "SpellCard":
        """Create a Fireball spell card"""
        return cls("Fireball", cost=4, rarity="Uncommon", effect_type="Damage")

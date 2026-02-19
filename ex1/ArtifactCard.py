from ex0.Card import Card


class ArtifactCard(Card):
    """
    Class representing an artifact card in the game

    Attributes:
        name (str): The name of the artifact card
        cost (int): The mana cost to play the card
        rarity (str): The rarity of the card
            (Common, Uncommon, Rare, Legendary)
        durability (int): The durability of the artifact
        effect (str): The effect of the artifact
    """

    def __init__(self, name: str, cost: int, rarity: str, durability: int,
                 effect: str):
        """
        Initialize an ArtifactCard with its attributes

        Args:
            name (str): The name of the artifact card
            cost (int): The mana cost to play the card
            rarity (str): The rarity of the card
            durability (int): The durability of the artifact
            effect (str): The effect of the artifact
        """
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        """Play the artifact card and return the result of the action"""
        self._check_mana(game_state)
        result = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.activate_ability(),
        }
        return result

    def activate_ability(self) -> dict:
        """Activate the artifact's permanent ability"""
        return {"Permanent": self.effect}

    @classmethod
    def mana_ring(cls) -> "ArtifactCard":
        """Create a Mana Ring artifact card"""
        return cls(
            name="Mana Ring",
            cost=3,
            rarity="Uncommon",
            durability=5,
            effect="Mana Boost",
        )

    @classmethod
    def mana_crystal(cls) -> "ArtifactCard":
        """Create a Mana Crystal artifact card"""
        return cls(
            name="Mana Crystal",
            cost=2,
            rarity="Common",
            durability=3,
            effect="+1 mana per turn",
        )

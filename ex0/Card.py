from abc import ABC, abstractmethod


class NotEnoughManaError(Exception):
    """Raised when player tries to play a card without enough mana."""
    pass


class CardTypeError(Exception):
    """Raised when card type is invalid."""
    pass


class Card(ABC):
    """Abstract base class for all card types.

    Attributes:
        name (str): The name of the card.
        cost (int): The mana cost to play the card.
        rarity (str): The rarity of the card
            ("Common", "Uncommon", "Rare", "Epic", "Legendary").
        type (str): The type of the card, derived from the class name.
    """

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """Initialize a card with name, cost, rarity, and type.
        Args:
            name (str): The name of the card.
            cost (int): The mana cost to play the card.
            rarity (str): The rarity of the card
                ("Common", "Uncommon", "Rare", "Epic", "Legendary").
        """
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.type = self.__class__.__name__.replace('Card', '')

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Play the card. Child classes must implement this method.

        Child classes should call self._check_mana(game_state) first.
        """
        pass

    def get_card_info(self) -> dict:
        """Return a dictionary of the card's attributes."""
        return self.__dict__

    def is_playable(self, available_mana: int) -> bool:
        """Boolean method to check if the card is playable."""
        if available_mana >= self.cost:
            return True
        return False

    def _check_mana(self, game_state: dict) -> None:
        """Helper method to check if player has enough mana.

        Raises NotEnoughManaError if not enough mana.
        Should be called by child classes at the start of their play() method.
        """
        if not self.is_playable(game_state["active_player"].get_mana()):
            raise NotEnoughManaError(f"Not enough mana to play {self.name}!")

    def __repr__(self) -> str:
        return f"{self.name} ({self.type}, cost: {self.cost})"

    def __str__(self) -> str:
        return f"{self.name} ({self.cost})"

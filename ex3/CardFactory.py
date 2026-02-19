from abc import ABC, abstractmethod
from random import choice
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard


class CardFactory(ABC):
    """
    Abstract factory for creating different types of cards

    Attributes:
        supported_types (list): List of supported card types
    """

    supported_types = []

    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Create a creature card"""
        res = CreatureCard(name_or_power)
        return res

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Create a spell card"""
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Create an artifact card"""
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        """Create a themed deck of the specified size"""
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        """Return the supported card types"""
        pass

    @staticmethod
    def generate_deck(deck_list: dict) -> list[Card]:
        """Generate a random deck based on the provided deck list with 15
        creatures, 10 spells, and 5 artifacts."""
        deck = []
        for _ in range(15):
            creature = choice(deck_list["creatures"])
            deck.append(creature)
        for _ in range(10):
            spell = choice(deck_list["spells"])
            deck.append(spell)
        for _ in range(5):
            artifact = choice(deck_list["artifacts"])
            deck.append(artifact)
        return deck

    def __str__(self):
        """Return string representation of the factory"""
        return self.__class__.__name__

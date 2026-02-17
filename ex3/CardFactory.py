from abc import ABC, abstractmethod
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard


class CardFactory(ABC):
    supported_types = []

    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        res = CreatureCard(name_or_power)
        return res

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        pass

    def __str__(self):
        return self.__class__.__name__

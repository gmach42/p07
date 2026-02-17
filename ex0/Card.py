from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.type = self.__class__.__name__.replace('Card', '')

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return self.__dict__

    def is_playable(self, available_mana: int) -> bool:
        if available_mana >= self.cost:
            return True
        return False

    def __repr__(self) -> str:
        return f"{self.name} ({self.type}, cost: {self.cost})"

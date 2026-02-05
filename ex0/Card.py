from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.type = self.__class__.__name__.replace('Card', '')

    @abstractmethod
    def play(self, game_state: dict):
        pass

    def get_card_info(self):
        return self.__dict__

    def is_playable(self, available_mana: int):
        if available_mana >= self.cost:
            return True
        return False

    def __repr__(self):
        return f"{self.name} ({self.type}, cost: {self.cost})"

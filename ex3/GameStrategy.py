from abc import ABC, abstractmethod


class GameStrategy(ABC):
    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        for card in hand:
            card.play()

    @abstractmethod
    def get_strategy_name(self) -> str:
        return self.__class__.__name__

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        pass

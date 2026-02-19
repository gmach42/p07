from abc import ABC, abstractmethod
from ex0.Card import Card


class GameStrategy(ABC):
    """Abstract base class for game strategies"""

    @abstractmethod
    def execute_turn(self, hand: list[Card], battlefield: list) -> dict:
        """Execute the turn and return a dict of all actions performed"""
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Return the name of the strategy"""
        return self.__class__.__name__

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        """Prioritize targets for attacking based on strategy"""
        pass

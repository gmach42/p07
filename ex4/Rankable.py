from abc import ABC, abstractmethod


class Rankable(ABC):
    """Abstract base class for entities that can be ranked"""

    @abstractmethod
    def calculate_rating(self) -> int:
        """Calculate and return the rating of the entity"""
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Update the number of wins"""
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Update the number of losses"""
        pass

    @abstractmethod
    def get_rank_info(self) -> int:
        """Return the rank information"""
        pass

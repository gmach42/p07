from abc import ABC, abstractmethod


class Rankable(ABC):
    @abstractmethod
    def calculate_rating(self) -> int:
        pass

    @abstractmethod
    def update_wins(self, wins: int):
        pass

    @abstractmethod
    def update_losses(self, losses: int):
        pass

    @abstractmethod
    def get_rank_info(self) -> int:
        pass

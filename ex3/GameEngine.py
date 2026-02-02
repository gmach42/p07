from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class GameEngine:
    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        return {
            'Hand': self.hand,
            'Turn execution:\n': {'Strategy': self.strategy, 'Actions': self.actions},
        }

    def get_engine_status(self) -> dict:
        return {
            "Factory": self.factory,
            'Strategy': self.strategy,
            'Available types': self.available_types,
        }

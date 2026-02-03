from .CardFactory import CardFactory
from .GameStrategy import GameStrategy
from ex0.Card import Card


class GameEngine:
    def __init__(self, factory: CardFactory, strategy: GameStrategy):
        self.factory = factory
        self.strategy = strategy
        self.total_damage: int = 0
        self.card_created: Card = []

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        return {
            'Strategy': self.strategy,
            'Actions': self.self.strategy.execute_turn
        }

    def get_engine_status(self) -> dict:
        return {
            "Factory": self.factory,
            'Strategy': self.strategy,
            'Available types': self.available_types,
        }

    def get_game_report(self) -> dict:
        return {
            'turn_simulated': self.nb_turns,
            'strategy_used': self.strategy,
            'total_damage': self.total_damage,
            'card_created': self.card_created,
        }

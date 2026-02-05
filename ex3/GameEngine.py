from .CardFactory import CardFactory
from .GameStrategy import GameStrategy
from ex0.Card import Card


class GameEngine:
    def __init__(self, factory: CardFactory, strategy: GameStrategy):
        self.factory = factory
        self.strategy = strategy
        self.total_damage: int = 0
        self.card_created: Card = []
        self.available_types = []
        self.nb_turns: int = 0
        self.hand: list = []
        self.battlefield: list = []

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        self.available_types = self.factory.get_supported_types()

    def simulate_turn(self, hand: list, battlefield: list, gamestate: dict) -> dict:
        actions = self.strategy.execute_turn(hand, battlefield)
        gamestate['mana'] = actions['remaining_mana']
        gamestate['hand'] = [card for card in hand if card not in actions['cards_played']]
        gamestate['battlefield'] = battlefield
        self.nb_turns += 1
        return {
            'Strategy': self.strategy.get_strategy_name(),
            'Actions': actions,
        }

    def get_engine_status(self) -> dict:
        return {
            "Factory": self.factory,
            'Strategy': self.strategy.get_strategy_name(),
            'Available types': self.available_types,
        }

    def get_game_report(self) -> dict:
        return {
            'turn_simulated': self.nb_turns,
            'strategy_used': self.strategy.get_strategy_name(),
            'total_damage': self.total_damage,
            'card_created': self.card_created,
        }

from .CardFactory import CardFactory
from .GameStrategy import GameStrategy
from ex0.Card import Card
from ex1.Deck import Deck


class Player:
    def __init__(self, name: str, mana: int, deck: Deck):
        self.name = name
        self.__mana = mana
        self.__deck = deck
        self.__hand: list[Card] = []

    def set_mana(self, mana: int) -> None:
        self.__mana = mana

    def get_mana(self) -> int:
        return self.__mana

    def draw_card(self) -> None:
        card_drawn = self.__deck.draw_card()
        self.__hand.append(card_drawn)

    def get_hand(self) -> list:
        return self.__hand


class GameState:
    def __init__(self, players: list[Player], battlefield: dict):
        self.players = players
        self.battlefield = battlefield


class GameEngine:
    def __init__(
        self,
        factory: CardFactory,
        strategy: GameStrategy,
        gamestate: GameState,
    ):
        self.factory = factory
        self.strategy = strategy
        self.gamestate = gamestate
        self.nb_turns: int = 0
        self.total_damage: int = 0

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        self.available_types = self.factory.get_supported_types()

    def simulate_turn(self) -> dict:
        pass

    def get_engine_status(self) -> dict:
        return {
            "Factory": self.factory,
            "Strategy": self.strategy.get_strategy_name(),
            "Available types": self.factory.get_supported_types(),
        }

    def get_game_report(self) -> dict:
        return {
            "turn_simulated": self.nb_turns,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "card_created": self.card_created,
        }

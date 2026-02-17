from ex0.CreatureCard import CreatureCard
from ex0.Card import Card
from ex0.Player import Player
from .CardFactory import CardFactory
from .GameStrategy import GameStrategy
from enum import Enum
from random import shuffle
from typing import TypedDict


class TurnPhase(Enum):
    INIT = "Initialization phase:"
    DRAW = "Drawing phase:"
    MAIN = "Main phase:"
    COMBAT = "Combat phase:"
    END = "End phase:"


class Gamestate(TypedDict):
    turn: int
    players: list[Player]
    active_player: Player
    phase: TurnPhase
    game_over: bool
    winner: Player | None
    total_damage: int


class BoardField(TypedDict):
    lifepoints: int
    creatures: list[CreatureCard]


class GameEngine:

    def __init__(
        self,
        name: str,
        battlefield: dict,
    ):
        self.name: str = name
        self.battlefield: dict[Gamestate | BoardField] = battlefield
        self.factory: CardFactory
        self.strategy: GameStrategy
        self.total_damage: int = 0
        self.card_created: list[Card] = []

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        available_types = self.factory.get_supported_types()

        # Create decks for each player and shuffle them
        self.factory.create_themed_deck("large")
        # Yes deck_list is a dict :)
        deck_list: dict = self.factory.create_themed_deck("large")
        for player in self.battlefield[0]['players']:
            player.deck = self.factory.generate_deck(deck_list)
            shuffle(player.deck)
            self.card_created.extend(player.deck)

        # Print engine configuration
        print(f"Configuring {self.name}...")
        print(f"Factory: {self.factory.__class__.__name__}")
        print(f"Strategy: {self.strategy.get_strategy_name()}")
        print(f"Available types: {available_types}")

    def simulate_turn(self) -> dict:
        # Get gamestate status and active player
        gamestate = self.battlefield[0]
        active_player: Player = gamestate.get('active_player')
        print(f"\nSimulating turn {gamestate['turn']} for {active_player.name}...")

        turn_report = self.strategy.execute_turn(active_player.get_hand(),
                                                 self.battlefield)
        self.total_damage += turn_report.get("damage_dealt", 0)
        gamestate['turn'] += 1
        return turn_report

    def get_engine_status(self) -> dict:
        return {
            "Factory": self.factory,
            "Strategy": self.strategy.get_strategy_name(),
            "Available types": self.factory.get_supported_types(),
        }

    def get_game_report(self) -> dict:
        if self.battlefield[0]["winner"].__name__ == 'Gildas':
            message = "Evil has been vanquished, YOU WIN"
        else:
            message = "Piscine Python shall be the end of us all, YOU LOSE"
        return {
            "turn_simulated": self.battlefield[0]['turn'] - 1,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "card_created": self.card_created,  # Why tho
            "winner": self.battlefield[0]['winner'],
            "message": message,
        }

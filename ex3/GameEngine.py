from .CardFactory import CardFactory
from .GameStrategy import GameStrategy
from ex0.Card import Card, Player
from ex1.Deck import Deck
from enum import Enum


class TurnPhase(Enum):
    INIT = "Initialization phase:"
    DRAW = "Drawing phase:"
    MAIN = "Main phase:"
    COMBAT = "Combat phase:"
    END = "End phase:"


class GameError(Exception):
    pass


class TurnPhaseError(GameError):
    pass


class GameEngine:

    def __init__(
        self,
        name: str,
        factory: CardFactory,
        strategy: GameStrategy,
        battlefield: dict,
    ):
        self.name = name
        self.factory = factory
        self.strategy = strategy
        self.total_damage: int = 0
        self.battlefield = battlefield

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        available_types = self.factory.get_supported_types()
        print(f"Configuring {self.name}...")
        print(f"Factory: {self.factory.__class__.__name__}")
        print(f"Strategy: {self.strategy.get_strategy_name()}")
        print(f"Available types: {available_types}")

    def simulate_turn(self) -> dict:
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
            "turn_simulated": self.nb_turns,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "card_created": self.card_created,
            "winner": self.battlefield[0]['winner'],
            "message": message,
        }

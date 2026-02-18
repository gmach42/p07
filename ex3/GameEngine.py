from ex0.CreatureCard import CreatureCard
from ex0.Card import Card
from ex0.Player import Player
from .CardFactory import CardFactory
from .GameStrategy import GameStrategy
from enum import Enum
from typing import TypedDict
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class TurnPhase(Enum):
    """Enum representing the different phases of a turn"""
    INIT = "Initialization phase:"
    DRAW = "Drawing phase:"
    MAIN = "Main phase:"
    COMBAT = "Combat phase:"
    END = "End phase:"


class Gamestate(TypedDict):
    """TypetDict representing the current state of the game"""
    turn: int
    players: list[Player]
    active_player: Player
    phase: TurnPhase
    game_over: bool
    winner: Player | None
    total_damage: int


class BoardField(TypedDict):
    """TypetDict representing the board a player"""
    player: Player
    board: tuple[int, list[CreatureCard]]


class GameEngine:

    def __init__(
        self,
        name: str,
        battlefield: list[Gamestate | dict[str, list[CreatureCard]]],
    ):
        self.name: str = name
        self.battlefield = battlefield
        self.factory: CardFactory
        self.strategy: GameStrategy
        self.total_damage: int = 0
        self.card_created: list[Card] = []
        self.player1: Player = battlefield[0]['players'][0]
        self.player2: Player = battlefield[0]['players'][1]

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:

        # Set factory and strategy for the game engine
        self.factory = factory
        self.strategy = strategy

        # Create decks for each player and shuffle them
        self.factory.create_themed_deck("large")
        deck_list: dict = self.factory.create_themed_deck("large")
        for player in self.battlefield[0]['players']:
            # Generate a deck list of 15 creatures, 10 spells and 5 artifacts
            player.deck = self.factory.generate_deck(deck_list)
            player.deck = Deck.from_card_list(player.name, player.deck)
            player.deck.shuffle()
            self.card_created.extend(player.deck.total_cards)

    def simulate_turn(self) -> dict:
        # Get gamestate status and active player
        gamestate = self.battlefield[0]
        active_player: Player = gamestate.get('active_player')
        hand = active_player.get_hand()
        starting_mana = active_player.get_mana()
        self.print_battlefield()
        print(f"{active_player.name}'s hand: {hand}")
        turn_report = self.strategy.execute_turn(hand, self.battlefield)
        self.total_damage += turn_report.get("damage_dealt", 0)
        # Reset mana to starting value for next turn
        mana_used = turn_report.get('mana_used', 0)
        print(
            f"{active_player.name} has used {mana_used}/"
            f"{starting_mana} mana this turn"
        )
        active_player.mana = starting_mana
        if starting_mana < 8:
            # Increment mana by 1 each turn, up to a maximum of 5
            active_player.mana += 1
        gamestate['turn'] += 1
        # Switch active player for the next turn
        gamestate['active_player'] = (self.player2 if active_player
                                      == self.player1 else self.player1)
        return turn_report

    def get_engine_status(self) -> dict:
        supported_types = self.factory.get_supported_types()
        available_types: dict[str, list[str]] = {}
        for category, types in supported_types.items():
            availables_types_name = [t["name"] for t in types]
            available_types[category] = availables_types_name

        return {
            "Factory": str(self.factory),
            "Strategy": self.strategy.get_strategy_name(),
            "Available types": available_types,
        }

    def get_game_report(self) -> dict:
        if self.battlefield[0]["winner"].name == "Gildas":
            message = "Evil has been vanquished, YOU WIN"
        else:
            message = "Piscine Python shall be the end of us all, YOU LOSE"
        card_created = {
            "creature_cards":
            [c for c in self.card_created if isinstance(c, CreatureCard)],
            "spell_cards":
            [c for c in self.card_created if isinstance(c, SpellCard)],
            "artifact_cards":
            [c for c in self.card_created if isinstance(c, ArtifactCard)]
        }
        return {
            "turn simulated": self.battlefield[0]['turn'] - 1,
            "strategy used": self.strategy.get_strategy_name(),
            "total direct damage": self.total_damage,
            "card created": card_created,  # Why tho
            "winner": self.battlefield[0]['winner'],
            "message": message,
        }

    def print_battlefield(self) -> None:
        player_boards = self.battlefield[1]
        player1_board = [
            c.name for c in player_boards[self.player1.name]
            if isinstance(c, CreatureCard)
        ]
        player2_board = [
            c.name for c in player_boards[self.player2.name]
            if isinstance(c, CreatureCard)
        ]
        print("Current battlefield state:")
        battlefield_state = f"{self.player1.name}: {player1_board} VS " \
                            f"{self.player2.name}: {player2_board}"
        print('\n' + '+' * len(battlefield_state))
        print(battlefield_state)
        print('+' * len(battlefield_state) + '\n')

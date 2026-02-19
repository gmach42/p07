from typing import TypedDict
from ex0.Player import Player
from ex0.TurnPhase import TurnPhase


class GameState(TypedDict):
    """
    TypetDict representing the current state of the game

    Attributes:
        turn (int): The current turn number
        players (list[Player]): The list of players in the game
        active_player (Player): The player whose turn it is
        phase (TurnPhase): The current phase of the turn
        game_over (bool): Whether the game has ended
        winner (Player): The player who won the game
        total_damage (int): The total damage dealt in the game so far
    """
    turn: int
    players: list[Player]
    active_player: Player | None
    phase: TurnPhase
    game_over: bool
    winner: Player | None
    total_damage: int | None

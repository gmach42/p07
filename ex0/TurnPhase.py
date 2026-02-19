from enum import Enum


class TurnPhase(Enum):
    """Enum representing the different phases of a turn"""
    INIT = "Initialization phase:"
    DRAW = "Drawing phase:"
    MAIN = "Main phase:"
    COMBAT = "Combat phase:"
    END = "End phase:"

from .GameEngine import GameEngine, TurnPhase
from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy
from ..ex1 import Deck, SpellCard, ArtifactCard
from ..ex0 import Card, CreatureCard, Player


def print_dict(d: dict) -> str:
    for k, v in d.items():
        print(f"{k.capitalize()}: {v}")


def main():
    # Create players
    gildas = Player("Gildas", 10, Deck([]))
    piscine_python = Player("Piscine Python", 10, Deck([]))

    # Gamestate with turn number and player info
    gamestate: dict[int, list[Player]] = {
        "turn": 1,
        "players": [gildas, piscine_python],
        "active_player": gildas,  # Who is currently playing
        "phase": TurnPhase.INIT,  # init, draw, main, combat, end
        "game_over": False,
        "winner": None,  # Evil shall be vanquished
        "total_damage": 0,  # Why tho
    }

    # Have to implement nonsensical battlefield structure to fit
    # the strategy's expected input
    gildas_battlefield: dict[int, list[CreatureCard]] = {
        'lifepoints': 30,
        'creatures': []
    }

    enemy_battlefield: dict[int, list[Card]] = {
        'lifepoints': 30,
        'creatures': []
    }

    # Battlefield contains gamestate and each respective player's battlefield
    # Would have been more intuitive to have gamestate contain battlefield
    # (or have a separate class for it) but then we would have to change the
    # strategy's expected input so here we are
    battlefield: list = [
        gamestate, {
            "gildas": gildas_battlefield,
            "enemy": enemy_battlefield
        },
    ]
    print("=== DataDeck Game Engine ===\n")

    # Setting up Fantasy Card Game engine
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    game = GameEngine("Fantasy Card Game", factory, strategy, battlefield)
    print_dict(game.get_engine_status())

    print("\nSimulating a game...")
    while not gamestate['game_over']:
        print(f"\n--- Turn {gamestate['turn']} ---")
        print(f"Active Player: {gamestate['active_player'].name}")
        print_dict(game.simulate_turn())
        print(f"End of turn {gamestate['turn'] - 1} status:")

    print("\nGame Report:")
    game_report = game.get_game_report()
    print_dict(game_report)

    print("\n" + "=" * 30)
    print(game_report['message'])
    print("=" * 30)


if __name__ == "__main__":
    main()

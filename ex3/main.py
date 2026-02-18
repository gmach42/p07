from ex0.CreatureCard import CreatureCard
from .GameEngine import GameEngine, TurnPhase, Gamestate
from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy
from ex0.Player import Player


def print_dict(d: dict, except_keys: list[str] = None) -> str:
    if except_keys is None:
        except_keys = []
    for k, v in d.items():
        if k not in except_keys:
            print(f"{k.capitalize()}: {v}")


def print_battlefield(
        battlefield: list[Gamestate | dict[int, list[CreatureCard]]]) -> None:
    gamestate = battlefield[0]
    player_boards = battlefield[1]
    print(f"Active Player: {gamestate['active_player'].name}")
    print("Player Boards:")
    for player, creatures in player_boards.items():
        print(f"{player}: {[creature.name for creature in creatures]}")


def main():
    # Create players
    gildas = Player("Gildas", 1)
    piscine_python = Player("Piscine Python", 1)

    # Gamestate with turn number and player info
    gamestate: Gamestate = {
        "turn": 1,
        "players": [gildas, piscine_python],
        "active_player": gildas,  # Who is currently playing
        "phase": TurnPhase.INIT,  # init, draw, main, combat, end
        "game_over": False,
        "winner": None,  # Evil shall be vanquished
        "total_damage": 0,  # Why tho
    }

    # Battlefield contains gamestate and each respective player's battlefield
    # Would have been more intuitive to have gamestate contain battlefield
    # (or have a separate class for it) but then we would have to change the
    # strategy's expected input so here we are
    battlefield: list[Gamestate | dict[str, list[CreatureCard | Player]]] = [
        gamestate,
        {
            "Gildas": [gildas],
            "Piscine Python": [piscine_python]
        },
    ]
    print("=== DataDeck Game Engine ===\n")

    # Setting up Fantasy Card Game engine
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    game = GameEngine("Fantasy Card Game", battlefield)

    game.configure_engine(factory, strategy)

    print("\nStarting Battle...\n")
    while not gamestate['game_over']:
        active = gamestate['active_player'].name
        print(f"=== Turn {gamestate['turn']} - {active} ===")
        game.simulate_turn()
        print("\nResults of the turn:")
        print(f"  {gildas.name}: {gildas.lifepoints} HP")
        print(f"  {piscine_python.name}: {piscine_python.lifepoints} HP")
        print()

    game_report = game.get_game_report()
    print("=" * 50)
    print(f"{game_report['message']}")
    print("=" * 50)
    print()
    print_dict(game_report,
               except_keys=["message", "card created", "strategy used"])
    print()


if __name__ == "__main__":
    main()

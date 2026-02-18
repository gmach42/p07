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

    # Why not just pass the factory and strategy to the constructor?
    print(f"Configuring {game.name}...")
    game.configure_engine(factory, strategy)
    print(game.get_engine_status()["Factory"])
    print(game.get_engine_status()["Strategy"])
    print_dict(game.get_engine_status()["Available types"])

    print("\nSimulating a game...")
    while not gamestate['game_over']:
        print(f"\n--- Turn {gamestate['turn']} ---")
        print_battlefield(battlefield)
        print_dict(game.simulate_turn())
        print(f"End of turn {gamestate['turn'] - 1} status:")
        print(f"{gildas.name}: {gildas.lifepoints} lifepoints")
        print(f"{piscine_python.name}: {piscine_python.lifepoints} lifepoints")

    print("\nGame Report:")
    game_report = game.get_game_report()
    print_dict(game_report, except_keys=["message", "card_created"])
    print("\nCards created during the game:")
    for category, cards in game_report["card_created"].items():
        print(f"{category.capitalize()}: {[card.name for card in cards]}")

    print("\n" + "=" * 50)
    print(game_report['message'])
    print("=" * 50)


if __name__ == "__main__":
    main()

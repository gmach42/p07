from ex0.CreatureCard import CreatureCard
from ex0.GameState import GameState
from ex0.Player import Player
from ex0.TurnPhase import TurnPhase
from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


def print_dict(d: dict, except_keys: list[str] = None) -> None:
    """
    Helper function to print a dictionary in a readable format,
    excluding specified keys.
    """
    if except_keys is None:
        except_keys = []
    for k, v in d.items():
        if k not in except_keys:
            print(f"{k.capitalize()}: {v}")


def main() -> None:

    print("=== DataDeck Game Engine ===\n")

    # ---------- INITIALIZATION -------------
    gildas = Player("Gildas", 1)
    piscine_python = Player("Piscine Python", 1)
    game_state: GameState = {
        "turn": 1,
        "players": [gildas, piscine_python],
        "active_player": gildas,  # Who is currently playing
        "phase": TurnPhase.INIT,  # init, draw, main, combat, end
        "game_over": False,
        "winner": None,
        "total_damage": 0,  # Why tho
    }

    # Battlefield contains gamestate and each respective player's battlefield
    # Would have been more intuitive to have gamestate contain battlefield
    # (or have a separate class for it) but then we would have to change the
    # strategy's expected input so here we are
    battlefield: list[GameState | dict[str, list[CreatureCard | Player]]] = [
        game_state,
        {
            "Gildas": [gildas],
            "Piscine Python": [piscine_python]
        },
    ]

    # --------- GAME CONFIGURATION ----------
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    game = GameEngine("Fantasy Card Game", battlefield)

    game.configure_engine(factory, strategy)

    # Record the starting deck of each player for endgame display
    starting_deck_player1 = [card for card in gildas.deck.total_cards]
    starting_deck_player2 = [card for card in piscine_python.deck.total_cards]
    starting_deck_player1 = game.sort_cards_by_type_display(
        starting_deck_player1)
    starting_deck_player2 = game.sort_cards_by_type_display(
        starting_deck_player2)

    # ----------- GAME SIMULATION -----------
    print("\nStarting Battle...\n")
    while not game_state['game_over']:
        active = game_state['active_player'].name
        print(f"=== Turn {game_state['turn']} - {active} ===")
        game.simulate_turn()
        print("\nResults of the turn:")
        print(f"  {gildas.name}: {gildas.lifepoints} HP")
        print(f"  {piscine_python.name}: {piscine_python.lifepoints} HP")
        print()

    # ----------- ENDGAME REPORT ------------
    game_report = game.get_game_report()
    print("=" * len(game_report['message']))
    print(f"{game_report['message']}")
    print("=" * len(game_report['message']) + "\n")
    print_dict(game_report,
               except_keys=["message", "card created", "strategy used"])

    print("\nGame Engine Configuration:")
    print_dict(game.get_engine_status(), except_keys=["Available types"])
    print("\nAvailable Cards in the Factory:")
    print_dict(game.get_engine_status()["Available types"])

    # print("\nStarting Deck of each player:")
    # print(f"{gildas.name}:")
    # print_dict(starting_deck_player1)
    # print(f"{piscine_python.name}:")
    # print_dict(starting_deck_player2)

    print()
    # --------------------------------------


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")

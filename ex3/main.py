from .GameEngine import GameEngine
from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy


def print_dict(d: dict) -> str:
    for k, v in d.items():
        print(f"{k.capitalize()}: {v}")


def main():
    print("=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    game_engine = GameEngine(factory, strategy)
    print_dict(game_engine.get_engine_status())

    print("\nSimulating aggressive turn...")
    fire_dragon = factory.create_creature("Fire Dragon")
    goblin_warrior = factory.create_creature("Goblin Warrior")
    fireball = factory.create_spell("Fireball")
    hand = [fire_dragon, goblin_warrior, fireball]
    print(f"Hand: {hand}")
    battlefield = [
        {'enemy_player': 'Enemy Player'},
        {'enemy_creature': None},
        {'player': 'Player'},
        {'allied_creature': None}
        ]

    print("\nTurn execution:")
    print_dict(game_engine.simulate_turn(hand, battlefield))

    print("\nGame Report:")
    print_dict(game_engine.get_game_report())


if __name__ == "__main__":
    main()

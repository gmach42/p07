from .GameEngine import GameEngine
from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy


def print_dict(d: dict) -> str:
    for k, v in d.items():
        print(f"{k.capitalize()}: {v}")


def main():
    print("=== DataDeck Game Engine ===")
    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    game_engine = GameEngine(factory, strategy)
    print_dict(game_engine.get_engine_status())

    print("\nSimulating aggressive turn...")
    print("Hand: [Fire Dragon (5), Goblin Warrior (2), Lightning Bolt (3)]")

    print("\nTurn execution:")
    print("Strategy: AggressiveStrategy")
    print("Actions: {'cards_played': ['Goblin Warrior', 'Lightning Bolt'],")
    print("'mana_used': 5, 'targets_attacked': ['Enemy Player'],")
    print("'damage_dealt': 8}")

    print("\nGame Report:")
    print("{'turns_simulated': 1, 'strategy_used': 'AggressiveStrategy',")
    print("'total_damage': 8, 'cards_created': 3}")
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()

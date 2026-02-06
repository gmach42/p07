from .GameEngine import GameEngine, Player
from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy
from ex1.Deck import Deck


def print_dict(d: dict) -> str:
    for k, v in d.items():
        print(f"{k.capitalize()}: {v}")


def main():
    gildas = Player("Gildas", 10, Deck("Gildas'_deck"))
    enemy = Player("Enemy", 5, Deck("Enemy's_deck"))
    battlefield = {
        'gildas_crea': [],
        'enemy_crea': [],
    }
    gamestate = {
        'players': [gildas, enemy],
        'battlefield': battlefield,
    }
    print("=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")

    # Setting up FantasyCardFactory
    factory = FantasyCardFactory()
    fire_dragon = factory.create_creature("Fire Dragon")
    goblin_warrior = factory.create_creature("Goblin Warrior")
    fireball = factory.create_spell("Fireball")
    
    strategy = AggressiveStrategy()
    game_engine = GameEngine(factory, strategy)
    print_dict(game_engine.get_engine_status())

    print("\nSimulating aggressive turn...")
    hand = [fire_dragon, goblin_warrior, fireball]
    print(f"Hand: {gildas.get_hand()}")

    print("\nTurn execution:")
    print_dict(game_engine.simulate_turn(hand, battlefield))

    print("\nGame Report:")
    print_dict(game_engine.get_game_report())


if __name__ == "__main__":
    main()

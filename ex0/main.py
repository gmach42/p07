from .CreatureCard import CreatureCard
from .Player import Player


def main() -> None:
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    # Create a Goblin Warrior card and a Fire Dragon card
    goblin_warrior = CreatureCard("GoblinWarrior", 3, "Rare", 2, 7)
    fire_dragon = CreatureCard("FireDragon", 5, "Legendary", 7, 5)

    # Create a player
    gildas = Player("Gildas", 8, None)

    # Simulate a game state with Gildas having 8 mana and one enemy creature
    game_state = {
        "player": gildas,
        "mana": 8,
        "ally_crea": [],
        "enemy_crea": [goblin_warrior],
        "match_status": True,
    }

    print("CreatureCard Info:")
    print(fire_dragon.get_card_info(), "\n")

    # Gildas play a Fire Dragon
    print(
        f"Playing {fire_dragon.name} with "
        f"{game_state['mana']} mana available"
    )
    print(f"Playable: {fire_dragon.is_playable(game_state['mana'])}")
    print(f"Play result: {fire_dragon.play(game_state)}\n")

    # Fire Dragon attacks Goblin Warrior:
    print(f"{fire_dragon.name} attacks {goblin_warrior.name}:")
    print(f"Attack result: {fire_dragon.attack_target(goblin_warrior)}\n")

    # Gildas tries to play a new Fire Dragon but...
    print(f"Testing insufficient mana ({game_state['mana']} available):")
    print(f"Playable: {fire_dragon.is_playable(game_state['mana'])}")
    print(f"Play result: {fire_dragon.play(game_state)}\n")

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()

from .CreatureCard import CreatureCard


def main():
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    # Create a Goblin Warrior card and a Fire Dragon card
    goblin_warrior = CreatureCard("GoblinWarrior", 3, "Rare", 2, 7)
    fire_dragon = CreatureCard("FireDragon", 5, "Legendary", 7, 5)

    # Simulate a game state with Gildas having 8 mana and one enemy creature
    game_state = {
        "player": "Gildas",
        "mana": 8,
        "ally_crea": [],
        "enemy_crea": [goblin_warrior],
        "match_status": True,
    }

    print("CreatureCard Info:")
    print(fire_dragon.get_card_info(), "\n")

    # Gildas play a Fire Dragon!
    print(
        f"Playing {fire_dragon.name} with "
        f"{game_state['mana']} mana available"
    )
    print(f"Playable: {fire_dragon.is_playable(game_state['mana'])}")
    fire_dragon.play(game_state)

    # Fire Dragon attacks Goblin Warrior:
    print(f"{fire_dragon.name} attacks {goblin_warrior.name}:")
    fire_dragon.attack_target(goblin_warrior)

    # Gildas tries to play a new Fire Dragon but...
    print(f"Testing insufficient mana ({game_state['mana']} available):")
    print(f"Playable: {fire_dragon.is_playable(game_state['mana'])}")
    fire_dragon.play(game_state)

    print("Abstrat pattern successfully demonstrated! (fun?(nope))")


if __name__ == "__main__":
    main()

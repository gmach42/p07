from ex0.CreatureCard import CreatureCard
from ex0.Player import Player
from ex0.GameState import GameState
from ex0.Card import NotEnoughManaError


def main() -> None:
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    # Create a Goblin Warrior card and a Fire Dragon card
    goblin_warrior = CreatureCard("GoblinWarrior", 3, "Rare", 2, 7)
    fire_dragon = CreatureCard("FireDragon", 5, "Legendary", 7, 5)

    # Create a player
    gildas = Player("Gildas", 8)

    game_state: GameState = {
        "players": [gildas],
        "active_player": gildas,
        "game_over": False,
    }

    print("CreatureCard Info:")
    print(fire_dragon.get_card_info(), "\n")

    # Gildas play a Fire Dragon
    print(f"Playing {fire_dragon.name} with "
          f"{gildas.get_mana()} mana available")
    print(f"Playable: {fire_dragon.is_playable(gildas.get_mana())}")
    print(f"Play result: {fire_dragon.play(game_state)}\n")

    # Deck and hand not implemented yet so we directly spend mana here
    gildas.spend_mana(fire_dragon.cost)

    # Fire Dragon attacks Goblin Warrior:
    print(f"{fire_dragon.name} attacks {goblin_warrior.name}:")
    print(f"Attack result: {fire_dragon.attack_target(goblin_warrior)}\n")

    # Gildas tries to play a new Fire Dragon but...
    print(f"Testing insufficient mana ({gildas.get_mana()} available):")
    print(f"Playable: {fire_dragon.is_playable(gildas.get_mana())}")
    try:
        print(f"Play result: {fire_dragon.play(game_state)}\n")
    except NotEnoughManaError as e:
        print(e, "\n")

    print("Abstract pattern successfully demonstrated!\n")


if __name__ == "__main__":
    main()

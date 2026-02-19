from .EliteCard import EliteCard
from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical
from ex0.Player import Player
from ex0.GameState import GameState
from ex0.CreatureCard import CreatureCard


def print_dict(d: dict) -> None:
    """Helper function to print a dictionary in a readable format"""
    for k, v in d.items():
        print(f"{k.capitalize()}: {v}")


def main() -> None:
    print("\n=== DataDeck Ability System ===")

    gildas = Player("Gildas", 10)

    goblin_warrior = CreatureCard.goblin_warrior()
    gnome_scout = CreatureCard.gnome_scout()
    arcane_warrior = EliteCard(
        name="Arcane Warrior",
        cost=7,
        rarity="Epic",
        combat_type="melee",
        attack_power=5,
        defense=3,
        health=11,
        mana=5,
        knowned_spells={"fireball": 2, "heal": 3},
    )

    print("\nEliteCard capabilities:")
    # List methods from each class to show that EliteCard has all of them
    # Dunder methods are filtered out for clarity
    card_methods = [m for m in dir(Card) if not m.startswith("_")]
    print(f"- Card: {card_methods}")
    combatable_methods = [m for m in dir(Combatable) if not m.startswith("_")]
    print(f"- Combatable: {combatable_methods}")
    magical_methods = [m for m in dir(Magical) if not m.startswith("_")]
    print(f"- Magical: {magical_methods}")

    print("\nEliteCard info:")
    print_dict(arcane_warrior.get_card_info())

    print("\nPlaying Arcane Warrior (Elite Card):\n")
    game_state: GameState = {
        "players": [gildas],
        "active_player": gildas,
        "game_over": False,
        "enemy_creatures": [goblin_warrior, gnome_scout],
    }

    arcane_warrior.play(game_state)

    print("Combat phase:")
    print(f"Attack result: {arcane_warrior.attack(goblin_warrior.__str__())}")
    print(f"Defense result: {arcane_warrior.defend(5)}")

    print("\nMagic phase:")
    targets = game_state["enemy_creatures"]
    print(
        "Spell cast: "
        f"{arcane_warrior.cast_spell('fireball', targets)}"
    )
    print(f"Mana channel: {arcane_warrior.channel_mana(3)}\n")
    print("Multiple interface implementation successful!\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")

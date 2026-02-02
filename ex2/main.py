from .EliteCard import EliteCard
from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical


def print_dict(d: dict) -> str:
    for k, v in d.items():
        print(f"{k.capitalize()}: {v}")


def main():
    print("\n=== DataDeck Ability System ===")

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
    card_methods = [m for m in dir(Card) if not m.startswith("_")]
    print(f"- Card: {card_methods}")
    combatable_methods = [m for m in dir(Combatable) if not m.startswith("_")]
    print(f"- Combatable: {combatable_methods}")
    magical_methods = [m for m in dir(Magical) if not m.startswith("_")]
    print(f"- Magical: {magical_methods}")

    print("\nEliteCard info:")
    print_dict(arcane_warrior.get_card_info())

    print("\nPlaying Arcane Warrior (Elite Card):")
    game_state = {
        "player": "Gildas",
        "mana": 20,
        "played_cards": [],
        "enemy_crea": ["Enemy1", "Enemy2"],
        "match_status": True}
    print(arcane_warrior.play(game_state))

    print("Game state info:")
    print_dict(game_state)

    print("\nCombat phase:")
    print(f"Attack result: {arcane_warrior.attack('Enemy')}")
    print(f"Defense result: {arcane_warrior.defend(5)}")

    print("\nMagic phase:")
    print(
        "Spell cast: "
        f"{arcane_warrior.cast_spell('fireball', game_state['enemy_crea'])}"
    )
    print(f"Mana channel: {arcane_warrior.channel_mana(3)}\n")


if __name__ == "__main__":
    main()

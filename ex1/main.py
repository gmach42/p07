from .Deck import Deck
from ex0.CreatureCard import CreatureCard
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard


def main() -> None:
    print("=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")
    deck = Deck("Gildas")
    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    lightning_bolt = SpellCard(
        "Lightning Bolt", 3, "Common", "Deal 3 damage to target"
    )
    mana_crystal = ArtifactCard(
        "Mana Crystal", 2, "Rare", 10, "+1 mana per turn"
    )
    cards = [fire_dragon, lightning_bolt, mana_crystal]
    for card in cards:
        deck.add_card(card)
    deck.shuffle()
    print(f"Deck stats: {deck.get_deck_stats()}\n")

    print("Drawing and playing cards:")
    game_state = {
        "mana": 10,
        "ally_crea": [],
        "enemy_crea": [CreatureCard("Gnome_scout", 2, "Common", 1, 2)],
    }
    while len(deck.total_cards) > 0:
        card = deck.draw_card()
        result = card.play(game_state)
        print(f"Play result: {result}\n")

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()

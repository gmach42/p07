from ex0.Card import Card
from .Deck import Deck
from ex0.CreatureCard import CreatureCard
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard
from ex0.GameState import GameState
from ex0.Player import Player


def main() -> None:
    print("=== DataDeck Deck Builder ===\n")

    gildas = Player("Gildas", 8)

    print("Building deck with different card types...")

    # Create some cards to add to the deck
    goblin_warrior = CreatureCard.goblin_warrior()
    fire_dragon = CreatureCard.fire_dragon()
    lightning_bolt = SpellCard.lightning_bolt()
    mana_crystal = ArtifactCard.mana_crystal()
    cards: list[Card] = [fire_dragon, lightning_bolt, mana_crystal]

    # Add cards to the deck, shuffle and display
    deck = Deck("Gildas")
    for card in cards:
        deck.add_card(card)
    deck.shuffle()
    print(f"Deck stats: {deck.get_deck_stats()}\n")

    # Create a simple game state for testing card play
    game_state: GameState = {
        "players": [gildas],
        "active_player": gildas,
        "enemy_creatures": [goblin_warrior],
    }

    # Draw and play cards until the deck is empty
    print("Drawing and playing cards:\n")
    while len(deck.total_cards) > 0:
        card = deck.draw_card()
        result = card.play(game_state)
        print(f"Play result: {result}\n")

    print(
        "Polymorphism in action: Same interface, different card behaviors!\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")

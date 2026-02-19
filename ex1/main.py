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
    deck = Deck("Gildas")
    goblin_warrior = CreatureCard.goblin_warrior()
    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    lightning_bolt = SpellCard("Lightning Bolt", 3, "Common",
                               "Deal 3 damage to target")
    mana_crystal = ArtifactCard("Mana Crystal", 2, "Rare", 10,
                                "+1 mana per turn")
    cards: list[CreatureCard | SpellCard
                | ArtifactCard] = [fire_dragon, lightning_bolt, mana_crystal]
    for card in cards:
        deck.add_card(card)
    deck.shuffle()
    print(f"Deck stats: {deck.get_deck_stats()}\n")

    print("Drawing and playing cards:\n")
    game_state: GameState = {
        "players": [gildas],
        "active_player": gildas,
        "enemy_creatures": [goblin_warrior],
    }

    while len(deck.total_cards) > 0:
        card = deck.draw_card()
        result = card.play(game_state)
        print(f"Play result: {result}\n")

    print(
        "Polymorphism in action: Same interface, different card behaviors!\n")


if __name__ == "__main__":
    main()

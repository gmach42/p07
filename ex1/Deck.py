from ex0.Card import Card
import random


class Deck:
    """
    Class representing a deck of cards

    Attributes:
        name (str): The name of the deck
        total_cards (list[Card]): The list of cards in the deck
        card_types (dict[str, int]): Count of each card type in the deck
        avg_cost (float): Average mana cost of cards in the deck
    """

    def __init__(self, name: str):
        """
        Initialize a Deck with a name

        Args:
            name (str): The name of the deck
        """
        self.name = name
        self.total_cards: list[Card] = []
        self.card_types: dict[str, int] = {}
        self.avg_cost: float = self.get_average_cost()

    def get_average_cost(self) -> float:
        """Calculate and return the average cost of cards in the deck"""
        total_cost = 0
        for card in self.total_cards:
            total_cost += card.cost
        if len(self.total_cards) == 0:
            return 0.0
        return float(f"{total_cost / len(self.total_cards):.2f}")

    def add_card(self, card: Card) -> None:
        """Add a card to the deck"""
        card_type: str = card.type.lower()
        if card_type not in self.card_types:
            self.card_types[card_type] = 0
        self.card_types[card_type] += 1
        self.total_cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Remove a card from the deck by name"""
        list_of_card_names: list[str] = [
            card.name for card in self.total_cards
        ]
        if card_name not in list_of_card_names:
            return False
        card_to_remove: Card = (
            self.total_cards[list_of_card_names.index(card_name)])
        self.total_cards.remove(card_to_remove)
        self.card_types[card_to_remove.type.lower()] -= 1
        return True

    def shuffle(self) -> None:
        """Shuffle the deck randomly"""
        random.shuffle(self.total_cards)

    def draw_card(self) -> Card:
        """Draw the top card from the deck"""
        card_drew = self.total_cards[0]
        self.total_cards.pop(0)
        print(f"Drew: {card_drew.name} ({card_drew.type})")
        return card_drew

    def get_deck_stats(self) -> dict:
        """Return statistics about the deck"""
        stats = {
            "total_cards": len(self.total_cards),
            "card_types": self.card_types,
            "average_cost": self.get_average_cost(),
        }
        return stats

    @classmethod
    def from_card_list(cls, name: str, cards: list[Card]) -> "Deck":
        """Class method to create a Deck from a list of Card objects"""
        deck = cls(name)
        for card in cards:
            deck.add_card(card)
        return deck

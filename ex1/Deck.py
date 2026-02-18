from ex0.Card import Card
import random


class Deck:
    def __init__(self, name: str):
        self.name = name
        self.total_cards = []
        self.card_types = {}
        self.avg_cost = self.get_average_cost()

    def get_average_cost(self) -> float:
        total_cost = 0
        for card in self.total_cards:
            total_cost += card.cost
        if len(self.total_cards) == 0:
            return 0.0
        return float(f"{total_cost / len(self.total_cards):.2f}")

    def add_card(self, card: Card) -> None:
        card_type = card.type.lower()
        if card_type not in self.card_types:
            self.card_types[card_type] = 0
        self.card_types[card_type] += 1
        self.total_cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        if card_name not in self.total_cards:
            return False
        self.total_cards.remove(card_name)
        self.card_types[card_name.type.lower()] -= 1
        return True

    def shuffle(self) -> None:
        random.shuffle(self.total_cards)

    def draw_card(self) -> Card:
        card_drew = self.total_cards[0]
        self.total_cards.pop(0)
        print(f"Drew: {card_drew.name} ({card_drew.type})")
        return card_drew

    def get_deck_stats(self) -> dict:
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

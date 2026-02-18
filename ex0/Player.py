from .Card import Card
from ex1.Deck import Deck


class Player:

    def __init__(self, name: str, mana: int):
        self.name: str = name
        self.mana: int = mana
        self.deck: Deck = None
        self.hand: list[Card] = []
        self.lifepoints: int = 30

    def spend_mana(self, mana: int) -> None:
        self.mana -= mana

    def get_mana(self) -> int:
        return self.mana

    def draw_card(self) -> None:
        card_drawn = self.deck.draw_card()
        self.hand.append(card_drawn)
        if self.deck.total_cards == []:
            print(f"{self.name} has no more cards to draw!")
            self.deck = None

    def get_hand(self) -> list[str]:
        hand = [f"{card.name} ({card.cost})" for card in self.hand]
        return hand

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return (
            f"Player(name={self.name}, mana={self.mana}, "
            f"hand={[card.name for card in self.hand]})"
        )

    def play_card(self, card: Card, game_state: dict) -> dict:
        result = {
                "card_played": None,
                "mana_used": 0,
                "effect": None,
        }
        if card not in self.hand:
            print(f"{self.name} does not have {card.name} in hand.")
            return result
        if not card.is_playable(self.mana):
            print(
                f"{self.name} does not have enough mana to play {card.name}.")
            return result
        result = card.play(game_state)
        if result.get("card_played") is not None:
            print(f"{self.name} played {card.name}.")
            self.spend_mana(result["mana_used"])
            self.hand.remove(card)
        return result

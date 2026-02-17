from .Card import Card
from ex1.Deck import Deck


class Player:

    def __init__(self, name: str, mana: int):
        self.name: str = name
        self.__mana: int = mana
        self.deck: Deck | dict = None
        self.__hand: list[Card] = []

    def spend_mana(self, mana: int) -> None:
        self.__mana -= mana

    def get_mana(self) -> int:
        return self.__mana

    def draw_card(self) -> None:
        card_drawn = self.__deck.draw_card()
        self.__hand.append(card_drawn)

    def get_hand(self) -> list[Card]:
        return self.__hand

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return (
            f"Player(name={self.name}, mana={self.__mana}, "
            f"hand={[card.name for card in self.__hand]})"
        )

    def play_card(self, card: Card, game_state: dict) -> dict:
        if card not in self.__hand:
            print(f"{self.name} does not have {card.name} in hand.")
            return None
        if not card.is_playable(self.__mana):
            print(
                f"{self.name} does not have enough mana to play {card.name}.")
            return None
        result = card.play(game_state)
        if result is not None:
            self.spend_mana(result["mana_used"])
            self.__hand.remove(card)
        return result

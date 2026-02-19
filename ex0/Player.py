from ex0.Card import Card
from ex1.Deck import Deck


class Player:
    """
    Class representing a player in the card game

    Attributes:
        name (str): The name of the player
        mana (int): The current mana available to the player
        deck (Deck): The player's deck of cards
        hand (list[Card]): The player's current hand of cards
        lifepoints (int): The player's current life points
    """

    def __init__(self, name: str, mana: int):
        """
        Initialize a Player with a name and starting mana

        Args:
            name (str): The name of the player
            mana (int): The starting mana for the player
        """
        self.name: str = name
        self.mana: int = mana
        self.deck: Deck
        self.hand: list[Card] = []
        self.lifepoints: int = 30

    def spend_mana(self, mana: int) -> None:
        """Spend mana when playing a card"""
        self.mana -= mana

    def get_mana(self) -> int:
        """Get the current mana of the player"""
        return self.mana

    def draw_card(self) -> None:
        """Draw a card from the player's deck"""
        card_drawn = self.deck.draw_card()
        self.hand.append(card_drawn)
        if self.deck.total_cards == []:
            print(f"{self.name} has no more cards to draw!")
            self.deck = None

    def get_hand(self) -> list[str]:
        """Get the current hand of the player"""
        hand = [f"{card.name} ({card.cost})" for card in self.hand]
        return hand

    def __str__(self) -> str:
        """Return simple string representation of the player"""
        return self.name

    def __repr__(self) -> str:
        """Return the detailed string representation of the player"""
        return (
            f"Player(name={self.name}, mana={self.mana}, "
            f"hand={[card.name for card in self.hand]})"
        )

    def play_card(self, card: Card, game_state: dict) -> dict:
        """Play a card from the player's hand"""
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
            self.spend_mana(card.cost)
            self.hand.remove(card)
        return result

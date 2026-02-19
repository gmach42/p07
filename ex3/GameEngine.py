from typing import TypedDict
from ex0.CreatureCard import CreatureCard
from ex0.Card import Card
from ex0.Player import Player
from ex0.GameState import GameState
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class BoardField(TypedDict):
    """TypedDict representing the board of a player"""
    player: Player
    board: list[CreatureCard | Player]


class GameEngine:
    """
    Game engine that manages the game state and turn execution

    Attributes:
        name (str): The name of the game engine
        battlefield (list): The current game battlefield state
        factory (CardFactory): The factory for creating cards
        strategy (GameStrategy): The strategy used for playing
        total_damage (int): Total damage dealt in the game
        card_created (list[Card]): List of all cards created
        player1 (Player): The first player
        player2 (Player): The second player
    """

    def __init__(
        self,
        name: str,
        battlefield: list[GameState | dict[str, list[CreatureCard]]],
    ):
        """
        Initialize the GameEngine

        Args:
            name (str): The name of the game engine
            battlefield (list): The initial battlefield state
        """
        self.name: str = name
        self.battlefield = battlefield
        self.factory: CardFactory
        self.strategy: GameStrategy
        self.total_damage: int = 0
        self.card_created: list[Card] = []
        self.player1: Player = battlefield[0]['players'][0]
        self.player2: Player = battlefield[0]['players'][1]

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        """Configure the game engine with a factory and strategy"""
        # Set factory and strategy for the game engine
        self.factory = factory
        self.strategy = strategy

        # Create decks for each player and shuffle them
        self.factory.create_themed_deck("large")
        deck_list: dict = self.factory.create_themed_deck("large")
        for player in self.battlefield[0]['players']:
            # Generate a deck list of 15 creatures, 10 spells and 5 artifacts
            player.deck = self.factory.generate_deck(deck_list)
            player.deck = Deck.from_card_list(player.name, player.deck)
            player.deck.shuffle()
            self.card_created.extend(player.deck.total_cards)

    def simulate_turn(self) -> dict:
        """Simulate a single turn and return the turn report"""
        # Get gamestate status and active player
        gamestate = self.battlefield[0]
        active_player: Player = gamestate.get('active_player')
        hand = active_player.get_hand()
        starting_mana = active_player.get_mana()
        self.print_battlefield()
        print(f"{active_player.name}'s hand: {hand}")
        turn_report = self.strategy.execute_turn(hand, self.battlefield)
        self.total_damage += turn_report.get("damage_dealt", 0)
        # Reset mana to starting value for next turn
        mana_used = turn_report.get('mana_used', 0)
        print(f"{active_player.name} has used {mana_used}/"
              f"{starting_mana} mana this turn")
        active_player.mana = starting_mana
        if starting_mana < 8:
            # Increment mana by 1 each turn, up to a maximum of 8
            active_player.mana += 1
        gamestate['turn'] += 1
        # Switch active player for the next turn
        gamestate['active_player'] = (self.player2 if active_player
                                      == self.player1 else self.player1)
        return turn_report

    @staticmethod
    def sort_cards_by_type_display(cards: list[Card]) -> dict[str, list[str]]:
        """Sort cards by type for display purposes"""
        sorted_cards_name: dict[str, list[str]] = {
            "creature_cards": [],
            "spell_cards": [],
            "artifact_cards": []
        }
        for card in cards:
            if isinstance(card, CreatureCard):
                sorted_cards_name["creature_cards"].append(card.name)
            elif isinstance(card, SpellCard):
                sorted_cards_name["spell_cards"].append(card.name)
            elif isinstance(card, ArtifactCard):
                sorted_cards_name["artifact_cards"].append(card.name)
        return sorted_cards_name

    def get_engine_status(self) -> dict:
        """Return the current status of the game engine"""
        supported_types = self.factory.get_supported_types()
        available_types: dict[str, list[str]] = {}
        for category, types in supported_types.items():
            availables_types_name = [t["name"] for t in types]
            available_types[category] = availables_types_name

        return {
            "Factory": str(self.factory),
            "Strategy": self.strategy.get_strategy_name(),
            "Available types": available_types,
        }

    def get_game_report(self) -> dict:
        """Generate a report at the end of the game with the final results."""
        if self.battlefield[0]["winner"].name == "Gildas":
            message = "Evil has been vanquished, YOU WIN"
        else:
            message = "Piscine Python shall be the end of us all, YOU LOSE"
        card_created = {
            "creature_cards":
            [c for c in self.card_created if isinstance(c, CreatureCard)],
            "spell_cards":
            [c for c in self.card_created if isinstance(c, SpellCard)],
            "artifact_cards":
            [c for c in self.card_created if isinstance(c, ArtifactCard)]
        }
        return {
            "turn simulated": self.battlefield[0]['turn'] - 1,
            "strategy used": self.strategy.get_strategy_name(),
            "total direct damage": self.total_damage,
            "card created": card_created,  # Why tho
            "winner": self.battlefield[0]['winner'],
            "message": message,
        }

    def print_battlefield(self) -> None:
        """Helper function to print the current state of the battlefield."""
        player_boards = self.battlefield[1]
        player1_board = [
            c.name for c in player_boards[self.player1.name]
            if isinstance(c, CreatureCard)
        ]
        player2_board = [
            c.name for c in player_boards[self.player2.name]
            if isinstance(c, CreatureCard)
        ]
        battlefield_state = f"{self.player1.name}: {player1_board} VS " \
                            f"{self.player2.name}: {player2_board}"
        half_length = (len(battlefield_state) - 13) // 2
        if len(battlefield_state) % 2 == 0:
            extra_plus = '+'
        else:
            extra_plus = ''
        print('\n' + '+' * half_length + ' BATTLEFIELD ' + '+' * half_length +
              extra_plus)
        print(battlefield_state)
        print('+' * len(battlefield_state) + '\n')

from .GameStrategy import GameStrategy
from ex0.Card import Card


class AggressiveStrategy(GameStrategy):

    @staticmethod
    def index_lowest_cost(hand: list) -> int:
        return hand.index(min(c.cost for c in hand))

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """
        Prioritize attacking and dealing damage
        Play low-cost creatures first for board pressure
        Targets enemy creatures and player directly
        Returns comprehensive turn execution results
        """
        while hand:
            card_to_play = hand[self.index_lowest_cost(hand)]
            try:
                card_to_play.play()
            except ValueError:
                continue

        card_played
        mana_used
        targets_attacked
        damaged_dealt

        return {
            'card_played': card_played,
            'mana_used': mana_used,
            'targets_attacked': targets_attacked
            'damaged_dealt': damage_dealt
        }

    def get_strategy_name(self) -> str:
        return super().get_strategy_name()

    def prioritize_targets(self, available_targets: list) -> list:
        return super().prioritize_targets(available_targets)

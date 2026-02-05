from .GameStrategy import GameStrategy
from ex0.Card import Card


class NotEnoughManaError(ValueError):
    print("Not enough mana to play this card.")


class AggressiveStrategy(GameStrategy):

    @staticmethod
    def lowest_cost_card(hand: list) -> Card:
        return min(hand, key=lambda card: card.cost)

    def execute_turn(self, hand: list, battlefield: list, gamestate: dict) -> dict:
        """
        Play low-cost cards first until hand is empty or insufficient mana
        """
        cards_played = []
        total_mana_used = 0
        available_mana = gamestate.get("mana", 10)  # Starting mana per turn

        while hand and available_mana > 0:
            # Find the lowest cost card that can be played
            card = self.lowest_cost_card(hand)

            # Check if we have enough mana to play this card
            if card.cost > available_mana:
                break  # Can't play any more cards

            # Play the card
            game_state = {"mana": available_mana}
            card.play(game_state)

            # Track what we played
            cards_played.append(card)
            available_mana -= card.cost
            total_mana_used += card.cost

            # Remove the played card from hand
            hand.remove(card)

        return {
            'cards_played': cards_played,
            'mana_used': total_mana_used,
            'targets_attacked': targets_attacked
        }

    def get_strategy_name(self) -> str:
        return super().get_strategy_name()

    def prioritize_targets(self, available_targets: list) -> list:
        # Prioritize attacking enemy creatures first, then the player
        prioritized_targets = sorted(available_targets, key=lambda t: (t.type != 'creature', t.health))
        return prioritized_targets

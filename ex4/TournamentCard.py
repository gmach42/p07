from Rankable import Rankable
from ex2 import Combatable
from ex0 import Card


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name, cost, rarity):
        super().__init__(name, cost, rarity)

    # Card's methods
    def play(self, game_state):
        return super().play(game_state)

    # Combatable's methods
    def attack(self, target):
        return super().attack(target)

    def defend(self, incoming_damage):
        return super().defend(incoming_damage)

    def get_combat_stats(self):
        return super().get_combat_stats()

    # Rankable's methods
    def calculate_rating(self):
        return super().calculate_rating()

    def update_wins(self, wins):
        return super().update_wins(wins)

    def update_losses(self, losses):
        return super().update_losses(losses)

    def get_rank_info(self):
        return super().get_rank_info()

    # TournamentCard specific methods
    def get_tournament_stats(self):
        pass

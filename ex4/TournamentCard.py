from Rankable import Rankable
from ex2 import Combatable
from ex0 import Card


class TournamentCard(Card, Combatable, Rankable):

    created_cards: dict[str, int] = {}

    def __init__(self, name, cost, rarity):
        super().__init__(name, cost, rarity)
        self.wins = 0
        self.losses = 0
        self.id = TournamentCard.create_id(name)

    @classmethod
    def create_id(cls, name):
        base_id = name.lower().replace(" ", "_")
        count = cls.created_cards.get(base_id, 0) + 1
        cls.created_cards[base_id] = count
        return f"{base_id}_{count:03d}"

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
        self.wins += wins

    def update_losses(self, losses):
        self.losses += losses

    def get_rank_info(self):
        return super().get_rank_info()

    # TournamentCard specific methods
    def get_tournament_stats(self) -> dict:
        # print("Fire Dragon (ID: dragon_001):")
        # print("- Interfaces: [Card, Combatable, Rankable]")
        # print("- Rating: 1200")
        # print("- Record: 0-0")
        return {
            'name': self.name,
            'id': self.id,
            'interfaces': ['Card', 'Combatable', 'Rankable'],
            'rating': self.calculate_rating(),
            'record': f"{self.wins}-{self.losses}"
        }

from ex0 import Card
from ex2 import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """
    Card class for tournament play with ranking capabilities

    Attributes:
        name (str): The name of the card
        cost (int): The mana cost to play the card
        rarity (str): The rarity of the card
        attack_power (int): Attack power for combat
        defense (int): Defense value
        health (int): Health points
        wins (int): Number of tournament wins
        losses (int): Number of tournament losses
        rating (int): Current rating
        id (str): Unique identifier for the card
    """

    created_cards: dict[str, int] = {}
    BASE_RATING = 1200

    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 attack_power: int,
                 defense: int,
                 health: int):
        """
        Initialize a TournamentCard

        Args:
            name (str): The name of the card
            cost (int): The mana cost to play the card
            rarity (str): The rarity of the card
            attack_power (int): Attack power
            defense (int): Defense value
            health (int): Health points
        """
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.defense = defense
        self.health = health
        self.max_health = health
        self.wins = 0
        self.losses = 0
        self.rating = self.BASE_RATING
        self.id = TournamentCard.create_id(name)

    @classmethod
    def create_id(cls, name: str) -> str:
        """Create a unique ID for the card based on its name"""
        base_id = name.lower().replace(" ", "_")
        count = cls.created_cards.get(base_id, 0) + 1
        cls.created_cards[base_id] = count
        return f"{base_id}_{count:03d}"

    # Card's methods
    def play(self, game_state: dict) -> dict:
        """Play the tournament card in a match context
        I don't use game_state in this exercise since
        it's too different from the main game
        """
        result = {
            "card_played": self.name,
            "id": self.id,
            "effect": "Tournament card deployed",
            "stats": self.get_combat_stats()
        }
        return result

    # Combatable's methods
    def attack(self, target: "TournamentCard") -> dict:
        """Attack a target card in tournament combat"""
        damage = max(0, self.attack_power - target.defense)
        target.health -= damage

        result = {
            "attacker": self.name,
            "attacker_id": self.id,
            "target": target.name,
            "target_id": target.id,
            "damage_dealt": damage,
            "target_remaining_health": target.health,
            "combat_resolved": target.health <= 0
        }
        return result

    def defend(self, incoming_damage: int) -> dict:
        """Defend against incoming damage"""
        actual_damage = max(0, incoming_damage - self.defense)
        self.health -= actual_damage

        result = {
            "defender": self.name,
            "defender_id": self.id,
            "incoming_damage": incoming_damage,
            "defense": self.defense,
            "actual_damage": actual_damage,
            "remaining_health": self.health,
            "defeated": self.health <= 0
        }
        return result

    def get_combat_stats(self) -> dict:
        """Return combat statistics"""
        return {
            "attack": self.attack_power,
            "defense": self.defense,
            "health": self.health,
            "max_health": self.max_health
        }

    # Rankable's methods
    def calculate_rating(self) -> int:
        """Calculate the current rating based on wins and losses"""
        # Rating is automatically calculated in update_wins/update_losses
        return self.rating

    def update_wins(self, wins: int) -> None:
        """Update the number of wins"""
        self.wins += wins
        self.rating += 16

    def update_losses(self, losses: int) -> None:
        """Update the number of losses"""
        self.losses += losses
        self.rating -= 16

    def get_rank_info(self) -> dict:
        """Return ranking information"""
        total_games = self.wins + self.losses
        win_rate = (self.wins / total_games * 100) if total_games > 0 else 0

        return {
            "id": self.id,
            "name": self.name,
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses,
            "win_rate": f"{win_rate:.1f}%"
        }

    # TournamentCard specific methods
    def get_tournament_stats(self) -> dict:
        """Return tournament statistics"""
        return {
            "name": self.name,
            "id": self.id,
            "interfaces": ["Card", "Combatable", "Rankable"],
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}",
            "combat_stats": self.get_combat_stats(),
            "rank_info": self.get_rank_info()
        }

    def reset_health(self) -> None:
        """Reset health to maximum for a new match"""
        self.health = self.max_health

    def __repr__(self) -> str:
        return f"{self.name} (ID: {self.id}, Rating: {self.rating})"

    def display_info(self) -> None:
        print(f"\n{self.name} (ID: {self.id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {self.rating}")
        print(f"- Record: {self.wins}-{self.losses}")

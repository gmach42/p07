from .TournamentCard import TournamentCard
from typing import Optional
import random


class TournamentPlatform:
    """
    Platform for managing tournament card matches and rankings

    Attributes:
        registered_cards (dict): Dictionary of registered cards by ID
        match_history (list): History of all matches played
        total_matches (int): Total number of matches played
    """

    def __init__(self) -> None:
        """Initialize the tournament platform"""
        self.registered_cards: dict[str, TournamentCard] = {}
        self.match_history: list[dict] = []
        self.total_matches: int = 0

    @property
    def total_cards(self) -> int:
        """Get the total number of registered cards"""
        return len(self.registered_cards)

    def register_card(self, card: "TournamentCard") -> str:
        """Register a card in the tournament platform"""

        if card.id in self.registered_cards:
            return card.id

        self.registered_cards[card.id] = card
        return card.id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """Create a match between two cards"""

        # Validate cards exist
        if card1_id not in self.registered_cards:
            return {"error": f"Card with ID {card1_id} not found"}
        if card2_id not in self.registered_cards:
            return {"error": f"Card with ID {card2_id} not found"}

        card1 = self.registered_cards[card1_id]
        card2 = self.registered_cards[card2_id]

        # Reset health for new match
        card1.reset_health()
        card2.reset_health()

        # Simulate combat
        rounds = []
        round_num = 0
        max_rounds = 50  # Prevent infinite loops

        while card1.health > 0 and card2.health > 0 and round_num < max_rounds:
            round_num += 1

            # Card1 attacks Card2
            attack1_result = card1.attack(card2)
            round_data = {
                "round": round_num,
                "attacker": card1.name,
                "defender": card2.name,
                "damage": attack1_result["damage_dealt"],
                "defender_health": card2.health
            }
            rounds.append(round_data)

            # Check if card2 is defeated
            if card2.health <= 0:
                break

            # Card2 attacks Card1
            attack2_result = card2.attack(card1)
            round_data = {
                "round": round_num,
                "attacker": card2.name,
                "defender": card1.name,
                "damage": attack2_result["damage_dealt"],
                "defender_health": card1.health
            }
            rounds.append(round_data)

        # Determine winner
        if card1.health > 0:
            winner = card1
            loser = card2
        elif card2.health > 0:
            winner = card2
            loser = card1
        else:
            # Draw (shouldn't happen but handle it)
            winner = None
            loser = None

        # Update rankings
        if winner:
            winner.update_wins(1)
            loser.update_losses(1)

        # Create match result with simple format
        self.total_matches += 1
        match_result = {
            "winner": winner.id if winner else None,
            "loser": loser.id if loser else None,
            "winner_rating": winner.rating if winner else None,
            "loser_rating": loser.rating if loser else None,
            "card1_name": card1.name,
            "card2_name": card2.name,
            "rounds": round_num
        }

        # Also store detailed history
        detailed_result = {
            "match_id": self.total_matches,
            "card1": {
                "name": card1.name,
                "id": card1.id,
                "final_health": card1.health
            },
            "card2": {
                "name": card2.name,
                "id": card2.id,
                "final_health": card2.health
            },
            "winner": {
                "name": winner.name,
                "id": winner.id,
                "new_rating": winner.rating
            } if winner else None,
            "loser": {
                "name": loser.name,
                "id": loser.id,
                "new_rating": loser.rating
            } if loser else None,
            "rounds": round_num,
            "round_details": rounds[:10]  # First 10 rounds
        }

        self.match_history.append(detailed_result)
        return match_result

    def get_leaderboard(self) -> list[dict]:
        """Return the current tournament leaderboard"""
        if not self.registered_cards:
            return []

        # Sort by rating, then by wins
        sorted_cards = sorted(self.registered_cards.values(),
                              key=lambda c: (c.rating, c.wins),
                              reverse=True)

        leaderboard = []
        for rank, card in enumerate(sorted_cards, 1):
            leaderboard.append({
                "rank": rank,
                "name": card.name,
                "id": card.id,
                "rating": card.rating,
                "wins": card.wins,
                "losses": card.losses,
                "record": f"{card.wins}-{card.losses}"
            })

        return leaderboard

    def generate_tournament_report(self) -> dict:
        """Generate a comprehensive tournament report"""
        if not self.registered_cards:
            return {"error": "No cards registered in tournament"}

        leaderboard = self.get_leaderboard()

        # Calculate statistics
        total_cards = len(self.registered_cards)
        total_wins = sum(card.wins for card in self.registered_cards.values())
        total_losses = sum(card.losses
                           for card in self.registered_cards.values())

        # Find top performer
        top_card = leaderboard[0] if leaderboard else None

        # Calculate average rating
        avg_rating = sum(
            card.rating
            for card in self.registered_cards.values()) / total_cards

        report = {
            "tournament_summary": {
                "total_cards": total_cards,
                "total_matches": self.total_matches,
                "total_wins": total_wins,
                "total_losses": total_losses,
                "average_rating": round(avg_rating, 2)
            },
            "top_performer":
            top_card,
            "leaderboard":
            leaderboard,
            "recent_matches":
            (self.match_history[-5:] if self.match_history else []),
            "registered_cards": [{
                "name": card.name,
                "id": card.id,
                "stats": card.get_tournament_stats()
            } for card in self.registered_cards.values()]
        }

        return report

    def simulate_random_matches(self, num_matches: int) -> list[dict]:
        """Simulate random matches between registered cards"""
        if len(self.registered_cards) < 2:
            return [{"error": "Need at least 2 cards to simulate matches"}]

        results = []
        card_ids = list(self.registered_cards.keys())

        for _ in range(num_matches):
            # Pick two random different cards
            card1_id, card2_id = random.sample(card_ids, 2)
            result = self.create_match(card1_id, card2_id)
            results.append(result)

        return results

    def get_card_stats(self, card_id: str) -> Optional[dict]:
        """Get detailed statistics for a specific card"""
        if card_id not in self.registered_cards:
            return None

        card = self.registered_cards[card_id]
        return card.get_tournament_stats()

    def __repr__(self) -> str:
        return (f"TournamentPlatform(cards={len(self.registered_cards)}, "
                f"matches={self.total_matches})")

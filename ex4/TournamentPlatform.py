from .TournamentCard import TournamentCard
from typing import Optional


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
        """Create a match between two cards and return match result"""

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
        max_rounds = 50

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
            # Draw if both cards at 0 health
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

        self.match_history.append(match_result)
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
        """Generate the tournament report"""
        if not self.registered_cards:
            return {"error": "No cards registered in tournament"}

        leaderboard = self.get_leaderboard()

        # Calculate statistics
        total_cards = len(self.registered_cards)

        # Find top performer
        top_card = leaderboard[0] if leaderboard else None

        # Calculate average rating
        avg_rating = sum(
            card.rating
            for card in self.registered_cards.values()) / total_cards

        report = {
            "tournament_summary": {
                "total_cards": total_cards,
                "matches_played": self.total_matches,
                "average_rating": round(avg_rating)
            },
            "top_performer":
            top_card,
            "leaderboard":
            leaderboard,
            "registered_cards": [{
                "name": card.name,
                "id": card.id,
                "stats": card.get_tournament_stats()
            } for card in self.registered_cards.values()]
        }

        return report

    def get_card_stats(self, card_id: str) -> Optional[dict]:
        """Get detailed statistics for a specific card"""
        if card_id not in self.registered_cards:
            return None

        card = self.registered_cards[card_id]
        return card.get_tournament_stats()

    def __repr__(self) -> str:
        return (f"TournamentPlatform(cards={len(self.registered_cards)}, "
                f"matches={self.total_matches})")

    def display_leaderboard(self) -> None:
        """Display the current tournament leaderboard"""
        leaderboard = self.get_leaderboard()
        for i, card_data in enumerate(leaderboard, 1):
            print(f"{i}. {card_data['name']} - "
                  f"Rating: {card_data['rating']} "
                  f"({card_data['wins']}-{card_data['losses']})")

    def simulate_tournament(self) -> None:
        """Simulate a full tournament with all registered cards"""
        card_ids = list(self.registered_cards.keys())
        counter = 1
        for i in range(len(card_ids)):
            for j in range(i + 1, len(card_ids)):
                print(f"Match {counter}:",
                      self.create_match(card_ids[i], card_ids[j]))
                counter += 1

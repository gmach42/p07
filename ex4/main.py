"""
Exercise 4 - Tournament Platform Demonstration

This module demonstrates the tournament system with multiple inheritance.
Shows TournamentCard (Card + Combatable + Rankable) and TournamentPlatform
with registration, matchmaking, and leaderboard management.
"""

from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    """
    Demonstrate the tournament platform system.

    Creates two tournament cards, registers them, simulates a match,
    and displays the leaderboard and platform statistics.
    """
    print("=== DataDeck Tournament Platform ===")

    # Create tournament platform
    tournament = TournamentPlatform()

    print("\nRegistering Tournament Cards...")

    # Create tournament cards
    fire_dragon = TournamentCard(name="Fire Dragon",
                                 cost=5,
                                 rarity="Legendary")
    ice_wizard = TournamentCard(name="Ice Wizard", cost=4, rarity="Epic")

    # Set initial ratings
    fire_dragon.rating = 1200
    ice_wizard.rating = 1150

    # Register cards
    tournament.register_card(fire_dragon)
    tournament.register_card(ice_wizard)

    # Display initial card info
    print(f"\n{fire_dragon.name} (ID: {fire_dragon.id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {fire_dragon.rating}")
    print(f"- Record: {fire_dragon.wins}-{fire_dragon.losses}")

    print(f"\n{ice_wizard.name} (ID: {ice_wizard.id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {ice_wizard.rating}")
    print(f"- Record: {ice_wizard.wins}-{ice_wizard.losses}")

    # Create match
    print("\nCreating tournament match...")
    match_result = tournament.create_match(fire_dragon.id, ice_wizard.id)

    print(f"Match result: 'winner': '{match_result['winner']}', "
          f"'loser': '{match_result['loser']}',")
    print(f"'winner_rating': {match_result['winner_rating']}, "
          f"'loser_rating': {match_result['loser_rating']}")

    # Display leaderboard
    print("\nTournament Leaderboard:")
    leaderboard = tournament.get_leaderboard()
    for i, card_data in enumerate(leaderboard, 1):
        print(f"{i}. {card_data['name']} - "
              f"Rating: {card_data['rating']} "
              f"({card_data['wins']}-{card_data['losses']})")

    # Display platform report
    print("\nPlatform Report:")
    report = tournament.generate_tournament_report()
    summary = report["tournament_summary"]
    print(report)
    print(f"'total_cards': {summary['total_cards']}, "
          f"'matches_played': {summary['total_matches']},")
    print(f"'avg_rating': {int(summary['average_rating'])}, "
          f"'platform_status': 'active'")

    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()

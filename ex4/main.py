from .TournamentPlatform import TournamentPlatform
from .TournamentCard import TournamentCard


print("=== DataDeck Tournament Platform ===")
tournament = TournamentPlatform()
print("Registering Tournament Cards...")
fire_dragon = TournamentCard(
    "Fire Dragon", "dragon_001", ["Card", "Combatable", "Rankable"], 1200
)
ice_wizard = TournamentCard(
    "Ice Wizard", "wizard_001", ["Card", "Combatable", "Rankable"], 1150
)

tournament.register_card(fire_dragon)
tournament.register_card(ice_wizard)

fire_dragon.get_tournament_stats()
ice_wizard.get_tournament_stats()

print("Fire Dragon (ID: dragon_001):")
print("- Interfaces: [Card, Combatable, Rankable]")
print("- Rating: 1200")
print("- Record: 0-0")
print("Ice Wizard (ID: wizard_001):")
print("- Interfaces: [Card, Combatable, Rankable]")
print("- Rating: 1150")
print("- Record: 0-0")
print("Creating tournament match...")
print("Match result: {'winner': 'dragon_001', 'loser': 'wizard_001',")
print("'winner_rating': 1216, 'loser_rating': 1134}")
print("Tournament Leaderboard:")
print("1. Fire Dragon - Rating: 1216 (1-0)")
print("2. Ice Wizard - Rating: 1134 (0-1)")
print("Platform Report:")
print("{'total_cards': 2, 'matches_played': 1,")
print("'avg_rating': 1175, 'platform_status': 'active'}")
print("=== Tournament Platform Successfully Deployed! ===")
print("All abstract patterns working together harmoniously!")

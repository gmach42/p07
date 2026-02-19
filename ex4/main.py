from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:

    print("\n=== DataDeck Tournament Platform ===")

    tournament = TournamentPlatform()

    print("\nRegistering Tournament Cards...")

    # Create tournament cards
    dracaufeu = TournamentCard(name="Dracaufeu",
                               cost=5,
                               rarity="Legendary",
                               attack_power=6,
                               defense=5,
                               health=6)
    tortank = TournamentCard(name="Tortank",
                             cost=4,
                             rarity="Epic",
                             attack_power=3,
                             defense=5,
                             health=7)
    pikachu = TournamentCard(name="Pikachu",
                             cost=3,
                             rarity="Rare",
                             attack_power=7,
                             defense=2,
                             health=3)
    florizarre = TournamentCard(name="Florizarre",
                                cost=4,
                                rarity="Epic",
                                attack_power=4,
                                defense=4,
                                health=5)
    pikachu2 = TournamentCard(name="Pikachu",
                              cost=3,
                              rarity="Rare",
                              attack_power=7,
                              defense=2,
                              health=3)

    # Set initial non default initial ratings
    pikachu2.rating = 1150
    tortank.rating = 1225
    pikachu.rating = 1250

    # Register cards
    tournament.register_card(dracaufeu)
    tournament.register_card(tortank)
    tournament.register_card(florizarre)
    tournament.register_card(pikachu)
    tournament.register_card(pikachu2)

    # Display initial card info
    dracaufeu.display_info()
    tortank.display_info()
    florizarre.display_info()
    pikachu.display_info()
    pikachu2.display_info()

    # Create match and display res
    print("\nCreating tournament...")
    tournament.simulate_tournament()

    # Display leaderboard
    print("\nTournament Leaderboard:")
    tournament.display_leaderboard()

    # Display platform report
    print("\nPlatform Report:")
    report = tournament.generate_tournament_report()
    summary = report["tournament_summary"]
    print(summary, "\n")
    print("Top Performer:", str(report["top_performer"]) + "\n")

    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!\n")


if __name__ == "__main__":
    main()

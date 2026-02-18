from .GameStrategy import GameStrategy
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from .GameEngine import Player, TurnPhase
from operator import attrgetter


class AggressiveStrategy(GameStrategy):

    def __init__(self):
        self.total_damage: int = 0

    def execute_turn(self, hand: list, battlefield: list[dict]) -> dict:
        """Execute the turn and returns a list of all the action done"""

        # Get gamestate status
        gamestate = battlefield[0]

        if gamestate['phase'] is not TurnPhase.END and gamestate[
                'phase'] is not TurnPhase.INIT:
            raise ValueError("The turn cannot begin, "
                             "another turn is already taking place...")

        # Get all game data
        active_player: Player = gamestate.get('active_player')
        active_board: list = battlefield[1].get(active_player.name)
        opposite_player = [
            p for p in gamestate.get('players', []) if p != active_player
        ][0]
        opposite_board: dict = battlefield[1].get(opposite_player.name)

        # Draw phase
        gamestate['phase'] = TurnPhase.DRAW
        if active_player.deck is not None:
            active_player.draw_card()
        else:
            print(f"{active_player.name} has no deck to draw from!")
        print(f"Current hand: {active_player.get_hand()}")

        # Main Phase, active player can play his/her cards
        gamestate['phase'] = TurnPhase.MAIN
        targets: list = self.prioritize_targets(opposite_board)
        targets_attacked: set = set()
        direct_damage_dealt: int = 0
        cards_played, mana_used = self.play_main_phase(active_player,
                                                       gamestate)
        for creature in cards_played:
            if isinstance(creature, CreatureCard):
                active_board.extend([creature])
                print(
                    f"{creature.name} has been summoned to the battlefield for "
                    f"{active_player.name}.")

        # Combat phase, prioritize dealing damage and targeting enemy
        # player and creatures
        gamestate['phase'] = TurnPhase.COMBAT
        if not active_board:
            print(
                f"No creatures available for {active_player.name} to attack.")
        else:
            active_creatures = [
                creature for creature in active_board
                if isinstance(creature, CreatureCard)
            ]
            for creature in active_creatures:
                if targets:
                    target = targets[0]  # Get the highest priority target

                    # Check if target is a Player or a Creature
                    if isinstance(target, Player):
                        # Attack player directly
                        print(
                            "No creatures available, targeting enemy player directly"
                        )
                        damage_dealt = creature.attack
                        target.lifepoints -= damage_dealt
                        targets_attacked.add(target.name)
                        direct_damage_dealt += damage_dealt
                        self.total_damage += damage_dealt
                        print(
                            f"{creature.name} attacked {target.name} directly "
                            f"dealing {damage_dealt} damage.")
                    else:
                        # Attack creature
                        attack_result = creature.attack_target(target)
                        targets_attacked.add(target.name)
                        damage_dealt = attack_result.get("damage_dealt", 0)
                        print(f"{creature.name} attacked {target.name} "
                              f"dealing {damage_dealt} damage.")
                        if attack_result.get("combat_resolved"):
                            opposite_board.remove(target)
                            targets.remove(target)
                            print(f"{target.name} has been destroyed!")
                            if targets:
                                target = targets[0]
                else:
                    print(f"No targets left for {creature.name} to attack.")

        # End Phase check the status of the game
        gamestate['phase'] = TurnPhase.END
        if opposite_board[0].lifepoints <= 0:
            gamestate['game_over'] = True
            gamestate['winner'] = active_player
            print(gamestate)

        return {
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': targets_attacked,
            'damage_dealt': direct_damage_dealt,
        }

    def get_strategy_name(self) -> str:
        return super().get_strategy_name()

    def prioritize_targets(self, available_targets: list) -> list:
        """
        Prioritize attacking low health enemy creatures first, low attack
        second, and if no creatures are available, target the enemy player
        directly
        """
        opposite_player = [
            p for p in available_targets if isinstance(p, Player)
        ][0]
        opposite_board = [
            crea for crea in available_targets
            if isinstance(crea, CreatureCard)
        ]
        if not opposite_board:  # No creatures on battlefield
            return [opposite_player]  # Return as list, not just the player

        prioritized_targets = sorted(opposite_board,
                                     key=lambda c: (c.health, c.attack))
        prioritized_targets.append(
            opposite_player)  # Add player as last target
        print(f"Prioritized targets: {[t.name for t in prioritized_targets]}")
        return prioritized_targets

    def play_main_phase(self, player: Player,
                        gamestate: dict) -> tuple[list[Card], int]:

        hand: list[Card] = sorted(player.hand, key=attrgetter('cost'))
        mana_start: int = player.get_mana()

        creatures: list[CreatureCard] = [
            c for c in hand if isinstance(c, CreatureCard)
        ]
        spells: list[SpellCard] = [s for s in hand if isinstance(s, SpellCard)]
        artifacts: list[ArtifactCard] = [
            a for a in hand if isinstance(a, ArtifactCard)
        ]

        played_cards: list[Card] = []

        # Play crea first then spells and finally artifact (Strategy choice)
        played_cards.extend(self.play_cards(creatures, player, gamestate))
        played_cards.extend(self.play_cards(spells, player, gamestate))
        played_cards.extend(self.play_cards(artifacts, player, gamestate))

        mana_spend = mana_start - player.get_mana()
        return played_cards, mana_spend

    def play_cards(self, cards: list[Card], player: Player,
                   gamestate: dict) -> list[Card]:
        played = []
        play_result: dict = {}
        for card in cards:
            if player.get_mana() >= card.cost:
                play_result = player.play_card(card, gamestate)
                played.append(card)
                print(
                    f"Played {card.name} with effect: {play_result.get('effect')}"
                )
            else:
                print(f"Not enough mana to play {card.name}")
        return played

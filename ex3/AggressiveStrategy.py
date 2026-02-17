from .GameStrategy import GameStrategy
from ..ex0 import Card, CreatureCard
from ..ex1 import SpellCard, ArtifactCard
from .GameEngine import Player, TurnPhase, TurnPhaseError
from operator import attrgetter


class AggressiveStrategy(GameStrategy):

    def __init__(self):
        self.total_damage: int = 0

    def execute_turn(
        self, hand: list, battlefield: list[dict,
                                            dict[dict[int, list[CreatureCard]],
                                                 dict[int,
                                                      list[CreatureCard]]]]
    ) -> dict:
        """Execute the turn and returns a list of all the action done"""

        # Get gamestate status
        gamestate = battlefield[0]

        if gamestate['phase'] is not TurnPhase.END or gamestate[
                'phase'] is not TurnPhase.INIT:
            raise TurnPhaseError("The turn cannot begin, "
                                 "another turn is already taking place...")

        # Get all game data
        active_player: Player = gamestate.get('active_player')
        active_battlefield: dict = battlefield[1].get(active_player.name)
        opposite_player = [
            p for p in gamestate.get('players', []) if p != active_player
        ][0]
        opposite_battlefield: dict = battlefield[1].get(opposite_player.name)

        # Draw phase
        gamestate['phase'] = TurnPhase.DRAW
        active_player.draw_card()

        # Main Phase, active player can play his/her cards
        gamestate['phase'] = TurnPhase.MAIN
        targets: list = self.prioritize_targets(opposite_battlefield)
        targets_attacked: set = {}
        direct_damage_dealt: int = 0
        cards_played, mana_used = self.play_main_phase(active_player,
                                                       gamestate)

        # Combat phase, prioritize dealing damage and targeting enemy
        # player and creatures
        gamestate['phase'] = TurnPhase.COMBAT
        for creature in active_battlefield['creatures']:
            target: CreatureCard = targets[0]
            _, target, damage_dealt, _ = creature.attack_target(target)
            if target.name == opposite_player.name:
                direct_damage_dealt += damage_dealt
                opposite_battlefield['lifepoints'] -= damage_dealt
            targets_attacked.add(target)
            if target.health <= 0:
                targets.pop(0)

        # End Phase check the status of the game
        gamestate['phase'] = TurnPhase.END
        if opposite_battlefield['lifepoints'] <= 0:
            gamestate['game_over'] = True
            gamestate['winner'] = active_player
            print(gamestate)
        gamestate['turn'] += 1

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
        prioritized_targets = sorted(available_targets['creatures'],
                                     key=lambda c: (c.health, c.attack))
        print(f"Prioritized targets: {prioritized_targets}")
        return prioritized_targets

    def play_main_phase(self, player: Player,
                        gamestate: dict) -> tuple[list[Card], int]:

        hand: list[Card] = sorted(player.get_hand(), key=attrgetter('cost'))
        mana_start: int = player.get_mana

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
        for card in cards:
            if player.get_mana() >= card.cost:
                card_played, mana_used, effect = player.play_card(
                    card, gamestate)
                played.append(card_played)
                player.spend_mana(mana_used)
                print(f"Played {card_played} with effect: {effect}")
            else:
                print(f"Not enough mana to play {card.name}")
        return played

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex0.GameState import GameState
from ex0.TurnPhase import TurnPhase
from ex0.Player import Player
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.GameStrategy import GameStrategy
from operator import attrgetter


class AggressiveStrategy(GameStrategy):
    """
    Aggressive game strategy that prioritizes dealing damage

    Attributes:
        total_damage (int): Total damage dealt using this strategy
    """

    def __init__(self):
        """Initialize the aggressive strategy"""
        self.total_damage: int = 0

    def execute_turn(self, hand: list, battlefield: list[dict]) -> dict:
        """Execute the turn and return a dict of all actions performed"""

        # Get gamestate status
        gamestate: GameState = battlefield[0]

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
        opposite_board: list[Player | CreatureCard] = (battlefield[1].get(
            opposite_player.name))

        # Draw phase
        gamestate['phase'] = TurnPhase.DRAW
        if active_player.deck is not None:
            active_player.draw_card()

        # Main Phase, active player can play his/her cards
        gamestate['phase'] = TurnPhase.MAIN
        targets_attacked: set = set()
        direct_damage_dealt: int = 0
        cards_played, mana_used = (self.play_main_phase(
            active_player, gamestate))

        # Track newly summoned creatures (can't attack first turn)
        newly_summoned: list[CreatureCard] = []
        for creature in cards_played:
            if isinstance(creature, CreatureCard):
                active_board.append(creature)
                newly_summoned.append(creature)
                print(f"{creature.name} enters the battlefield")

        spell_played: list[SpellCard] = [
            s for s in cards_played if isinstance(s, SpellCard)
        ]

        # Combat phase, prioritize dealing damage and targeting enemy
        # player and creatures
        gamestate['phase'] = TurnPhase.COMBAT

        # Get prioritized targets for combat
        targets: list[Player | CreatureCard] = (
            self.prioritize_targets(opposite_board))

        # Spell cycle
        if spell_played:
            ta, dd = (self.spell_combat_phase(spell_played, active_player,
                                              opposite_board, targets))
            targets_attacked.update(ta)
            direct_damage_dealt += dd

        # Creature cycle
        if not active_board:
            pass
        else:
            # Only creatures that were NOT just summoned can attack
            active_creatures = [
                creature for creature in active_board
                if isinstance(creature, CreatureCard)
                and creature not in newly_summoned
            ]
            if active_creatures:
                ta, dd = (self.creature_combat_phase(active_creatures,
                                                     opposite_board, targets))
                targets_attacked.update(ta)
                direct_damage_dealt += dd

        # End Phase check the status of the game
        gamestate['phase'] = TurnPhase.END
        if opposite_player.lifepoints <= 0:
            opposite_player.lifepoints = 0
            gamestate['game_over'] = True
            gamestate['winner'] = active_player

        return {
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': targets_attacked,
            'damage_dealt': direct_damage_dealt,
        }

    def get_strategy_name(self) -> str:
        """Return the name of the strategy"""
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
        return prioritized_targets

    def play_main_phase(self, player: Player,
                        gamestate: dict) -> tuple[list[Card], int]:
        """Play the main phase: sort hand and play cards by priority"""

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
        """Play cards from hand if player has enough mana"""
        played = []
        for card in cards:
            if player.get_mana() >= card.cost:
                player.play_card(card, gamestate)
                played.append(card)
                print(f"Played {card.name}")
        return played

    def creature_combat_phase(self, active_board: list, opposite_board: list,
                              targets: list) -> tuple[set, int]:
        targets_attacked: set = set()
        direct_damage_dealt: int = 0

        for creature in active_board:
            if targets:
                target = targets[0]  # Get the highest priority target

                # Check if target is a Player or a Creature
                if isinstance(target, Player):
                    # Attack player directly
                    damage_dealt = creature.attack
                    target.lifepoints -= damage_dealt
                    targets_attacked.add(target.name)
                    direct_damage_dealt += damage_dealt
                    self.total_damage += damage_dealt
                    print(f"{creature.name} attacks "
                          f"{target.name} for {damage_dealt} damage")
                else:
                    # Attack creature on board
                    attack_result = creature.attack_target(target)
                    targets_attacked.add(target.name)
                    damage_dealt = attack_result.get("damage_dealt", 0)
                    print(f"{creature.name} attacks "
                          f"{target.name} for {damage_dealt} damage")
                    if attack_result.get("combat_resolved"):
                        opposite_board.remove(target)
                        targets.remove(target)
                        print(f"{target.name} destroyed!")
                        if targets:
                            target = targets[0]

        return targets_attacked, direct_damage_dealt

    def spell_combat_phase(self, spell_played: list[SpellCard],
                           active_player: Player, opposite_board: list,
                           targets: list) -> tuple[set, int]:
        targets_attacked: set = set()
        direct_damage_dealt: int = 0

        for spell in spell_played:
            if spell.effect_type == "damage":
                if not targets:
                    continue
                target = targets[0]
                if isinstance(target, Player):
                    # Attack player directly
                    damage_dealt = spell.cost
                    target.lifepoints -= damage_dealt
                    targets_attacked.add(target.name)
                    direct_damage_dealt += damage_dealt
                    self.total_damage += damage_dealt
                    print(f"{spell.name} hits {target.name} "
                          f"for {damage_dealt} damage")
                else:
                    # Attack creature on board
                    damage_dealt = spell.cost
                    targets_attacked.add(target.name)
                    target.health -= damage_dealt
                    print(f"{spell.name} hits {target.name} "
                          f"for {damage_dealt} damage")
                    if target.health <= 0:
                        opposite_board.remove(target)
                        targets.remove(target)
                        print(f"{target.name} destroyed!")
                        if targets:
                            target = targets[0]
            elif spell.effect_type == "heal":
                # Heal self
                heal_amount = spell.cost
                active_player.lifepoints += heal_amount
                print(f"{spell.name} restores {heal_amount} HP "
                      f"to {active_player.name}")

        return targets_attacked, direct_damage_dealt

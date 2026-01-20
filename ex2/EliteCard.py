from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical


class EliteCard(Card, Combatable, Magical):
    # Card's methods
    def play(self, game_state: dict) -> dict:
        return super().play(game_state)

    # Combatable's methods
    def attack(self, target) -> dict:
        return super().attack(target)

    def defend(self, incoming_damage: int) -> dict:
        return super().defend(incoming_damage)

    def get_combat_stats(self):
        return super().get_combat_stats()

    # Magic-related methods
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return super().cast_spell(spell_name, targets)

    def channel_mana(self, amount: int) -> dict:
        return super().channel_mana(amount)

    def get_magic_stats(self) -> dict:
        return super().get_magic_stats()

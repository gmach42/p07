from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1 import Deck, SpellCard, ArtifactCard


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str) -> CreatureCard:
        return super().create_creature(name_or_power)

    def create_spell(self, name_or_power: str) -> SpellCard:
        return super().create_spell(name_or_power)

    def create_artifact(self, name_or_power: str) -> ArtifactCard:
        return super().create_artifact(name_or_power)

    def create_themed_deck(self, size: str) -> Deck:
        return super().create_themed_deck(size)

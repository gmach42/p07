from .CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1 import SpellCard, ArtifactCard


class FantasyCardFactory(CardFactory):
    supported_types = {
        "creatures": {
            "Fire Dragon": CreatureCard(
                "Fire Dragon", cost=6, rarity="Rare", power=6, toughness=4
            ),
            "Goblin Warrior": CreatureCard(
                "Goblin Warrior", cost=2, rarity="Common", power=2, toughness=1
            ),
            "Gnome Scout": CreatureCard(
                "Gnome Scout", cost=1, rarity="Common", power=1, toughness=1
            ),
        },
        "spells": ["fireball"],
        "artifacts": ["mana_ring"],
    }

    def create_creature(self, name_or_power: str) -> CreatureCard:
        creatures = {
            "Fire Dragon": CreatureCard(
                "Fire Dragon", cost=6, rarity="Rare", power=6, toughness=4
            ),
            "Goblin Warrior": CreatureCard(
                "Goblin Warrior", cost=2, rarity="Common", power=2, toughness=1
            ),
            "Gnome Scout": CreatureCard(
                "Gnome Scout", cost=1, rarity="Common", power=1, toughness=1
            ),
        }

        if name_or_power not in creatures:
            raise ValueError(f"Creature '{name_or_power}' not supported")
        return creatures[name_or_power]

    def create_spell(self, name_or_power: str) -> SpellCard:
        return super().create_spell(name_or_power)

    def create_artifact(self, name_or_power: str) -> ArtifactCard:
        return super().create_artifact(name_or_power)

    def create_themed_deck(self, size: str) -> dict:
        return super().create_themed_deck(size)

    def get_supported_types(self) -> dict:
        return self.supported_types

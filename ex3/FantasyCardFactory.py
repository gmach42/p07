from .CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1 import SpellCard, ArtifactCard


class FantasyCardFactory(CardFactory):
    supported_types = {
        "creatures": [
            CreatureCard.fire_dragon(),
            CreatureCard.goblin_warrior(),
            CreatureCard.gnome_scout(),
        ],
        "spells": [SpellCard.fireball()],
        "artifacts": [ArtifactCard.mana_ring()],
    }

    def create_creature(self, name_or_power: str) -> CreatureCard:
        creatures = {c.name: c for c in self.supported_types["creatures"]}

        if name_or_power not in creatures:
            raise ValueError(f"Creature '{name_or_power}' not supported")
        return creatures[name_or_power]

    def create_spell(self, name_or_power: str) -> SpellCard:
        spells = {s.name: s for s in self.supported_types["spells"]}

        if name_or_power not in spells:
            raise ValueError(f"Spell '{name_or_power}' not supported")
        return spells[name_or_power]

    def create_artifact(self, name_or_power: str) -> ArtifactCard:
        artifacts = {a.name: a for a in self.supported_types["artifacts"]}

        if name_or_power not in artifacts:
            raise ValueError(f"Artifact '{name_or_power}' not supported")
        return artifacts[name_or_power]

    def create_themed_deck(self, size: str) -> dict:
        return super().create_themed_deck(size)

    def get_supported_types(self) -> dict:
        return self.supported_types

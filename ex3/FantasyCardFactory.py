from .CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1 import SpellCard, ArtifactCard


class FantasyCardFactory(CardFactory):
    """
    Factory for creating fantasy-themed cards

    Attributes:
        supported_types (dict): Dictionary of supported card types with stats
    """

    def __init__(self):
        """Initialize the FantasyCardFactory with supported card types"""
        self.supported_types = {
            "creatures": [
                {
                    "name": "Fire Dragon",
                    "cost": 5,
                    "rarity": "Legendary",
                    "attack": 7,
                    "health": 5
                },
                {
                    "name": "Goblin Warrior",
                    "cost": 2,
                    "rarity": "Common",
                    "attack": 2,
                    "health": 1
                },
                {
                    "name": "Ice Wizard",
                    "cost": 4,
                    "rarity": "Rare",
                    "attack": 3,
                    "health": 4
                },
                {
                    "name": "Lightning Elemental",
                    "cost": 3,
                    "rarity": "Uncommon",
                    "attack": 4,
                    "health": 2
                },
                {
                    "name": "Stone Golem",
                    "cost": 6,
                    "rarity": "Rare",
                    "attack": 5,
                    "health": 8
                },
                {
                    "name": "Shadow Assassin",
                    "cost": 3,
                    "rarity": "Uncommon",
                    "attack": 5,
                    "health": 2
                },
                {
                    "name": "Healing Angel",
                    "cost": 4,
                    "rarity": "Rare",
                    "attack": 2,
                    "health": 6
                },
                {
                    "name": "Forest Sprite",
                    "cost": 1,
                    "rarity": "Common",
                    "attack": 1,
                    "health": 1
                },
            ],
            "spells": [
                {
                    "name": "Lightning Bolt",
                    "cost": 3,
                    "rarity": "Common",
                    "effect_type": "damage"
                },
                {
                    "name": "Healing Potion",
                    "cost": 2,
                    "rarity": "Common",
                    "effect_type": "heal"
                },
                {
                    "name": "Fireball",
                    "cost": 4,
                    "rarity": "Uncommon",
                    "effect_type": "damage"
                },
                {
                    "name": "Shield Spell",
                    "cost": 1,
                    "rarity": "Common",
                    "effect_type": "buff"
                },
                {
                    "name": "Meteor",
                    "cost": 8,
                    "rarity": "Legendary",
                    "effect_type": "damage"
                },
                {
                    "name": "Ice Shard",
                    "cost": 2,
                    "rarity": "Common",
                    "effect_type": "damage"
                },
                {
                    "name": "Divine Light",
                    "cost": 5,
                    "rarity": "Rare",
                    "effect_type": "heal"
                },
                {
                    "name": "Magic Missile",
                    "cost": 1,
                    "rarity": "Common",
                    "effect_type": "damage"
                },
            ],
            "artifacts": [
                {
                    "name": "Mana Crystal",
                    "cost": 2,
                    "rarity": "Common",
                    "durability": 5,
                    "effect": "Permanent: +1 mana per turn"
                },
                {
                    "name": "Sword of Power",
                    "cost": 3,
                    "rarity": "Uncommon",
                    "durability": 3,
                    "effect": "Permanent: +2 attack to equipped creature"
                },
                {
                    "name": "Ring of Wisdom",
                    "cost": 4,
                    "rarity": "Rare",
                    "durability": 4,
                    "effect": "Permanent: Draw an extra card each turn"
                },
                {
                    "name": "Shield of Defense",
                    "cost": 5,
                    "rarity": "Rare",
                    "durability": 6,
                    "effect": "Permanent: +3 health to all friendly creatures"
                },
                {
                    "name": "Crown of Kings",
                    "cost": 7,
                    "rarity": "Legendary",
                    "durability": 8,
                    "effect": "Permanent: +1 cost reduction to all cards"
                },
                {
                    "name": "Boots of Speed",
                    "cost": 2,
                    "rarity": "Uncommon",
                    "durability": 2,
                    "effect": "Permanent: Cards cost 1 less mana"
                },
                {
                    "name": "Cloak of Shadows",
                    "cost": 3,
                    "rarity": "Uncommon",
                    "durability": 3,
                    "effect": "Permanent: Creatures have stealth"
                },
                {
                    "name": "Staff of Elements",
                    "cost": 6,
                    "rarity": "Legendary",
                    "durability": 7,
                    "effect": "Permanent: +1 spell damage"
                },
            ]
        }

    def create_creature(self, name_or_power: str) -> CreatureCard:
        """Create a creature card by name"""
        if name_or_power not in [
                c["name"] for c in self.supported_types["creatures"]
        ]:
            raise ValueError(f"Creature '{name_or_power}' not supported")
        card_index = next(
            i for i, c in enumerate(self.supported_types["creatures"])
            if c["name"] == name_or_power)
        card = self.supported_types["creatures"][card_index]
        return CreatureCard(
            name=card["name"],
            cost=card["cost"],
            rarity=card["rarity"],
            attack=card["attack"],
            health=card["health"],
        )

    def create_spell(self, name_or_power: str) -> SpellCard:
        """Create a spell card by name"""
        if name_or_power not in [
                c["name"] for c in self.supported_types["spells"]
        ]:
            raise ValueError(f"Spell '{name_or_power}' not supported")
        card_index = next(i
                          for i, c in enumerate(self.supported_types["spells"])
                          if c["name"] == name_or_power)
        card = self.supported_types["spells"][card_index]
        return SpellCard(
            name=card["name"],
            cost=card["cost"],
            rarity=card["rarity"],
            effect_type=card["effect_type"],
        )

    def create_artifact(self, name_or_power: str) -> ArtifactCard:
        """Create an artifact card by name"""
        if name_or_power not in [
                c["name"] for c in self.supported_types["artifacts"]
        ]:
            raise ValueError(f"Artifact '{name_or_power}' not supported")
        card_index = next(
            i for i, c in enumerate(self.supported_types["artifacts"])
            if c["name"] == name_or_power)
        card = self.supported_types["artifacts"][card_index]
        return ArtifactCard(
            name=card["name"],
            cost=card["cost"],
            rarity=card["rarity"],
            durability=card["durability"],
            effect=card["effect"],
        )

    def create_themed_deck(self, size: str) -> dict:
        """AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH
        :)
        Create a themed deck of the specified size.
        For some obscure reason, this method shall return a dictionary
        instead of a Deck object

        3 sizes are supported: "small", "medium", and "large".
        """
        if size == "small":
            return {
                "creatures": [self.create_creature("Goblin Warrior")],
                "spells": [self.create_spell("Magic Missile")],
                "artifacts": [self.create_artifact("Mana Crystal")],
            }
        elif size == "medium":
            return {
                "creatures": [
                    self.create_creature("Goblin Warrior"),
                    self.create_creature("Ice Wizard"),
                    self.create_creature("Forest Sprite"),
                ],
                "spells": [
                    self.create_spell("Magic Missile"),
                    self.create_spell("Ice Shard"),
                    self.create_spell("Healing Potion"),
                ],
                "artifacts": [
                    self.create_artifact("Mana Crystal"),
                    self.create_artifact("Boots of Speed"),
                ],
            }
        elif size == "large":
            return {
                "creatures": [
                    self.create_creature("Fire Dragon"),
                    self.create_creature("Goblin Warrior"),
                    self.create_creature("Ice Wizard"),
                    self.create_creature("Lightning Elemental"),
                    self.create_creature("Stone Golem"),
                    self.create_creature("Shadow Assassin"),
                    self.create_creature("Healing Angel"),
                    self.create_creature("Forest Sprite"),
                ],
                "spells": [
                    self.create_spell("Lightning Bolt"),
                    self.create_spell("Healing Potion"),
                    self.create_spell("Fireball"),
                    self.create_spell("Shield Spell"),
                    self.create_spell("Meteor"),
                    self.create_spell("Ice Shard"),
                    self.create_spell("Divine Light"),
                    self.create_spell("Magic Missile"),
                ],
                "artifacts": [
                    self.create_artifact("Mana Crystal"),
                    self.create_artifact("Sword of Power"),
                    self.create_artifact("Ring of Wisdom"),
                    self.create_artifact("Shield of Defense"),
                    self.create_artifact("Crown of Kings"),
                    self.create_artifact("Boots of Speed"),
                    self.create_artifact("Cloak of Shadows"),
                    self.create_artifact("Staff of Elements"),
                ],
            }
        else:
            raise ValueError(f"Deck size '{size}' not supported")

    def get_supported_types(self) -> dict:
        """Return the dictionary of supported card types"""
        return self.supported_types

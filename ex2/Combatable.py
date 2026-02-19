from abc import ABC, abstractmethod


class Combatable(ABC):
    """Abstract base class for entities that can engage in combat"""

    @abstractmethod
    def attack(self, target) -> dict:
        """Attack a target and return the result"""
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        """Defend against incoming damage and return the result"""
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        """Return the combat statistics of the entity"""
        pass

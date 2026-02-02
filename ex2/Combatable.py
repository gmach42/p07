from abc import ABC, abstractmethod


class Combatable(ABC):
    @abstractmethod
    def attack(self, target) -> dict:
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        return {
            "combat_type": self.combat_type,
            "attack_power": self.attack_power,
            "defense": self.defense,
            "health": self.health,
        }

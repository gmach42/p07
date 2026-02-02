from abc import ABC, abstractmethod
from typing import Optional


class Magical(ABC):
    def __init__(
        self, mana: int, knowned_spells: Optional[dict[str, int]] = None
    ):
        super().__init__()

        # mana validation
        if mana < 0:
            raise ValueError("mana needs to be null or a positive integer")
        self.mana = mana

        # knowned_spells validation
        if knowned_spells is None:
            self.knowned_spells = {}
        else:
            if not isinstance(knowned_spells, dict):
                raise TypeError("knowned_spells must be a dict")
            for spell_name, cost in knowned_spells.items():
                if not isinstance(spell_name, str):
                    raise TypeError(
                        f"Spell name must be str, here it's {type(spell_name)}"
                        )
                if not isinstance(cost, int) or cost < 0:
                    raise ValueError(
                        f"Spell cost must non-negative int, here it's {cost}"
                    )
        # Copy knowned spells here to avoid conflicts
        self.knowned_spells = dict(knowned_spells)

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        return {
            "mana": self.mana,
            "spell_knowned": self.knowned_spells,
        }

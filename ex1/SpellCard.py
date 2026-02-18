from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        player = game_state["active_player"]
        if not self.is_playable(player.get_mana()):
            print("Cannot play card, not enough mana.")
            return
        result = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.resolve_effect(game_state.get("enemy_crea", [])),
        }
        self.resolve_effect(game_state.get("enemy_crea", []))
        return result

    def resolve_effect(self, targets: list) -> dict:
        for target in targets:
            target.health -= 3
        names = [target.name for target in targets]
        return {"Effect Type": self.effect_type, "Targets": names}

    @classmethod
    def fireball(cls) -> "SpellCard":
        return cls("Fireball", cost=4, rarity="Uncommon", effect_type="Damage")

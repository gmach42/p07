from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        if not self.is_playable(game_state["mana"]):
            print()
            return
        result = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.resolve_effect(game_state.get("enemy_crea", [])),
        }
        game_state["mana"] -= self.cost
        self.resolve_effect(game_state.get("enemy_crea", []))
        print(f"Play result: {result}\n")

    def resolve_effect(self, targets: list) -> dict:
        for target in targets:
            target.health -= 3
        return {"Effect Type": self.effect_type, "Targets": targets}

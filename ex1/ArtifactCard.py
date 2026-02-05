from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str, durability: int, effect: str
    ):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        if not self.is_playable(game_state["mana"]):
            print("")
            return
        result = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.activate_ability(),
        }
        game_state["mana"] -= self.cost
        print(f"Play result: {result}\n")

    def activate_ability(self) -> dict:
        return {"Permanent": self.effect}

    @classmethod
    def mana_ring(cls):
        return cls(
            "Mana Ring", cost=3, rarity="Uncommon", durability=5, effect="Mana Boost"
        )

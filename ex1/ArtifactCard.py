from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str, durability: int, effect: str
    ):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        player = game_state["active_player"]
        if not self.is_playable(player.get_mana()):
            print("")
            return
        result = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.activate_ability(),
        }
        return result

    def activate_ability(self) -> dict:
        return {"Permanent": self.effect}

    @classmethod
    def mana_ring(cls) -> "ArtifactCard":
        return cls(
            name="Mana Ring",
            cost=3,
            rarity="Uncommon",
            durability=5,
            effect="Mana Boost",
        )

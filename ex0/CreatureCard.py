from Card import Card


class CreatureCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int
    ):
        super().__init__(name, cost, rarity)
        if attack > 0:
            self.attack = attack
        else:
            raise ValueError(
                f"Please enter a non-zero positive value "
                f"to set the attack of {self.name}"
            )
        if attack > 0:
            self.health = health
        else:
            raise ValueError(
                f"Please enter a non-zero positive value "
                f"to set the health of {self.name}"
            )

    def play(self, game_state: dict):
        pass

    def attack_target(self):
        pass

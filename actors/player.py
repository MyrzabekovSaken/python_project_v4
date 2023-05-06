from dataclasses import dataclass
from actors.warrior import Warrior

@dataclass
class Player(Warrior):
    pass

    def to_dict(self):
            return {
                "first_name": self.first_name,
                "hp": self.hp,
                "inventory": self.inventory,
                "attack_point": self.attack_point
            }
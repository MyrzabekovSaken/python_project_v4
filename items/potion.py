from dataclasses import dataclass, field

from item import Item
from items.effect import Effect

@dataclass
class Potion(Item):
    duration: int
    effects: list[Effect] = field(default_factory=list)
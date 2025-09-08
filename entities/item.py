import dataclasses
import random


@dataclasses.dataclass
class Item:
    id: int
    name: str
    value: int

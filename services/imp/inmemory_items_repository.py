from entities.item import Item
from services.items_repository import ItemsRepository


class InMemoryItemsRepository(ItemsRepository):
    def __init__(self):
        self.items = {}

    def add_item(self, item: Item):
        self.items[item.id] = item

    def get_items(self) -> list[Item]:
        return list(self.items.values())


class TupleItemsRepository(ItemsRepository):
    def __init__(self):
        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)

    def get_items(self) -> list[Item]:
        return self.items
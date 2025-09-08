from entities.item import Item
from services.items_repository import ItemsRepository


class ItemsService:
    def __init__(self, repo: ItemsRepository):
        self.repo = repo

    def get_items(self) -> list[Item]:
        return self.repo.get_items()

    def add_item(self, item: Item):
        self.repo.add_item(item)

    def get_sum(self) -> int:
        return sum([item.value for item in self.repo.get_items()], 0)
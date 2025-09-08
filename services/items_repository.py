from abc import ABC, abstractmethod

from entities.item import Item


class ItemsRepository(ABC):
    @abstractmethod
    def add_item(self, item: Item):
        raise NotImplemented

    @abstractmethod
    def get_items(self) -> list[Item]:
        raise NotImplemented



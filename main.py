from entities.item import Item
from services.imp.inmemory_items_repository import InMemoryItemsRepository, TupleItemsRepository
from services.items_service import ItemsService


def main():
    tuple_repo = TupleItemsRepository()
    repo = InMemoryItemsRepository()
    service = ItemsService(repo=repo)

    service.add_item(Item(id=1, name='1', value=100))
    service.add_item(Item(id=2, name='2', value=200))
    service.add_item(Item(id=3, name='3', value=300))

    print(service.get_sum())


if __name__ == "__main__":
    main()
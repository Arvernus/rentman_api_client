from enum import Enum


class MateriaalCollectionputResponseSchemaDataItemStockManagement(str, Enum):
    EXCLUDE_FROM_STOCK_TRACKING = "Exclude from stock tracking"
    TRACK_STOCK = "Track stock"

    def __str__(self) -> str:
        return str(self.value)

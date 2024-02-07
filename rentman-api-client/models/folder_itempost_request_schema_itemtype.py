from enum import Enum


class FolderItempostRequestSchemaItemtype(str, Enum):
    EQUIPMENT = "equipment"
    CONTACT = "contact"
    VEHICLE = "vehicle"
    USER = "user"
    CONTAINER = "container"

    def __str__(self) -> str:
        return str(self.value)

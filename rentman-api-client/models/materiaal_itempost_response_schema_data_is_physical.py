from enum import Enum


class MateriaalItempostResponseSchemaDataIsPhysical(str, Enum):
    VIRTUAL_PACKAGE = "Virtual package"
    PHYSICAL_EQUIPMENT = "Physical equipment"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class FilesItempostRequestSchemaPreviewstatus(str, Enum):
    VALUE_False = "False"
    VALUE_True = "True"
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)

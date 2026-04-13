from enum import Enum


class FSCode(str, Enum):
    BS = "BS"
    CF = "CF"
    IS = "IS"

    def __str__(self) -> str:
        return str(self.value)

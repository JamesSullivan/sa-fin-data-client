from enum import Enum


class FSCodeExtended(str, Enum):
    BS = "BS"
    CF = "CF"
    CI = "CI"
    CP = "CP"
    EQ = "EQ"
    IS = "IS"
    OT = "OT"
    UN = "UN"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class ServiceMode(Enum):
    LOCAL = "LOCAL"
    REMOTE = "REMOTE"

    @classmethod
    def from_string(cls, mode: str) -> "ServiceMode":
        if mode is None or (mode := mode.upper()) not in cls.__members__:
            return cls.LOCAL
        else:
            return cls(mode)

import enum

class ConflictStrategy(enum.Enum):
    IGNORE = 1
    RENAME_SOURCE = 2
    DELETE_DESTINATION = 3
    INTERACTIVE = 4
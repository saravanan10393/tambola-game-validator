from enum import Enum

class ClaimType(Enum):
    TOP_ROW = "TOP_ROW"
    MIDDLE_ROW = "MIDDLE_ROW"
    BOTTOM_ROW = "BOTTOM_ROW"
    FAST_FIVE = "FAST_FIVE"
    ALL = "ALL"


class ClaimStatus(Enum):
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"

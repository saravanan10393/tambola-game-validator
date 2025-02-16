"""
Base level assumptions:

1. Ticket numbers are comma separated string of integers.
2. It is the controller responsibility to pass  only the ticket numbers from Ticket Entity.
    Purpose fully designed  to avoid dependency on Ticket Entity.
3. Based on the hard rule of the game that Numbers on the ticket will not  exceed 15 in count and each row has only 5 numbers,
    hard coded the row calculation in code. Did not use the matrix as it involves extra computation.
4. It is the responsibility of Ticket entity to store the ticket numbers effectively using sparse matrix or any other data structure.

"""

from typing import List
from abc import ABC, abstractmethod

from constants import ClaimType, ClaimStatus

class BaseClaimValidator(ABC):
    @abstractmethod
    def validate(self, ticket_numbers: List[int], numbers_announced: List[int]) -> ClaimStatus:
        pass

    def get_claim_status(self, ticket_numbers: List[int], numbers_announced: List[int],
                         expected_strike: int) -> ClaimStatus:
        number_hash = {num: False for num in ticket_numbers}
        strike_count = 0
        claim_status = ClaimStatus.ACCEPTED

        for num in numbers_announced:
            if strike_count == expected_strike:
                claim_status = ClaimStatus.REJECTED
                break
            if number_hash.get(num) is False:
                number_hash[num] = True
                strike_count += 1

        if strike_count < expected_strike:
            claim_status = ClaimStatus.REJECTED

        return claim_status


class AllClaimValidator(BaseClaimValidator):
    def validate(self, ticket_numbers: List[int], numbers_announced: List[int]) -> ClaimStatus:
        if len(numbers_announced) < len(ticket_numbers):
            return ClaimStatus.REJECTED
        return self.get_claim_status(ticket_numbers, numbers_announced, len(ticket_numbers))


class TopRowClaimValidator(BaseClaimValidator):
    def validate(self, ticket_numbers: List[int], numbers_announced: List[int]) -> ClaimStatus:
        top_row = ticket_numbers[:5]
        return self.get_claim_status(top_row, numbers_announced, len(top_row))


class MiddleRowClaimValidator(BaseClaimValidator):
    def validate(self, ticket_numbers: List[int], numbers_announced: List[int]) -> ClaimStatus:
        middle_row = ticket_numbers[5:10]
        return self.get_claim_status(ticket_numbers[5:10], numbers_announced, len(middle_row))


class BottomRowClaimValidator(BaseClaimValidator):
    def validate(self, ticket_numbers: List[int], numbers_announced: List[int]) -> ClaimStatus:
        bottom_row = ticket_numbers[10:15]
        return self.get_claim_status(ticket_numbers[10:15], numbers_announced, len(bottom_row))


class FastFiveClaimValidator(BaseClaimValidator):
    def validate(self, ticket_numbers: List[int], numbers_announced: List[int]) -> ClaimStatus:
        return self.get_claim_status(ticket_numbers, numbers_announced, 5)


class ClaimValidator:
    _strategies = {
        ClaimType.ALL: AllClaimValidator(),
        ClaimType.TOP_ROW: TopRowClaimValidator(),
        ClaimType.MIDDLE_ROW: MiddleRowClaimValidator(),
        ClaimType.BOTTOM_ROW: BottomRowClaimValidator(),
        ClaimType.FAST_FIVE: FastFiveClaimValidator()
    }

    @staticmethod
    def validate(ticket: str, numbers_announced: List[int], claim: ClaimType) -> ClaimStatus:
        ticket_numbers = [int(num) for num in ticket.split(",") if num.isdigit()]
        strategy = ClaimValidator._strategies.get(claim)
        if strategy:
            return strategy.validate(ticket_numbers, numbers_announced)
        return ClaimStatus.REJECTED
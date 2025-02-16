import unittest

import unittest
from claim_validator import ClaimValidator
from constants import ClaimType, ClaimStatus

class TestClaimValidator(unittest.TestCase):
    def setUp(self):
        self.ticket = ("4,16,_,_,48,_,63,76,_,"
                       "7,_,23,38,_,52,_,_,80,"
                       "9,_,25,_,_,56,64,_,83")

    def test_top_row_valid_claim(self):
        numbers_announced = [4, 16, 48, 63, 76]
        result = ClaimValidator.validate(self.ticket, numbers_announced, ClaimType.TOP_ROW)
        self.assertEqual(result, ClaimStatus.ACCEPTED)

    def test_top_row_early_claim(self):
        numbers_announced = [4, 16]
        result = ClaimValidator.validate(self.ticket, numbers_announced, ClaimType.TOP_ROW)
        self.assertEqual(result, ClaimStatus.REJECTED)

    def test_top_row_late_claim(self):
        numbers_announced = [4, 16, 48, 63, 76, 7]
        result = ClaimValidator.validate(self.ticket, numbers_announced, ClaimType.TOP_ROW)
        self.assertEqual(result, ClaimStatus.REJECTED)

    def test_middle_row_valid_claim(self):
        numbers_announced = [7, 23, 38, 52, 80]
        result = ClaimValidator.validate(self.ticket, numbers_announced, ClaimType.MIDDLE_ROW)
        self.assertEqual(result, ClaimStatus.ACCEPTED)

    def test_middle_row_early_claim(self):
        numbers_announced = [7, 23, 38]
        result = ClaimValidator.validate(self.ticket, numbers_announced, ClaimType.MIDDLE_ROW)
        self.assertEqual(result, ClaimStatus.REJECTED)

    def test_middle_row_late_claim(self):
        numbers_announced = [7, 23, 38, 52, 80, 4]
        result = ClaimValidator.validate(self.ticket, numbers_announced, ClaimType.MIDDLE_ROW)
        self.assertEqual(result, ClaimStatus.REJECTED)

    def test_bottom_row_valid_claim(self):
        numbers_announced = [9, 25, 56, 64, 83]
        result = ClaimValidator.validate(self.ticket, numbers_announced, ClaimType.BOTTOM_ROW)
        self.assertEqual(result, ClaimStatus.ACCEPTED)

    def test_bottom_row_early_claim(self):
        numbers_announced = [9, 25, 56]
        result = ClaimValidator.validate(self.ticket, numbers_announced, ClaimType.BOTTOM_ROW)
        self.assertEqual(result, ClaimStatus.REJECTED)

    def test_bottom_row_late_claim(self):
        numbers_announced = [9, 25, 56, 64, 83, 7]
        result = ClaimValidator.validate(self.ticket, numbers_announced, ClaimType.BOTTOM_ROW)
        self.assertEqual(result, ClaimStatus.REJECTED)

    def test_fast_five_valid_claim(self):
        numbers_announced = [4, 16, 48, 63, 76]
        result = ClaimValidator.validate(self.ticket, numbers_announced, ClaimType.FAST_FIVE)
        self.assertEqual(result, ClaimStatus.ACCEPTED)

    def test_fast_five_early_claim(self):
        numbers_announced = [4, 16, 48, 63]
        result = ClaimValidator.validate(self.ticket, numbers_announced, ClaimType.FAST_FIVE)
        self.assertEqual(result, ClaimStatus.REJECTED)

    def test_fast_five_late_claim(self):
        numbers_announced = [4, 16, 48, 63, 76, 7]
        result = ClaimValidator.validate(self.ticket, numbers_announced, ClaimType.FAST_FIVE)
        self.assertEqual(result, ClaimStatus.REJECTED)

    def test_all_numbers_valid_claim(self):
        numbers_announced = [4, 16, 48, 63, 76, 7, 23, 38, 52, 80, 9, 25, 56, 64, 83]
        result = ClaimValidator.validate(self.ticket, numbers_announced, ClaimType.ALL)
        self.assertEqual(result, ClaimStatus.ACCEPTED)

    def test_all_numbers_early_claim(self):
        numbers_announced = [4, 16, 48, 63, 76, 7, 23, 38, 52, 80, 9, 25, 56, 64]
        result = ClaimValidator.validate(self.ticket, numbers_announced, ClaimType.ALL)
        self.assertEqual(result, ClaimStatus.REJECTED)

    def test_all_numbers_late_claim(self):
        numbers_announced = [4, 16, 48, 63, 76, 7, 23, 38, 52, 80, 9, 25, 56, 64, 83, 1]
        result = ClaimValidator.validate(self.ticket, numbers_announced, ClaimType.ALL)
        self.assertEqual(result, ClaimStatus.REJECTED)

    def test_invalid_claim_type(self):
        numbers_announced = [4, 16, 48]
        result = ClaimValidator.validate(self.ticket, numbers_announced, "INVALID_CLAIM")
        self.assertEqual(result, ClaimStatus.REJECTED)

    def test_numbers_in_different_order(self):
        numbers_announced = [48, 4, 16, 63, 76]
        result = ClaimValidator.validate(self.ticket, numbers_announced, ClaimType.TOP_ROW)
        self.assertEqual(result, ClaimStatus.ACCEPTED)

if __name__ == '__main__':
    unittest.main()
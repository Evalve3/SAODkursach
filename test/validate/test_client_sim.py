import unittest

from src.core.dto.sim_return_dto import SimIssueRefund


class TestSimIssueRefund(unittest.TestCase):
    def test_valid_input(self):
        # Valid inputs
        sim_refund = SimIssueRefund(
            passport_number="1234-567890",
            sim_number="123-4567890",
            date_of_issue="2021-01-01",
            date_end="2022-01-01"
        )
        self.assertIsInstance(sim_refund, SimIssueRefund)

    def test_invalid_passport_number(self):
        # Invalid passport number
        with self.assertRaises(ValueError):
            SimIssueRefund(
                passport_number="1234567890",
                sim_number="123-4567890",
                date_of_issue="2021-01-01",
                date_end="2022-01-01"
            )

    def test_invalid_sim_number(self):
        # Invalid sim number
        with self.assertRaises(ValueError):
            SimIssueRefund(
                passport_number="1234-567890",
                sim_number="1234567890",
                date_of_issue="2021-01-01",
                date_end="2022-01-01"
            )

    def test_invalid_date_of_issue(self):
        # Invalid date of issue
        with self.assertRaises(ValueError):
            SimIssueRefund(
                passport_number="1234-567890",
                sim_number="123-4567890",
                date_of_issue="2021-01-01" * 50,  # too long
                date_end="2022-01-01"
            )

    def test_invalid_date_end(self):
        # Invalid date end
        with self.assertRaises(ValueError):
            SimIssueRefund(
                passport_number="1234-567890",
                sim_number="123-4567890",
                date_of_issue="2021-01-01",
                date_end="2022-01-01" * 50  # too long
            )

    def test_invalid_type(self):
        # Invalid type of passport number
        with self.assertRaises(TypeError):
            SimIssueRefund(
                passport_number=1234567890,  # should be str
                sim_number="123-4567890",
                date_of_issue="2021-01-01",
                date_end="2022-01-01"
            )

    def test_equal(self):
        # Valid inputs
        sim_refund1 = SimIssueRefund(
            passport_number="1234-567890",
            sim_number="123-4567890",
            date_of_issue="2021-01-01",
            date_end="2022-01-01"
        )
        sim_refund2 = SimIssueRefund(
            passport_number="1234-567290",
            sim_number="123-4567890",
            date_of_issue="2001-01-01",
            date_end="2012-01-01"
        )
        self.assertEqual(sim_refund1, sim_refund2)

    def test_not_equal(self):
        # Valid inputs
        sim_refund1 = SimIssueRefund(
            passport_number="1234-567890",
            sim_number="123-4567890",
            date_of_issue="2021-01-01",
            date_end="2022-01-01"
        )
        sim_refund2 = SimIssueRefund(
            passport_number="1234-567290",
            sim_number="123-4567890",
            date_of_issue="2001-01-01",
            date_end="2012-01-01"
        )
        self.assertNotEqual(sim_refund1, sim_refund2)

    
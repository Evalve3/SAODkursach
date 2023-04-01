import unittest
from typing import Type

from src.core.dto.sim_dto import Sim


class TestSim(unittest.TestCase):
    def setUp(self) -> None:
        self.sim_valid = Sim(sim_number='123-4567890', tariff_plan='Test Plan', year_of_issue=2022, active=True)


    def test_valid_sim(self) -> None:
        self.assertIsInstance(self.sim_valid, Sim)

    def test_invalid_sim_number(self) -> None:
        with self.assertRaises(TypeError):
            Sim(sim_number=1234567890, tariff_plan='Test Plan', year_of_issue=2022, active=True)
        with self.assertRaises(ValueError):
            Sim(sim_number='1234', tariff_plan='Test Plan', year_of_issue=2022, active=True)
        with self.assertRaises(ValueError):
            Sim(sim_number='123-456789', tariff_plan='Test Plan', year_of_issue=2022, active=True)

    def test_invalid_tariff_plan(self) -> None:
        with self.assertRaises(TypeError):
            Sim(sim_number='123-4567890', tariff_plan=123, year_of_issue=2022, active=True)
        with self.assertRaises(ValueError):
            Sim(sim_number='123-4567890', tariff_plan='a' * 101, year_of_issue=2022, active=True)

    def test_invalid_year_of_issue(self) -> None:
        with self.assertRaises(TypeError):
            Sim(sim_number='123-4567890', tariff_plan='Test Plan', year_of_issue='2022', active=True)
        with self.assertRaises(ValueError):
            Sim(sim_number='123-4567890', tariff_plan='Test Plan', year_of_issue=1800, active=True)
        with self.assertRaises(ValueError):
            Sim(sim_number='123-4567890', tariff_plan='Test Plan', year_of_issue=3000, active=True)

    def test_invalid_active(self) -> None:
        with self.assertRaises(TypeError):
            Sim(sim_number='123-4567890', tariff_plan='Test Plan', year_of_issue=2022, active='True')
        with self.assertRaises(TypeError):
            Sim(sim_number='123-4567890', tariff_plan='Test Plan', year_of_issue=2022, active=1)
        with self.assertRaises(TypeError):
            Sim(sim_number='123-4567890', tariff_plan='Test Plan', year_of_issue=2022, active=None)

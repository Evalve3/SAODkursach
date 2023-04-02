import unittest

from src.core.dto.sim_dto import Sim
from src.data.data_structures.hash_table.hash_table_line import HashTableLine
from src.data.sim_repo.sim_repo import SimRepo


class TestSimRepo(unittest.TestCase):

    def setUp(self):
        self.sim1 = Sim("111-1111111", "Tariff Plan A", 2020, True)
        self.sim2 = Sim("222-2222222", "Tariff Plan B", 2019, False)
        self.sim3 = Sim("333-3333333", "Tariff Plan C", 2018, True)
        self.sim4 = Sim("444-4444444", "Tariff Plan D", 2021, True)
        self.sim5 = Sim("555-5555555", "Tariff Plan E", 2022, False)
        self.repo = SimRepo(HashTableLine(150))

    def tearDown(self):
        self.repo = None

    def test_add(self):
        self.repo.add(self.sim1)
        self.assertEqual(len(self.repo.get_all()), 1)
        self.assertEqual(self.repo.find_by_number("111-1111111"), self.sim1)

    def test_remove(self):
        self.repo.add(self.sim2)
        self.repo.remove(self.sim2)
        self.assertEqual(len(self.repo.get_all()), 0)

    def test_find_by_number(self):
        self.repo.add(self.sim3)
        self.assertEqual(self.repo.find_by_number("333-3333333"), self.sim3)

    def test_get_all(self):
        self.repo.add(self.sim4)
        self.repo.add(self.sim5)
        self.assertEqual(len(self.repo.get_all()), 2)

    def test_remove_all(self):
        self.repo.add(self.sim1)
        self.repo.add(self.sim2)
        self.repo.add(self.sim3)
        self.repo.add(self.sim4)
        self.repo.add(self.sim5)
        self.repo.remove_all()
        self.assertEqual(len(self.repo.get_all()), 0)

    def test_find_by_tariff(self):
        self.repo.add(self.sim1)
        self.repo.add(self.sim2)
        self.repo.add(self.sim3)
        self.repo.add(self.sim4)
        self.repo.add(self.sim5)
        self.assertEqual(len(self.repo.find_by_tariff("Tariff Plan A")), 1)
        self.assertEqual(len(self.repo.find_by_tariff("Tariff Plan C")), 1)
        self.assertEqual(len(self.repo.find_by_tariff("Tariff Plan E")), 1)
        self.assertEqual(len(self.repo.find_by_tariff("Tariff Plan F")), 0)

    def test_edit_data(self):
        self.repo.add(self.sim1)
        self.repo.edit_sim(self.sim1, {"tariff_plan": "Tariff Plan F"})
        self.assertEqual(self.repo.find_by_number("111-1111111").tariff_plan, "Tariff Plan F")


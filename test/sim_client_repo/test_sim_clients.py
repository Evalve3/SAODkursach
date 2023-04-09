import unittest

from src.core.dto.client_dto import Client
from src.core.dto.sim_dto import Sim
from src.core.dto.sim_return_dto import SimIssueRefund
from src.data.data_structures.my_list.cycled_list import List
from src.data.sim_clients_repo.sim_clients_repo import SimClientIssueRefundRepo


class TestSimClientIssueRefundRepo(unittest.TestCase):

    def setUp(self):
        self.sim_list = List()
        self.repo = SimClientIssueRefundRepo(self.sim_list)
        self.client1 = Client(passport_number="1234-567890", place_date_of_issue="Moscow", full_name="Ivan Ivanov",
                         year_of_birth=1985, address="123 Main St.")
        self.client2 = Client(passport_number="9876-543210", place_date_of_issue="St. Petersburg", full_name="Petr Petrov",
                         year_of_birth=1990, address="456 Park Ave.")
        self.client3 = Client(passport_number="1111-222222", place_date_of_issue="Kazan", full_name="Maria Petrova",
                         year_of_birth=1975, address="789 Elm St.")
        self.issuesim1 = SimIssueRefund(passport_number='1234-567890', sim_number='123-4567890', date_of_issue='2022-01-01',
                       date_end='2023-01-01')
        self.issuesim2 = SimIssueRefund(passport_number='9876-543210', sim_number='456-1234567', date_of_issue='2021-12-31',
                       date_end='2022-12-31')
        self.issuesim3 = SimIssueRefund(passport_number='1111-222222', sim_number='789-9876543', date_of_issue='2023-04-01',
                       date_end='2024-04-01')
        self.sim1 = Sim(sim_number='123-4567890', tariff_plan='Plan A', year_of_issue=2022, has=True)
        self.sim2 = Sim(sim_number='456-1234567', tariff_plan='Plan B', year_of_issue=2021, has=False)
        self.sim3 = Sim(sim_number='789-9876543', tariff_plan='Plan C', year_of_issue=2020, has=True)

    def test_register_client_sim(self):
        client = self.client1
        sim = self.sim1
        date_end = '2023-01-01'
        self.repo.register_sim_number(client, sim, date_end)
        self.assertEqual(self.repo.find_by_sim_number('123-4567890'), self.issuesim1)

    def test_find_client_sims(self):
        self.repo.sim_list.add_tail(self.issuesim1)
        self.repo.sim_list.add_tail(self.issuesim2)
        self.repo.sim_list.add_tail(self.issuesim3)
        self.assertEqual(self.repo.find_client_sims(self.client1), [self.issuesim1])
        self.assertEqual(self.repo.find_client_sims(self.client2), [self.issuesim2])
        self.assertEqual(self.repo.find_client_sims(self.client3), [self.issuesim3])

    def test_find_by_sim_number(self):
        self.repo.sim_list.add_tail(self.issuesim1)
        self.repo.sim_list.add_tail(self.issuesim2)
        self.repo.sim_list.add_tail(self.issuesim3)
        self.assertEqual(self.repo.find_by_sim_number('123-4567890'), self.issuesim1)
        self.assertEqual(self.repo.find_by_sim_number('456-1234567'), self.issuesim2)
        self.assertEqual(self.repo.find_by_sim_number('789-9876543'), self.issuesim3)

    def test_find_by_sim_number_not_found(self):
        self.repo.sim_list.add_tail(self.issuesim1)
        self.repo.sim_list.add_tail(self.issuesim2)
        self.repo.sim_list.add_tail(self.issuesim3)
        with self.assertRaises(ValueError):
            self.repo.find_by_sim_number('111-1111111')





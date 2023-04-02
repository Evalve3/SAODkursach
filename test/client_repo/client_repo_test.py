import unittest

from src.core.dto.client_dto import Client
from src.data.client_repo.client_repo import ClientRepo
from src.data.algorithms.search_in_text.in_search import InSearch
from src.data.data_structures.tree.AVL import AvlTree


class TestClientRepo(unittest.TestCase):

    def setUp(self) -> None:
        self.tree = AvlTree()
        self.search_in_text = InSearch()
        self.client_repo = ClientRepo(self.tree, self.search_in_text)

    def test_add_client(self):
        client = Client('1234-567890', 'Moscow, 01.01.2020', 'John Smith', 1985, 'Address')
        self.client_repo.add(client)
        self.assertIn(client, self.client_repo.get_all())

    def test_remove_client(self):
        client = Client('1234-567890', 'Moscow, 01.01.2020', 'John Smith', 1985, 'Address')
        self.client_repo.add(client)
        self.client_repo.remove(client)
        self.assertNotIn(client, self.client_repo.get_all())

    def test_find_client_by_passport(self):
        client = Client('1234-567890', 'Moscow, 01.01.2020', 'John Smith', 1985, 'Address')
        self.client_repo.add(client)
        found_client = self.client_repo.find_by_passport('1234-567890')
        self.assertEqual(client, found_client)

    def test_find_client_by_text(self):
        client1 = Client('1234-567890', 'Moscow, 01.01.2020', 'John Smith', 1985, 'Moscow, 01.01.2020')
        client2 = Client('9876-543210', 'Saint Petersburg, 01.01.2020', 'Jane Doe', 1990, 'Saint Petersburg, 01.01.2020')
        self.client_repo.add(client1)
        self.client_repo.add(client2)
        found_clients = self.client_repo.find_by_text('Moscow')
        self.assertIn(client1, found_clients)
        self.assertNotIn(client2, found_clients)

    def test_clear_data(self):
        client = Client('1234-567890', 'Moscow, 01.01.2020', 'John Smith', 1985, 'Address')
        self.client_repo.add(client)
        self.client_repo.clear_data(client)
        self.assertNotIn(client, self.client_repo.get_all())

    def test_remove_all(self):
        client1 = Client('1234-567890', 'Moscow, 01.01.2020', 'John Smith', 1985, 'Moscow, 01.01.2020')
        client2 = Client('9876-543210', 'Saint Petersburg, 01.01.2020', 'Jane Doe', 1990, 'Saint Petersburg, 01.01.2020')
        self.client_repo.add(client1)
        self.client_repo.add(client2)
        self.client_repo.remove_all()
        self.assertNotIn(client1, self.client_repo.get_all())
        self.assertNotIn(client2, self.client_repo.get_all())

if __name__ == '__main__':
    unittest.main()

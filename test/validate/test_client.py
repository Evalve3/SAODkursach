import unittest

from src.core.dto.client_dto import Client


class TestClient(unittest.TestCase):
    def test_valid_client(self):
        client = Client('1234-567890', 'New York', 'John Doe', 1980, '123 Main St')
        self.assertIsInstance(client, Client)

    def test_invalid_passport_number(self):
        with self.assertRaises(ValueError):
            client = Client('123-456-789', 'New York', 'John Doe', 1980, '123 Main St')

    def test_invalid_year_of_birth(self):
        with self.assertRaises(ValueError):
            client = Client('1234-567890', 'New York', 'John Doe', 2024, '123 Main St')

    def test_invalid_full_name(self):
        with self.assertRaises(ValueError):
            client = Client('1234-567890', 'New York', 'a'*101, 1980, '123 Main St')

    def test_invalid_place_date_of_issue(self):
        with self.assertRaises(ValueError):
            client = Client('1234-567890', 'a'*101, 'John Doe', 1980, '123 Main St')

    def test_invalid_address(self):
        with self.assertRaises(ValueError):
            client = Client('1234-567890', 'New York', 'John Doe', 1980, 'a'*101)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            client = Client(1234, 'New York', 'John Doe', 1980, '123 Main St')
        with self.assertRaises(TypeError):
            client = Client('1234-567890', 'New York', 1234, 1980, '123 Main St')
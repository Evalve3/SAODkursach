import unittest

from src.data.search_in_text.in_search import InSearch


class TestInSearch(unittest.TestCase):

    def setUp(self):
        self.in_search = InSearch()

    def test_search(self):
        text = "Moscow, 01.01.2020"
        pattern = "Moscow"
        self.assertTrue(self.in_search.search(text, pattern))

    def test_search_false(self):
        text = "This is a test string"
        pattern = "not in text"
        self.assertFalse(self.in_search.search(text, pattern))

    def test_empty_string(self):
        text = ""
        pattern = "test"
        self.assertFalse(self.in_search.search(text, pattern))

    def test_empty_pattern(self):
        text = "This is a test string"
        pattern = ""
        self.assertTrue(self.in_search.search(text, pattern))

    def test_case_sensitive(self):
        text = "This is a test string"
        pattern = "Test"
        self.assertFalse(self.in_search.search(text, pattern))


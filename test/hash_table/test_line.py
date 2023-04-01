import unittest

from src.data.hash_table.hash_table_line import HashTableLine


class TestTable(unittest.TestCase):

    def setUp(self):
        self.table = HashTableLine(100)
        # self.table.fill_table(self.table)
        self.table.print()

    def test_add(self):
        self.table.insert("A911KI", "A911KI")
        self.assertFalse(self.table.find("A911KI") == -1)
        self.table.insert("L241YY", "L241YY")
        self.assertFalse(self.table.find("L241YY") == -1)

    def test_get_all(self):
        self.table.insert("A911KI", "A911KI")
        self.table.insert("L241YY", "L241YY")
        self.table.insert("C789FG", "C789FG")
        res = self.table.get_all()
        self.assertEqual(len(res), 3)
        self.table.print()


    def test_add_duplicate(self):
        self.table.insert("A911KI", "A911KI")
        self.assertFalse(self.table.find("A911KI") == -1)
        self.table.insert("A911KI", "A911KI")
        self.assertFalse(self.table.find("A911KI") == -1)
        self.table.print()

    def test_add_after_delete(self):
        self.table.insert("A911KI", "A911KI")
        self.assertFalse(self.table.find("A911KI") == -1)
        self.table.remove("A911KI")
        self.assertTrue(self.table.find("A911KI") == -1)
        self.table.insert("A911KI", "A911KI")
        self.assertFalse(self.table.find("A911KI") == -1)

    def test_find(self):
        self.table.insert("A911KI", "A911KI")
        self.table.insert("L241YY", "L241YY")
        self.assertFalse(self.table.find("A911KI") == -1)
        self.assertFalse(self.table.find("L241YY") == -1)
        self.assertEqual(self.table.find("C789FG"), -1)

    def test_del(self):
        self.table.insert("A911KI", "A911KI")
        self.table.insert("L241YY", "L241YY")
        self.table.remove("A911KI")
        self.assertEqual(self.table.find("A911KI"), -1)
        self.assertNotEqual(self.table.find("L241YY"), -1)



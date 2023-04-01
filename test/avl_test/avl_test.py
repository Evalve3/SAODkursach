import unittest

from src.data.tree.AVL import AvlTree


class TestAvl(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = AvlTree()

    def test_insert(self):
        self.tree.insert('1234-123456', 'dfgdsfg')
        self.tree.insert('1234-123457', 'dfgdsfg')
        self.tree.insert('1234-123458', 'dfgdsfg')
        self.tree.insert('1234-123459', 'dfgdsfg')
        self.tree.insert('1234-123460', 'dfgdsfg')
        self.tree.insert('1234-123461', 'dfgdsfg')
        self.tree.insert('1234-123462', 'dfgdsfg')
        self.assertTrue(self.tree.find('1234-123456'))
        self.assertTrue(self.tree.find('1234-123457'))
        self.assertTrue(self.tree.find('1234-123458'))
        self.assertTrue(self.tree.find('1234-123459'))
        self.assertTrue(self.tree.find('1234-123460'))
        self.assertTrue(self.tree.find('1234-123461'))
        self.assertTrue(self.tree.find('1234-123462'))
        self.assertFalse(self.tree.find('32'))
        self.tree.print()

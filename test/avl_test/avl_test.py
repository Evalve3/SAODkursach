import unittest

from src.data.data_structures.tree.AVL import AvlTree


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

    def test_remove(self):
        self.tree.insert('1234-123456', 'dfgdsfg')
        self.tree.insert('1234-123457', 'dfgdsfg')
        self.tree.insert('1234-123458', 'dfgdsfg')
        self.tree.insert('1234-123459', 'dfgdsfg')
        self.tree.insert('1234-123460', 'dfgdsfg')
        self.tree.insert('1234-123461', 'dfgdsfg')
        self.tree.insert('1234-123462', 'dfgdsfg')
        self.tree.remove('1234-123456')
        self.tree.remove('1234-123457')
        self.tree.remove('1234-123458')
        self.tree.remove('1234-123459')
        self.tree.remove('1234-123460')
        self.tree.remove('1234-123461')
        self.tree.remove('1234-123462')
        self.assertFalse(self.tree.find('1234-123456'))
        self.assertFalse(self.tree.find('1234-123457'))
        self.assertFalse(self.tree.find('1234-123458'))
        self.assertFalse(self.tree.find('1234-123459'))
        self.assertFalse(self.tree.find('1234-123460'))
        self.assertFalse(self.tree.find('1234-123461'))
        self.assertFalse(self.tree.find('1234-123462'))
        self.assertFalse(self.tree.find('32'))
        self.tree.print()

    def test_get_all(self):
        self.tree.insert('1234-123456', 'dfgdsfg')
        self.tree.insert('1234-123457', 'dfgdsfg')
        self.tree.insert('1234-123458', 'dfgdsfg')
        self.tree.insert('1234-123459', 'dfgdsfg')
        self.tree.insert('1234-123460', 'dfgdsfg')
        self.tree.insert('1234-123461', 'dfgdsfg')
        self.tree.insert('1234-123462', 'dfgdsfg')
        self.assertEqual(len(self.tree.get_all()), 7)
        self.tree.print()


    def test_find(self):
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

    def test_remove_all(self):
        self.tree.insert('1234-123456', 'dfgdsfg')
        self.tree.insert('1234-123457', 'dfgdsfg')
        self.tree.insert('1234-123458', 'dfgdsfg')
        self.tree.insert('1234-123459', 'dfgdsfg')
        self.tree.insert('1234-123460', 'dfgdsfg')
        self.tree.insert('1234-123461', 'dfgdsfg')
        self.tree.insert('1234-123462', 'dfgdsfg')
        self.tree.remove_all()
        self.assertEqual(len(self.tree.get_all()), 0)
        self.tree.print()

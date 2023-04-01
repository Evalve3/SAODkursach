import unittest
import io

from src.data.my_list.cycled_list import List
from unittest.mock import patch


class TestList(unittest.TestCase):
    def setUp(self):
        self.lst = List()

    def test_add_tail(self):
        self.lst.add_tail(1)
        self.lst.add_tail(2)
        self.assertEqual(self.lst.get_len(), 2)
        self.assertEqual(self.lst.get_elem(0).value, 1)
        self.assertEqual(self.lst.get_elem(1).value, 2)

    def test_add_tail_empty_list(self):
        self.lst.add_tail(1)
        self.assertEqual(self.lst.get_len(), 1)
        self.assertEqual(self.lst.get_elem(0).value, 1)

    def test_show_list(self):
        self.lst.add_tail(1)
        self.lst.add_tail(2)
        self.lst.add_tail(3)
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.lst.show_list()
            self.assertEqual(fake_stdout.getvalue(), '1 2 3 ')

    def test_get_elem(self):
        self.lst.add_tail(1)
        self.lst.add_tail(2)
        self.lst.add_tail(3)
        self.assertEqual(self.lst.get_elem(0).value, 1)
        self.assertEqual(self.lst.get_elem(1).value, 2)
        self.assertEqual(self.lst.get_elem(2).value, 3)

    def test_del_elem(self):
        self.lst.add_tail(1)
        self.lst.add_tail(2)
        self.lst.add_tail(3)
        self.lst.del_elem(1)
        self.assertEqual(self.lst.get_len(), 2)
        self.assertEqual(self.lst.get_elem(0).value, 1)
        self.assertEqual(self.lst.get_elem(1).value, 3)

    def test_del_elem_empty_list(self):
        with self.assertRaises(IndexError):
            self.lst.del_elem(0)

    def test_del_elem_out_of_range(self):
        self.lst.add_tail(1)
        with self.assertRaises(IndexError):
            self.lst.del_elem(1)

    def test_del_list(self):
        self.lst.add_tail(1)
        self.lst.add_tail(2)
        self.lst.add_tail(3)
        self.lst.del_list()
        self.assertEqual(self.lst.get_len(), 0)
        self.assertIsNone(self.lst.head)
        self.assertIsNone(self.lst.tail)

import unittest
from utils.make_list import byte_list


class TestMakeListMethods(unittest.TestCase):
    def test_byte_list(self):
        listAscii, listAsciiSize = byte_list()
        expected_size = 256
        self.assertEqual(listAsciiSize,  expected_size)

if __name__ == '__main__':
    unittest.main()

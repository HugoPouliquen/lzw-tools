import unittest
from utils.compression import compress


class TestCompressMethods(unittest.TestCase):
    def test_compress(self):
        text = 'TOBEORNOTTOBEORTOBEORNOT'
        expected = ['T', 'O', 'B', 'E', 'O', 'R', 'N', 'O', 'T', 256, 258, 260, 265, 259, 261]
        self.assertEqual(compress(text),  expected)

if __name__ == '__main__':
    unittest.main()

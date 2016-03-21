import unittest
from utils.pretty import pretty_compression


class TestPrettyMethod(unittest.TestCase):
    def test_pretty_compression(self):
        compressed = ['T', 'O', 'B', 'E', 'O', 'R', 'N', 'O', 'T', 256, 258, 260, 265, 259, 261]
        expected = "T O B E O R N O T 256 258 260 265 259 261 "

        self.assertEqual(pretty_compression(compressed),  expected)

if __name__ == '__main__':
    unittest.main()

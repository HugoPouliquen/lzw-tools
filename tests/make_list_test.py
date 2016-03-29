import unittest
from utils.make_list import byteList


class TestMakeListMethods(unittest.TestCase):
    def test_byteList(self):
        """
        Purpose: Test list size and structure
        Description: It has a no regression tests.
        The first test is for the byte structure of the list. It test
        if the following structure matches the ascii table converted in byte
        The second test check the list size.
        """
        list_ascii, list_ascii_size = byteList()
        expected_size = 256
        self.assertEqual(list_ascii_size,  expected_size)

        expected_list = [
            b'\x00\x00', b'\x00\x01', b'\x00\x02', b'\x00\x03', b'\x00\x04',
            b'\x00\x05', b'\x00\x06', b'\x00\x07', b'\x00\x08', b'\x00\t',
            b'\x00\n', b'\x00\x0b', b'\x00\x0c', b'\x00\r', b'\x00\x0e',
            b'\x00\x0f', b'\x00\x10', b'\x00\x11', b'\x00\x12', b'\x00\x13',
            b'\x00\x14', b'\x00\x15', b'\x00\x16', b'\x00\x17', b'\x00\x18',
            b'\x00\x19', b'\x00\x1a', b'\x00\x1b', b'\x00\x1c', b'\x00\x1d',
            b'\x00\x1e', b'\x00\x1f', b'\x00 ', b'\x00!', b'\x00"', b'\x00#',
            b'\x00$', b'\x00%', b'\x00&', b"\x00'", b'\x00(', b'\x00)', b'\x00*',
            b'\x00+', b'\x00,', b'\x00-', b'\x00.', b'\x00/', b'\x000', b'\x001',
            b'\x002', b'\x003', b'\x004', b'\x005', b'\x006', b'\x007', b'\x008',
            b'\x009', b'\x00:', b'\x00;', b'\x00<', b'\x00=', b'\x00>', b'\x00?',
            b'\x00@', b'\x00A', b'\x00B', b'\x00C', b'\x00D', b'\x00E', b'\x00F',
            b'\x00G', b'\x00H', b'\x00I', b'\x00J', b'\x00K', b'\x00L', b'\x00M',
            b'\x00N', b'\x00O', b'\x00P', b'\x00Q', b'\x00R', b'\x00S', b'\x00T',
            b'\x00U', b'\x00V', b'\x00W', b'\x00X', b'\x00Y', b'\x00Z', b'\x00[',
            b'\x00\\', b'\x00]', b'\x00^', b'\x00_', b'\x00`', b'\x00a', b'\x00b',
            b'\x00c', b'\x00d', b'\x00e', b'\x00f', b'\x00g', b'\x00h', b'\x00i',
            b'\x00j', b'\x00k', b'\x00l', b'\x00m', b'\x00n', b'\x00o', b'\x00p',
            b'\x00q', b'\x00r', b'\x00s', b'\x00t', b'\x00u', b'\x00v', b'\x00w',
            b'\x00x', b'\x00y', b'\x00z', b'\x00{', b'\x00|', b'\x00}', b'\x00~',
            b'\x00\x7f', b'\x00\x80', b'\x00\x81', b'\x00\x82', b'\x00\x83',
            b'\x00\x84', b'\x00\x85', b'\x00\x86', b'\x00\x87', b'\x00\x88',
            b'\x00\x89', b'\x00\x8a', b'\x00\x8b', b'\x00\x8c', b'\x00\x8d',
            b'\x00\x8e', b'\x00\x8f', b'\x00\x90', b'\x00\x91', b'\x00\x92',
            b'\x00\x93', b'\x00\x94', b'\x00\x95', b'\x00\x96', b'\x00\x97',
            b'\x00\x98', b'\x00\x99', b'\x00\x9a', b'\x00\x9b', b'\x00\x9c',
            b'\x00\x9d', b'\x00\x9e', b'\x00\x9f', b'\x00\xa0', b'\x00\xa1',
            b'\x00\xa2', b'\x00\xa3', b'\x00\xa4', b'\x00\xa5', b'\x00\xa6',
            b'\x00\xa7', b'\x00\xa8', b'\x00\xa9', b'\x00\xaa', b'\x00\xab',
            b'\x00\xac', b'\x00\xad', b'\x00\xae', b'\x00\xaf', b'\x00\xb0',
            b'\x00\xb1', b'\x00\xb2', b'\x00\xb3', b'\x00\xb4', b'\x00\xb5',
            b'\x00\xb6', b'\x00\xb7', b'\x00\xb8', b'\x00\xb9', b'\x00\xba',
            b'\x00\xbb', b'\x00\xbc', b'\x00\xbd', b'\x00\xbe', b'\x00\xbf',
            b'\x00\xc0', b'\x00\xc1', b'\x00\xc2', b'\x00\xc3', b'\x00\xc4',
            b'\x00\xc5', b'\x00\xc6', b'\x00\xc7', b'\x00\xc8', b'\x00\xc9',
            b'\x00\xca', b'\x00\xcb', b'\x00\xcc', b'\x00\xcd', b'\x00\xce',
            b'\x00\xcf', b'\x00\xd0', b'\x00\xd1', b'\x00\xd2', b'\x00\xd3',
            b'\x00\xd4', b'\x00\xd5', b'\x00\xd6', b'\x00\xd7', b'\x00\xd8',
            b'\x00\xd9', b'\x00\xda', b'\x00\xdb', b'\x00\xdc', b'\x00\xdd',
            b'\x00\xde', b'\x00\xdf', b'\x00\xe0', b'\x00\xe1', b'\x00\xe2',
            b'\x00\xe3', b'\x00\xe4', b'\x00\xe5', b'\x00\xe6', b'\x00\xe7',
            b'\x00\xe8', b'\x00\xe9', b'\x00\xea', b'\x00\xeb', b'\x00\xec',
            b'\x00\xed', b'\x00\xee', b'\x00\xef', b'\x00\xf0', b'\x00\xf1',
            b'\x00\xf2', b'\x00\xf3', b'\x00\xf4', b'\x00\xf5', b'\x00\xf6',
            b'\x00\xf7', b'\x00\xf8', b'\x00\xf9', b'\x00\xfa', b'\x00\xfb',
            b'\x00\xfc', b'\x00\xfd', b'\x00\xfe', b'\x00\xff'
        ]

        self.assertEqual(list_ascii,  expected_list)

if __name__ == '__main__':
    unittest.main()

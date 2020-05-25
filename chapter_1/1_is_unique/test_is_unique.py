''' Test file for the is_unique functions '''

import unittest
from is_unique import is_unique_1


class TestIsUnique(unittest.TestCase):
    ''' Test class for all is_unique functions '''

    data = [
        ("abcdefghi", True),
        ("abcdefgha", False),
        ("rghilpwma", True),
        ("aaaaaaaaaaaaaaaaaaaaaaaaa", False),
        ("", True),
        ("m", True),
        ("cc", False)
        ]

    def test_is_unique_1(self):
        ''' test method for test_is_unique_1 function '''
        for string, expected in self.data:
            self.assertEqual(is_unique_1(string), expected)



if __name__ == "__main__":
    unittest.main()

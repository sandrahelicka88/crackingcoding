#1.9 String rotation
import unittest
def isSubstring(s1,s2):
    return s1.find(s2) != -1


def stringRoatation(string1, string2):# string 2 is shorter
    if len(string1) == len(string2)!=0:
        return isSubstring(string1+string1, string2)
    return False

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = stringRoatation(s1, s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
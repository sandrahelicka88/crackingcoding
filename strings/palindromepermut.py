import unittest

def check_permutation(string):
    char_set = [0 for _ in range(ord('z') - ord('a')+1)]
    countodd = 0
    for c in string:
        val = char_numb(c)
        if val!=-1:
            char_set[val]+=1
            if char_set[val]%2:
                countodd+=1
            else:
                countodd-=1
    return countodd<=1


def char_numb(ch):  # map character to numeric value
    a = ord('a')
    z = ord('z')
    ch = ord(ch)
    if a<=ch<=z:
        return ch-a
    else:
        return -1

class Test(unittest.TestCase):
    data = [
        ('tact coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('able was i ere i saw elba', True),
        ('so patient a nurse to nurse a patient so', False),
        ('random words', False),
        ('not a palindrome', False),
        ('no x in nixon', True),
        ('azaz', True)]
    
    def test_palindromepermut(self):
        for string, expected in self.data:
            result = check_permutation(string)
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
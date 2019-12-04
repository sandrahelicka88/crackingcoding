import unittest
from collections import Counter
def checkPermutation(string1, string2):
    if len(string1)!= len(string2):
        return False
    lookUp = Counter()
    for ch in string1:
        if ch in lookUp:
            lookUp[ch]+=1
        else:
            lookUp[ch]=1
    for ch in string2:
        lookUp[ch]-=1
        if lookUp[ch]<0:
            return False
    return True


class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )
    def test_pemrmutation(self):
    # true check
        for string in self.dataT:
            result = checkPermutation(*string)
            self.assertTrue(result)
    # false check
        for string in self.dataF:
            result = checkPermutation(*string)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
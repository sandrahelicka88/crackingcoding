import unittest
from collections import Counter
def digitFrequency(digit1, digit2):
    digit1 = str(digit1)
    digit2 = str(digit2)
    if len(digit1) != len(digit2):
        return False
    lookUp = Counter()
    for ch in digit1:
        if ch in lookUp:
            lookUp[ch]+=1
        else:
            lookUp[ch]=1
    for ch in digit2:
        lookUp[ch]-=1
        if lookUp[ch]<0:
            return False
    return True

class Test(unittest.TestCase):
    dataT = [
        (128,281),
        (34,43)
    ]
    dataF = [
        (358957, 58795),
        (34,14)
    ]
    def test_unique(self):
        for num1, num2 in self.dataT:
            result = digitFrequency(num1,num2)
            self.assertTrue(result)
        for num1, num2 in self.dataF:
            result = digitFrequency(num1,num2)
            self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()

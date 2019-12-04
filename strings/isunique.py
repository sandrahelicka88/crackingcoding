import unittest
#ascii string
#time complexity: O(n),where n is the length of the string
#space complexity O(1) or O(c) where c is set size
def isUnique(string):
    if len(string)> 128:
        return False 
    char_set = [ False for _ in range(128)]
    for ch in string:
        val = ord(ch)
        if char_set[val]:
            return False
        char_set[val] = True
    return True

# solution without additional storage
def isunique(string):
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return False
    return True




class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = isUnique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = isUnique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()
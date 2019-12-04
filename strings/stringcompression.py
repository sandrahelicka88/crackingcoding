import unittest
def stringCompressor(string):
    compresor = []
    counter = 0
    for i in range(len(string)):
        if i != 0 and string[i]!= string[i-1]:
            compresor.append(string[i-1]+str(counter))
            counter = 0
        counter+=1
    compresor.append(string[-1]+str(counter))
    return min (string, ''.join(compresor), key=len)
class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = stringCompressor(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
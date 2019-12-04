import unittest
'''Conversion: Write a function to determine the number of bits you would need to flip to convert integer A to integer B'''

def bitsToSwap(a,b):
    c = a^b
    count = 0
    while c>0:
        c = c&(c-1) # we want to clear the rightmost 1s until we get to zero
        count+=1 # and we count how many times we can do this until we get to 0
    return count




class Test(unittest.TestCase):
    def test_swapsrequired(self):
        output = bitsToSwap(29,15)
        self.assertEqual(output,2)
        output2 = bitsToSwap(16,32)
        self.assertEqual(output2,2)



if __name__ == '__main__':
    unittest.main()
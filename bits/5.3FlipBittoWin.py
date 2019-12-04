''' You have an integer and you can flip exactly one bit from 0 to 1. Write a code to find the length of the longest sequence of 1s you could create, Example: Input 1775 (or:11011101111), Output: 8'''
import sys
import unittest

def longSequence(n): 
    if ~n == 0: # 11111111 == 00000000 == 0
        return 8 * sys.getsizeof(n)
    current_length = 0
    previous_lenght = 0
    maxLength = 0 
    while n>0:
        if (n&1) ==1:# we check if current bit is 1
            current_length+=1
        elif (n&1)==0:
            if (n&2)==0:
                previous_lenght = 0 
            else:
                previous_lenght = current_length
                current_length = 0

        maxLength = max(previous_lenght+current_length,maxLength)
        n>>=1
    return maxLength+1
print(longSequence(13))
class Test(unittest.TestCase):
    def test_flipBit(self):
        output = longSequence(13)
        self.assertEqual(output,4)
        output2 = longSequence(40)
        self.assertEqual(output2,3)
        
        

if __name__ == '__main__':
    unittest.main()
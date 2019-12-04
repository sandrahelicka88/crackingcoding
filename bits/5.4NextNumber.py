'''Given a positive integer, print the next smallest and the next largest number that have the same number of 1 bits in their binary representation'''

import unittest

def getNextBigger(x):
    c = x
    c0 = 0
    c1 = 0
    while c>0 and c&1==0:
        c0+=1
        c>>=1
    while c>0 and c&1==1:
        c1+=1
        c>>=1
    if c0+c1 == 31 or c0+c1 ==0:
        return -1
    p = c0+c1
    x |= (1 << p) #flip rightmost non trailing zero
  
    #clear all bits to the right of p 
    x&= ~((1 << p) - 1) 
  
    #insert (c1-1) ones on the right. 
    x |= (1 << (c1 - 1)) - 1
  
    return x 
  
print(getNextBigger(13948)) 

def getNextSmallest(x):
    c = x
    c0 = 0
    c1 = 0
    while (c & 1) == 1:
        c1+=1 
        c>>=1 
    if c == 0: 
        return -1
    while (c & 1) == 0 and c!=0:
        c0+=1
        c>>=1 
    p= c0+c1
    mask = (~0)<<p+1 
    x = x&mask#clear bits from p
    sequenceOfOnes = (1<<(c1+1))-1
    x = x|sequenceOfOnes#adding sequences of 1s
    x<<(c0-1)#adding sequences of 0s
    return x

    
print(getNextSmallest(13948))
class Test(unittest.TestCase):
    def test_bigger(self):
        output = getNextBigger(5)
        self.assertEqual(output,6)
        output = getNextBigger(11)
        self.assertEqual(output,13)
    def test_smaller(self):
        output = getNextSmallest(11)
        self.assertEqual(output,7)
        output2 = getNextSmallest(5)
        self.assertEqual(output2,3)
    

if __name__ == '__main__':
    unittest.main()
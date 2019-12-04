'''You are given 2 32-bit numbers, N and M, and two bit positions i and j.Write a method to insert M into N such that M starts at bit j, and ends at bit i.You can assume that the bits j through i have enough space to fit all of M.'''
import unittest

def updateBits(binary_N, binary_M,i,j):
    n = int(binary_N,2)
    m = int(binary_M,2)
    if i>j or i<0 or j>=32:
        return 0
    allOnes = ~0
    #clear bits from i to j
    leftMask = allOnes<<(j+1)
    rightMask = (1<<i)-1
    mask = leftMask|rightMask
    n_cleared = n&mask
    m_shifted = m<<i
    result = n_cleared|m_shifted
    return bin(result)[2:]

class Test(unittest.TestCase):
    def test_updateBits(self):
        output = updateBits('10000000000','10011',2,6)
        self.assertEqual(output,'10001001100')
        output2 = updateBits('100011','01',2,3)
        self.assertEqual(output2,'100111')

if __name__ == '__main__':
    unittest.main()
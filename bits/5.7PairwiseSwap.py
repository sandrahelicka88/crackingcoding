import unittest
def swapOddEvenBits(x): # solution if the input is storded using 32 bits
    even_bits = x&0xAAAAAAAA # select even_bits(1010)
    print(even_bits)
    odd_bits = x&0x55555555 #select odd_bits (0101)
    print(odd_bits)
    shifted_even = logicalRight(even_bits)#logical right shifting
    shifted_odd = odd_bits<<1
    return(shifted_even | shifted_odd)
def logicalRight(n):#logical right shifting
    if n>=0:
        return n>>1
    else:
        return (n+0x100000000)>>1

class Test(unittest.TestCase):
    def test_swaps(self):
        output = swapOddEvenBits(23)
        self.assertEqual(output,43)
        output = swapOddEvenBits(-23)
        self.assertEqual(output, 4294967254) #tutaj mi wychodzi taki wynik jezeli zrobie logiczny right shift numeru -23 , to tak ma wyjsc?

if __name__ == '__main__':
    unittest.main()



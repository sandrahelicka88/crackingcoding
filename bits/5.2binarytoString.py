import unittest
'''Given a real number between 0 and 1 that is passed as a double, print the binary represantation. If the number cannot be represented accurely in binary with at most 32 characters print ERROR'''

def binaryToStr(n):
    if n>=1 or n<=0:
        return 'ERROR'
    result = '0.'
    while n>0:
        if len(result)>=32:
            return 'ERROR'
        n*=2
        if n>=1:
            result+='1'
            n = n-1
        else:
            result+='0'
    return result
    

class Test(unittest.TestCase):
    def testbinToStr(self):
        output = binaryToStr(1)
        self.assertEqual(output,'ERROR')
        output2 = binaryToStr(0.125)
        self.assertEqual(output2,'0.001')
        output3 = binaryToStr(0.78)
        self.assertEqual(output,'ERROR')
        output4 = binaryToStr(0.0625)
        self.assertEqual(output4,'0.0001')



if __name__ == '__main__':
    unittest.main()

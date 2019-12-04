'''Find Duplicates: You have an array with all the numbers from 1 to N, where N is at most 32000. The array may have duplicate entries and you do not know what N is. With only 4 kilobytes of memory available, how would you print all duplicate elements in the array.'''
import unittest
# space complexity 0(n) , time complexity 0(n) where n its the length of array
def checkDuplicates(array):
    dups = []
    bitArray = BitArray(32000)
    for i in range(len(array)):
        num = array[i]
        print(num,'num')
        if bitArray.get(num):
            dups.append(num)
        else:
            bitArray.set(num)
    return dups

class BitArray:
    def __init__(self,n):
        self.arr = [0]* ((n>>5)+1) # we divide by 32(assuming that integer is stored using 32 bits)
    def get(self, integer):#get value of a bit at given position
        #find position of integer
        index = integer>>5
        #find bit number in array
        bitNumber = integer & 0x1F
        #find value of given bit number in arr[index]
        return (self.arr[index]&(1<<bitNumber))!=0
    def set(self,integer):
        #find position of integer
        index = integer>>5
        #set bit number in arr[index] 
        bitNumber = integer & 0x1F
        self.arr[index] = self.arr[index]|(1 << bitNumber)
        return self.arr[index]

print(checkDuplicates([22,67,89,34,23,67,1,1,0,3]))
class Test(unittest.TestCase):
    def test_duplicates(self):
        output = checkDuplicates([22,67,89,34,23,67,1,1,0,3])
        self.assertEqual(output,[67,1])
        output2 = checkDuplicates([12,45,67,89,100])
        self.assertEqual(output2,[])

if __name__ == '__main__':
    unittest.main()

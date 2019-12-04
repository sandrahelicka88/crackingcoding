'''You are given an array-like data structure Listy which lacks a size method.It does, however, have an elementAt(i) method returns the element at index i in O(1) time.If i is beyond the bounds of the data structure, it returns -1.For this reason, the data structure only support positive integers. Given a Listy which contains sorted, positive integers, find the index at which an element x occurs. If x occurs multiple times, you may return any index.'''

import unittest

# space complexity O(1), time complexity O(log n)
def findPositions(list1,target):
    index = 1
    while list1[index] != -1 and list1[index]<target:
        index*=2
    return binarySearch(list1,index//2,index,target)
def binarySearch(array,l,h,target):
    while l<=h:
        mid = (l+h)//2
        middle = array[mid]
        if middle>target or middle ==-1:
            h = mid-1
        elif middle<target:
            l = mid+1
        else:
            return mid
    return -1


class Test(unittest.TestCase):
    def test_search(self):
        output = findPositions([3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170],16)
        self.assertEqual(output,-1)
        output2 = findPositions([3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170],140)
        self.assertEqual(output2,8)
        output3 = findPositions([3,5,7,9,10,16],3)
        self.assertEqual(output3,0)

if __name__ == '__main__':
    unittest.main()
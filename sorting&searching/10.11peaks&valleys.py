'''Peaks and Valleys: In an array of integers, a 'peak' is an element which is greater than or equal to the adjacent integers and a 'valley' is an element which is less  than or equal to the adjacent integers.For example, in the array [5,8,6,2,3,4,6], [8,6] are peaks and [5,2] are valleys. Given an array of integers, sort the array into an alternating sequence of peaks and valleys.
Input: [5,3,1,2,3] 
Output: [5,1,3,2,3]
'''
#time complexity O(n) where n is length of the list , space complexity is O(1)
import unittest

import sys

def sortValleyPeak(alist):
    for i in range(1,len(alist),2):
        biggestIndex = maxIndex(alist,i-1,i,i+1)
        if i != biggestIndex:
            swap(alist,i,biggestIndex)
    return alist


def maxIndex(alist,a,b,c):
    length = len(alist)
    aValue = alist[a] if a>=0 and a<length else -sys.maxsize-1
    bValue = alist[b] if b>=0 and b<length else -sys.maxsize-1
    cValue = alist[c] if c>=0 and c<length else -sys.maxsize-1
    maxVal = max(aValue,max(bValue,cValue))
    if aValue == maxVal:
        return a
    elif bValue == maxVal:
        return b
    else:
        return c


def swap(alist,a,b):
    temp = alist[a]
    alist[a] = alist[b]
    alist[b] = temp


class Test(unittest.TestCase):
    def test_sortValleys(self):
        output = sortValleyPeak([5,3,1,2,3])
        self.assertEqual(output, [3,5,1,3,2])
        output2 = sortValleyPeak([9,1,0,4,8,7])
        self.assertEqual(output2,[1,9,0,8,4,7])


if __name__ == '__main__':
    unittest.main()
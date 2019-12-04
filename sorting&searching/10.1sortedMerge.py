'''Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B. Write a method to merge B into A in sorted order
INPUT: A = [1,4,6,0,0,0]
       B = [3,5,9]
       i = len(A) without the buffer=3
       j = len(B)=3
'''

import unittest
#space complexity : O(1) , time Complexity 0(a+b) where a is the length of array a and b is the length of array b 
def sortedMerge(listA,listB,i,j): 
    indexA = i-1
    indexB = j-1
    lastIndexA = (i+j)-1
    while indexA>=0 and indexB>=0:
        if listA[indexA]>listB[indexB]:
            listA[lastIndexA] = listA[indexA]
            indexA-=1
        else:
            listA[lastIndexA] = listB[indexB]
            indexB-=1
        lastIndexA-=1
    while indexB>=0:#for second case where length of A and B is different
        listA[lastIndexA] = listB[indexB]
        indexB-=1
        lastIndexA-=1
    return listA
class Test(unittest.TestCase):
    def test_merge(self):
        output = sortedMerge([1,2,3,0,0,0],[2,5,6],3,3)
        self.assertEqual(output,[1,2,2,3,5,6])
        output1 = sortedMerge([4,6,8,9,0,0],[1,5],4,2)
        self.assertEqual(output1,[1,4,5,6,8,9])
        output2 = sortedMerge([4,6,0,0,0,0],[1,5,8,9],2,4)
        self.assertEqual(output2,[1,4,5,6,8,9])



if __name__ == '__main__':
    unittest.main()
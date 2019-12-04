'''Sparse Search: Given a sorted array of strings that is interspersed with empty strings,write a method to find the location of a given string.
INPUT: ball, ['at',' ', ' ', ' ', 'ball', ' ', ' ', 'car', ' ',' ', 'dad',' ',' ']
OUTPUT: 4'''
import unittest
#space complexity O(1), time complexity O(n) where n is the length of the array
def sparseSearch(alist,low, high, elem):
    if high<low:
        return -1
    mid = (low+high)//2
    if alist[mid] == ' ': #if mid is empty , we move mid to the closest non empty string
        left = mid-1
        right = mid+1
        while True:
            if left<low or right>high:
                return -1
            if left>=low and alist[left] != ' ':
                mid = left
                break
            if right<=high and alist[right]!=' ':
                mid = right
                break
            right+=1
            left-=1
    if alist[mid] == elem:
        return mid
    elif alist[mid]>elem:
        return sparseSearch(alist,0,mid-1,elem)
    return sparseSearch(alist,mid+1,high,elem)


class Test(unittest.TestCase):
    def test_sparse(self):
        a = ['at', ' ', ' ', ' ','ball', ' ',' ','car',' ',' ','dad',' ',' ']
        b = [' ', ' ', ' ', ' ', ' ', ' ', 'dad']      
        output = sparseSearch(a,0,len(a)-1,'kot')
        self.assertEqual(output,-1)
        output1 = sparseSearch(a,0,len(a)-1,'car')
        self.assertEqual(output1,7)
        output2 = sparseSearch(a,0,len(a)-1,'at')
        self.assertEqual(output2,0)
        output3 = sparseSearch(b,0,len(b)-1,'dad')
        self.assertEqual(output3,6)


if __name__ == '__main__':
    unittest.main()
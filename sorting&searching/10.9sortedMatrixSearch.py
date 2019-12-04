'''Sorted Matrix Search: Given an MxN matrix in which each row and each column is sorted in ascending order, write a method to find an element.
Input: [
    [15,20,40,85],
    [20,35,80,95],
    [30,55,95,105],
    [40,80,100,120]
    ]

'''
import unittest
#Naive approch Space complexity O(1), time complexity O(M log N) where M is number of rows  and it takes log N time to search each one
def findElement(matrix,elem):
    if len(matrix)==0:
        return False
    row = 0
    col = len(matrix[0])-1
    while row<len(matrix) and col>=0:
        if matrix[row][col] == elem:
            return True
        elif matrix[row][col]>elem:
            col-=1
        else:
            row+=1
    return False

print(findElement([[15,20,40,85], [20,35,80,95],[30,55,95,105],[40,80,100,120]],92))
#binarySearch time complexity (logN), space complexity 0(n)

def searchMatrix(matrix, target, start_row, end_row, start_col, end_col):
    if start_row>end_row or start_col>end_col or matrix[start_row][start_col]>target or matrix[end_row][end_col]<target:
        return False
    mid_row = start_row+(end_row-start_row)//2
    mid_col = start_col+(end_col-start_col)//2
    if matrix[mid_row][mid_col] == target:
        return True
    elif matrix[mid_row][mid_col]>target:
        return searchMatrix(matrix, target, start_row,mid_row-1,start_col,mid_col-1) or searchMatrix(matrix, target, start_row,mid_row,mid_col+1,end_col) or searchMatrix(matrix, target, mid_row+1,end_row,start_col,mid_col)
    else:
        return searchMatrix(matrix,target,mid_row+1,end_row,mid_col+1,end_col) or searchMatrix(matrix, target, start_row,mid_row,mid_col+1,end_col) or searchMatrix(matrix, target, mid_row+1,end_row,start_col,mid_col)


class Test(unittest.TestCase):
    def test_findEl(self):
        output = findElement([[15,20,40,85], [20,35,80,95],[30,55,95,105],[40,80,100,120]],92)
        self.assertFalse(output)
        output2 = findElement([[15,20,40,85], [20,35,80,95],[30,55,95,105],[40,80,100,120]],55)
        self.assertTrue(output2)
        output3 = searchMatrix([[15,20,40,85], [20,35,80,95],[30,55,95,105],[40,80,100,120]],105,0,3,0,3)
        self.assertTrue(output3)



if __name__ == '__main__':
    unittest.main()


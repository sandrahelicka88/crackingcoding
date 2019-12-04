import unittest
def zeroMatrix(matrix):   #space O(n)
    rows = []
    columns = []
    numRows = len(matrix)
    numCol = len(matrix[0])
    for i in range(numRows):
        for j in range(numCol):
            if matrix[i][j]==0:
                rows.append(i)
                columns.append(j)
    for row in rows:
        nullifyRow(matrix, row)
    for col in columns:
        nullifyCol(matrix, col)
    return matrix

def nullifyRow(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0

def nullifyCol(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zeroMatrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
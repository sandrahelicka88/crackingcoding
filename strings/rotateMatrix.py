#1.7 Rotate matrix
import unittest
def rotateMatrix(matrix):
    if len(matrix)==1:
        return  matrix
    size_matrix = len(matrix)
    layer_count = size_matrix/2
    for layer in range(layer_count):
        first = layer
        last = size_matrix-first-1
        for i in range(first, last):
            #save top
            top = matrix[layer][i]
            #left->top
            matrix[layer][i] = matrix[-i-1][layer]
            #bottom->left
            matrix[-i-1][layer] = matrix[-layer-1][-i-1]
            #right->bottom
            matrix[-layer-1][-i-1] = matrix[i][-layer-1]
            #top->right
            matrix[i][-layer-1]=top
    return matrix
class Test(unittest.TestCase):
    data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]
    def test_matrix(self):
        for matrixinput, matrixExpected in self.data:
            output = rotateMatrix(matrixinput)
            self.assertEqual(output, matrixExpected)

if __name__ == '__main__':
    unittest.main()
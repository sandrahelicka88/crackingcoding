import unittest
def rotateAntclock90(matrix):
    size = len(matrix)
    layer_count = size/2
    for layer in range(layer_count):
        first = layer
        last = size-first-1
        for i in range(first, last):
            top = matrix[layer][i]
            matrix[layer][i] = matrix[i][-layer-1]
            matrix[i][-layer-1] = matrix[-layer-1][-i-1]
            matrix[-layer-1][-i-1] = matrix[-i-1][layer]
            matrix[-i-1][layer] = top   
    return matrix
class Test(unittest.TestCase):
    data = [
        (
            [
                [1,2,3,4,5],
                [6,7,8,9,10],
                [11,12,13,14,15],
                [16,17,18,19,20],
                [21,22,23,24,25]
            ],[
                [5,10,15 ,20 ,25],
                [4,9,14,19,24],
                [3,8,13,18,23],
                [2,7,12,17,22],
                [1,6,11,16,21]


            ]
        )
    ]
    def testMatrix(self):
        for inputMatrix, outputMatrix in self.data:
            result = rotateAntclock90(inputMatrix)
            self.assertEqual(result, outputMatrix)

if __name__ == '__main__':
    unittest.main()
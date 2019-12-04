import unittest

def maxSubarraySum(array,n):
    maxSum = 0 
    tempSum = 0
    for i in range(n):
        maxSum+=array[i]
    tempSum = maxSum
    for j in range(n,len(array)):
        tempSum = tempSum - [array[i-n]+array[i]
        maxSum = max(maxSum, tempSum)
    return maxSum

class Test(unittest.TestCase):
    data = [
        ([100,200,300,400],2,700),
        ([1,4,2,10,23,3,1,0,20],4,39)
    ]
    def test_sum(self):
        for array, num, expected in self.data:
            result = maxSubarraySum(array,num)
            self.assertEqual(result, expected)
        
if __name__ == '__main__':
    unittest.main()
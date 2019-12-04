def maxSubarraySum(array, n):
    maxSum = 0 
    tempSum = 0
    for i in range(n):
        maxSum+=array[i]
    tempSum = maxSum
    for j in range(n,len(array)):
        tempSum = tempSum - array[i-n] + array[i]
        maxSum = max(tempSum,maxSum)
    return maxSum

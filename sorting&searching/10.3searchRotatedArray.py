def findPivot(arr, low, high):
    if high<low:
        return -1
    if high == low:
        return low
    mid = (low+high)//2
    if mid<high and arr[mid]>arr[mid+1]:
        return mid
    if mid>low and arr[mid]<arr[mid-1]:
        return mid-1
    if arr[low]>=arr[mid]:
        return findPivot(arr,low,mid-1)
    return findPivot(arr, mid+1, high)

def pivotSearch(arr):
    pivot = findPivot(arr,low, hight)
    if pivot == -1:
        return binarySearch(arr, low, high, key)
    if 
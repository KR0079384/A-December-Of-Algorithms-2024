#missing number 
import numpy as np

def findMissingNum1(n,arr1):
    completeList = np.arange(1,n+1)

    for i in completeList:
        a=binarySearch(i,arr1)
        if not a:
            return i
    return "All are present !!"
#binary search to search for the element missing in the main candidate list 
def binarySearch(n,arr1):
    left=0
    right=len(arr1)-1
    while left<=right:
        mid=(left+right)//2
        if arr1[mid]==n:
            return True
        elif arr1[mid] > n:
            right = mid-1
        else:
            left = mid+1
    return False



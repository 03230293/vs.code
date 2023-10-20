def binary_search(array,x):
    left=0
    right=len(arr) -1

    while left <= right:
        mid=(left+right)//2

        if arr[mid]==x:
            return mid

        if arr[mid]<x:
            left=mid+1
        else:
            right=mid-1
    return -1


arr=[1,2,3,4,5,6]
x=3
result=binary_search(arr,x)

if result!=-1:
    print("Element found at index.", result)
else:
    print("Element is not found at index.")

    #Time=O(logn)
    #space=O(1)

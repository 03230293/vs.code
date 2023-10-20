
def linear_search(arr,target):
    for x in range(len(arr)):
        if arr(x) == target:
            return x
    return -1

arr=[2,8,6,4,10]
target=8
r= linear_search(arr,target)
if r != -1:
    print('Element found at index.', result)
else:
    print("Element not found.")
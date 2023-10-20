nums=[1,2,3,1]
output=True
x=set()
# output=True
# print(set(nums)!=nums) 

for num in nums:
    # if num in x:
    #     x.add(num)
    if num in x:
        print("nums!=x")
return(True)
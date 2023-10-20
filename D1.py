nums=[1,2,3,1]
output="True"

s=set(nums)
for n in nums: 
    if n in s:
        return True #There is duplicate
    s.add(n)
return False #No duplicate

#Space=O(n)
#Time=O(n)










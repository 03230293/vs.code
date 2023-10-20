nums= [1,2,3,4,1]
k=0
for x in nums:
	print(x) 
	if x==k:
		set=k
print(set) 

if nums!=set:
	print("True, there is duplicate in the array.")
else:
	print("False,there is no duplicate in the array.")
    

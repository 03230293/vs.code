
def containsDuplicate(nums):
        # 1. Brute Force Method
elements = len(nums)
for i in range(elements):
    for j in range((elements - i - 1)):
        j += i + 1
        print('i:', i, 'j:', j)
    if nums[i] == nums[j]:
                r4eturn True
        return False

        # 2. Sorting Method: ACCEPTED
        # nums = sorted(nums)
        # print(nums)
        # for i in range(len(nums)):
        #         if i+1 == len(nums):
        #         return False
        #         if nums[i] == nums[i+1]:
        #         return True

        # 3. Hash Set: ACCEPTED
        # set_list = set(nums)
        # result = len(nums) != len(set_list)
        # return result

        # 4, Hash Map: ACCEPTED
        # res = {
        #         '1': [],
        #         '2': []
        # }
        # store = {}
        # for i in range(len(nums)):
        #         element = nums[i]
        #         if str(element) in store:
        #         res['2'].append(element)
        #         # return True
        #         else:
        #         store[str(element)] = element
        #         res['1'].append(element)
                # return False
        # print(res)
        # print(store)
        # if len(res['2']) > 0:
        #         # print('Yes')
        #         return True
        # else: 
        #         # print('No')
        #         return False


# input = [1,2,3,1]
# res = containsDuplicate(input)
# print(res)
#1. contain_duplicates_easy.py
#Displaying 1. contain_duplicates_easy.py.
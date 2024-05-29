'''
Given an integer array nums, return true if any value appears more 
than once in the array, otherwise return false.
'''

def containsDuplicateBrute(nums) -> bool:
    # nums is a list of integers

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if(nums[i] == nums[j]): return True
    return False
        


def containsDuplicateOptimal(nums) -> bool:
    # nums is a list of integers

    hashset = set()
    for n in nums:
        if n in hashset: return True
        hashset.add(n)
    return False

#Test cases
test1 = [31, 27, 3, 2, 29, 2]
test2 = [3, 1, 13, 4, 8, 46, 99]

print(containsDuplicateBrute(test1))
print(containsDuplicateBrute(test2))
print(containsDuplicateOptimal(test1))
print(containsDuplicateOptimal(test2))

'''
Given an integer array nums, return true if any value appears more 
than once in the array, otherwise return false.
'''

def containsDuplicateBrute(nums: list[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if(nums[i] == nums[j]): return True
    return False

def containsDuplicateOptimal(nums: list[int]) -> bool:
    hashset = set()
    for n in nums:
        if n in hashset: return True
        hashset.add(n)
    return False

'''
Algorithm analysis:

Brute force approach has a time complexity of O(n^2) due to nested loops. In this problem we iterate
through our array via an inner loop to check if our current element in the outer loop is a duplicate.
If we never find a duplicate after all iterations, it's false by default. Space complexity is O(1)
since throughout the program we are only using constant variables. 

Optimal appraoch has a time complexity of O(n), we use a set to store elements we have iterated through,
on each new iteration we check that set to see if the element is already contained. If so then True,
else False by default. Space complexity is O(n) since our set is growing as the program is running
to a potential size of n.  
'''



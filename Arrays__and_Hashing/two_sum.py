'''
Given an array of integers nums and an integer target, return the indices i and j 
such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.
'''

def twoSumBrute(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target: return [i, j]

    return []

def twoSumOptimal(nums: list[int], target: int) -> list[int]:
    dictionary = {}

    for i, element in enumerate(nums):
        complement = target - element
        if complement in dictionary: 
            return [dictionary[complement], i]
        dictionary[element] = i
    
    return []

'''
Brute force appraoch, we use nested loops, we check the sum of the outer loop element with every inner
loop element. If the sum is equal to our target, take the indices of our current iterations in our outer
and inner loop. Has time complexity of O(n^2) due to nested loops, has space complexity of O(1) as
size of our program doesn't grow as it progresses. 

Optimal approach we use a dictionary that will contain each element in the input list and it's 
corresponding index. By finding the difference between the input target and each element in our
input list, if the difference is contained in the dictionary, it tells us we found both elements
that add up to our target. Element one is the difference number, and element two is the current number
we are currently iterating over. The time complexity is O(n) as we only iterate over input list once,
and the space complexity is O(n) as the size of our dictionary grows as the program progresses. 
'''



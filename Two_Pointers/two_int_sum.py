'''
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], 
such that they add up to a given target number target and index1 < index2. 
Note that index1 and index2 cannot be equal, therefore you may not use the 
same element twice. There will always be exactly one valid solution.

Your solution must use O(1) additional space
'''

def second_two_sum(nums: list[int], target: int) -> list[int]:
    low, high = 0, len(nums) - 1

    while low < high:
        sum = nums[low] + nums[high]
        if sum < target: low += 1
        elif sum > target: high -= 1
        else: return [low + 1, high + 1]
    
    return []

'''
The following has a time complexity of O(N) as we go through the array once, the 
space complexity is O(1) as our input doesn't create extra space as our program
progresses. We use two pointers for this algorithm, if the sum of our values
at the current indices is greater, we decrement the higher pointer, if the sum is
less than target, we increment lower pointer. This only works because we know our 
input array will always be sorted. 
'''
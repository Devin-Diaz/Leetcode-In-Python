'''
Given an array of integers nums, return the length of the longest 
consecutive sequence of elements.

A consecutive sequence is a sequence of elements in which each 
element is exactly 1 greater than the previous element.

You must write an algorithm that runs in O(n) time.
'''

def longest_consecutive(nums: list[int]) -> int:
    hashset = set(nums)
    max_count = 0

    for i in range(len(nums)):
        if nums[i] - 1 not in hashset:
            current_count = 1
            current_element = nums[i] + 1
            while current_element in hashset:
                current_count += 1
                current_element += 1
            
            max_count = max(max_count, current_count)

    return max_count

'''
The TC is O(N) as we only iterate once over the array, the SC is O(1) as we create no extra space
via the input. Here instead of always looking forward, we look backwards instead to get our sequence
started. As soon as we can't find an element in our hashset based off our current element we are iterating
over, it indicates that, it's the start to a potential max sequence. From there since we have all elements
existing in the hashset, we can keep adding 1 to the element where our sequence started and check it with
the hashset, based off that condition we can begin a counter and see how far the sequence goes. 
'''


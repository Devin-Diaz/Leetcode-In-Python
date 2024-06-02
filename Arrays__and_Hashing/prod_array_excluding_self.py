'''
Given an integer array nums, return an array output where output[i] is 
the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O(n) time without using the division operation?
'''

def brute_force(nums: list[int]) -> list[int]:
    output_list = []

    for i in range(len(nums)):
        prod = 1
        for j in range(len(nums)):
            if i == j: continue
            prod *= nums[j]
        output_list = prod
    
    return output_list

def optimal_approach(nums: list[int]) -> list[int]:
    n = len(nums)
    left_prod = [1] * n
    right_prod = [1] * n
    output_list = [1] * n

    # getting left side products
    for i in range(1, n):
        left_prod[i] = left_prod[i - 1] * nums[i - 1]

    # getting right side products
    for i in range(n - 2, -1, -1):
        right_prod[i] = right_prod[i + 1] * nums[i + 1]

    for i in range(n):
        output_list[i] = left_prod[i] * right_prod[i]

    return output_list 

'''
Our brute force appraoch is O(N^2) time complexity and O(N) space complexity since we have an array 
to size n based off our input. In this probelm we sum each element in the array except when the index
of our outer loop and inner loop is the same, we skip over that iteration to ensure we don't add that
element into the product for that index in our output array. 

Our optimal appraoch is O(N) TC with a space complexity of O(N). This appraoch we get the product of each
element and all of it's elements to it's left. Same for the right side. Lastly we multiply these 
elements via same index to get the product except self as by getting products of elements to there left
and right, we will never capture the element itself in the product. 
'''


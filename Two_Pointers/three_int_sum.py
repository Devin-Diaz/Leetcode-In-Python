'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and 
the triplets in any order
'''
def three_sum(nums: list[int]) -> list[list[int]]:
    output_list = []
    nums.sort()

    for i, element in enumerate(nums):
        if i > 0 and element == nums[i - 1]:
            continue
        
        left = i + 1
        right = len(nums) - 1

        while left < right:
            sum = element + nums[left] + nums[right]

            if sum > 0: right -= 1
            elif sum < 0: left += 1
            else: output_list.append([element, nums[left], nums[right]])

            left += 1
            right -= 1

            while nums[left] == nums[left - 1] and left < right:
                left += 1

    return output_list

'''
The tine complexity is O(N^2). We start off with our sorting method. Sorting is O(n log n),
however due to our nested loops with the for and while iterations, our time complexity sums 
to quadratic time. Our space complexity is O(1) exluding our output list. This algorithm
takes inspriation from two sum probelm with a sorted list. We start by iterating thorugh the
input list, we have a base case that ensures we don't use a duplicate element for one of the
three elements. Once we have a unique element, we do 2 pointer technique on the remainder of 
the list until we find a pair that sums up to 0. However we have to make sure that we don't
run into duplicates along with the way when using two pointer technique so after we find a pair 
of unique elements, we shift our left pointer until we have a new unique element for our second
element. You may think we should do this process for our right pointer as well, however, 
that won't really matter as at this point we have 2 unique elements thus we won't run into a 
duplicate set of three elements regardless. 
'''
            



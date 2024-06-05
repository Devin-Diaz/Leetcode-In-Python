'''
You are given an integer array heights where heights[i] represents the height of the ithbar.
You may choose any two bars to form a container. Return the maximum amount of water a container can store.

CASES:
Input: height = [1,7,2,5,4,7,3,6]
Output: 36

Input: height = [2,2,2]
Output: 4
'''

def original_approach(heights: list[int]) -> int:
    left = 0
    right = len(heights) - 1
    max_area = 0

    while left < right:
        if heights[left] < heights[right]:
            current_area = heights[left] * (right - left)
            max_area = max(max_area, current_area)
            left += 1
        else:
            current_area = heights[right] * (right - left)
            max_area = max(max_area, current_area)
            right -= 1
            
    return max_area

def clear_approach(heights: list[int]) -> int:
    left = 0
    right = len(heights)
    max_area = 0

    while left < right:
        current_area = min(heights[left], heights[right]) * (right - left)
        max_area = max(max_area, current_area)

        if heights[left] < heights[right]: left += 1
        else: right -= 1

    return max_area

'''
This problem has TC of O(N) and a SC of O(1). In this problem, we utilize two pointer technique to check which 
side of the container is smaller. We go with the value of that pointer to avoid the container over flowing.
We then calculate the area with the height being that pointer and the width being the difference between the 
pointers. We utilize a max function to keep track of the max area we calculate without overflowing the container.
We then shift the pointer based off whichever had the smallest value originally. We do this for the entire input
array and finally return the max area we calculated throughout the iterations. 
'''
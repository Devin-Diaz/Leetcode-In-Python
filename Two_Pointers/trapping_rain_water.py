'''
You are given an array non-negative integers heights which represent an elevation map. 
Each value heights[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.

TEST CASE:

Input: height = [0,2,0,3,1,0,1,3,2,1]
Output: 9
'''
def trap(height:list[int]) -> int:
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    result = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            result += (left_max - height[left])
        else:
            right -= 1
            right_max = max(right_max, height[right])
            result += (right_max - height[right])
        
        return result

'''
This algorithm is O(N) TC as our iterations are once. The SC is O(1) since all of our usage is constant 
throughout program. For this problem we keep track of a maxiumum height on our left side and right side
of input array. We then utilize two pointers that shift. By finding the difference between the current
max and the value of the pointer of the same side, we will be able to determine how many drops we can trap 
within that range. We don't have to worry about negatives as we are always subtracting from the max value. 
Essentially the pointer is always one ahead of the max and if the shifted pointer is less than the current
max of that same side, it means we can trap water in that position. We do this at both ends of the input arr.
'''


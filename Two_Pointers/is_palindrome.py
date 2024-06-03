'''
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. 
It is also case-insensitive and ignores all non-alphanumeric characters.
'''

import re

def is_palindrome(s: str) -> bool:
    s1 = re.sub("[^A-Za-z]","",s).lower()
    left = 0
    right = len(s1) - 1

    while left <= right:
        if s1[left] != s1[right]: return False
        print(s1[left])
        left += 1
        right -= 1

    return True

'''
Comparing left most and right elements at the same time via two variable pointers.
O(N) TC and O(1) SC. 
'''

'''
Given a string s, find the length of the longest substring without duplicate characters.
A substring is a contiguous sequence of characters within a string.

TEST CASES:

Input: s = "zxyzxyz"
Output: 3

Input: s = "xxxx"
Output: 1
'''

def brute_force(s: str) -> int:
    
    return None


def optimal(s: str) -> int:
    char_set = set()
    max_output = 0
    left = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_output = max(max_output, right - left + 1)
    return max_output
    
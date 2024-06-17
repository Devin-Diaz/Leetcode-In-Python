'''
You are given a string s consisting of only uppercase english characters and an integer k. 
You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

TEST CASES:

Input: s = "XYYX", k = 2
Output: 4

Input: s = "AAABABB", k = 1
Output: 5
'''

'''
    System 1:
        find character with the most occurences
        sliding window problem

        
    System 2:
        A: 4
        B: 2

        A A A B A B B    size window = 6 - 4 = 3  > 2
            L
                    R
'''

def longest_w_replacement(s: str, k: int) -> int:
    count = {}
    char_max = 0
    l = 0

    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1
        char_max = max(char_max, count[s[r]])

        if (r - l) - char_max + 1 > k:
            count[s[l]] -= 1
            l += 1
    
    return (r - l) + 1



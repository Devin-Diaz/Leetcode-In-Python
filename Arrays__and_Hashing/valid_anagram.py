'''
Given two strings s and t, return true if the two strings are anagrams of each other, 
otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the 
order of the characters can be different.
'''

def asciiValidAnagram(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    arr = [0] * 26

    for i in range(len(s)):
        arr[ord(s[i]) - ord('a')] += 1
        arr[ord(t[i]) - ord('a')] -= 1
    
    for n in arr:
        if n != 0: return False
    
    return True

def dictValidAnagram(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    count_s, count_t = {}, {}

    for i in range(len(s)):
        count_s[s[i]] = count_s.get(s[i], 0) + 1
        count_t[t[i]] = count_t.get(t[i], 0) + 1

    return count_s == count_t

'''
Algorithm Analysis:

The solution involving ascii requires us to keep in account all potential letters in the alphabet
via the indices of an array. Recall this solution is valid assuming all inputs will be in lowercase.
The first letter in lowercase ascii alphabet is of course 'a' with a value of 97. We then iterate
through both input words simultaneously and subtracting each character from input s and t by 97.
The difference of that is the index in which will either increment or decrement. If our inputs
are anagrams, all indices of the array will be 0 since they cancelled out as all letters were the same.
or they won't be 0 indicating it's not an anagram. Time complexity is O(n) due to one iteration, and 
space complexity is O(n) due to the size of our array growing as program progresses.

Other appraoch we use dictionaries to keep count of how many of each character are in each word.
If the dictionaries are the same we have a valid anagram else no. Time complexity is O(n) since
we iterate over an input word once, and space complexity is O(n) due to the size of our dictionaries
growing as the program is running.  
'''


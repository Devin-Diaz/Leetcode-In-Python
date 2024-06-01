'''
Given an array of strings strs, group all anagrams together into sublists. 
You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, 
but the order of the characters can be different.
'''

from collections import defaultdict

def first_approach(strs: list[str]) -> list[list[str]]:
    hashmap = {}

    for original_word in strs:
        sorted_word = ''.join(sorted(original_word))
        if sorted_word not in hashmap:
            hashmap[sorted_word] = []
        
        hashmap[sorted_word].append(original_word)
    
    return list(hashmap.values())

def second_appraoch(strs: list[str]) -> list[list[str]]:
    output = defaultdict(list)

    for original_word in strs:
        count = [0] * 26
        for letter in original_word:
            count[ord(letter) - ord('a')] += 1

        output[tuple(count)].append(original_word)
    
    return output.values()

'''
First appraoch, we iterate through our input list of strings, we sort each word, then that sorted word
becomes a key in our map followed by an empty list. If we find that the sorted word is already 
contained in our map, it means we have another anagram as every word that is an anagram will be sorted
in the same fashion. Lastly we return all lists of anagrams casted into one big list. The TC is O(N)
as we only iterate once through our list, and our SC is O(N) as the space of our dictionary grows as
we iterate. 

Second appraoch, the time and space complexity are both O(N * K) where N is the number of words 
and K is the length of the words. In this program we see use the ASCII combination of words via
a list as a key in our default dictionary, if we find an ASCII match with multiple words, they get
added to a list in the value of that corresponding ASCII pattern. Lastly we return all values.
'''



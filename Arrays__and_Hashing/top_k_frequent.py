'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.
'''

def top_k(nums: list[int], k: int) -> list[int]:
    hashmap = {}
    output = []
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        hashmap[n] = hashmap.get(n, 0) + 1

    for key, val in hashmap.items():
        freq[val].append(key)

    for i in range(len(freq) - 1, 0, -1):
        for element in freq[i]:
            output.append(element)
            if len(output) == k: return output
    
    return []

'''
In this program we start by finding the input vals with the highest occurences. We do this via hashmap
and adding 1 to each encounter we have with an existing key. Then we to a list that will contain lists, 
we add the values of the map to indices in this list and in that indice we store the key that being the 
element. By doing this, the latter half of the list will contain the most frequent elements since it's
the greatest index. From here we keep doing this process until we reach k times. The TC and SC of
this program is O(N). 
'''

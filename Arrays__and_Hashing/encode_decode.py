'''
Design an algorithm to encode a list of strings to a single string. 
The encoded string is then decoded back to the original list of strings.

Please implement encode and decode
'''

def encode(strs: list[str]) -> str:
    encoded_string = ""
    for s in strs:
        encoded_string += str(len(s)) + "#" + s

    return encoded_string

def decode(s: str) -> list[str]:
    decoded_list = []
    i = 0

    while i < len(s):
        j = i

        while s[j] != '#':
            j += 1
            
        word_len = int(s[i:j])

        #first letter of word index
        i = j + 1

        # character after last letter since substring is exlusive
        j = i + word_len

        # word appended
        decoded_list.append(s[i:j])

        # i will be starting on the length of the new word on next iteration
        i = j
        
    return decoded_list

'''
For encoding, we use the length of the string, followed by a pound sign then the word itself. For example"
[Devin, Diaz] --> 5#Devin4#Diaz. The # sign is our delimeter and is key when it comes to decoding

For decoding, we essentially use two pointers, j iterates over our encoded string until we hit the delimeter. 
With the delimeter hit with j and our i pointer being at the beginning, we can narrow down the length of the word
via substring and cast it to an integer for use. We then adjust our i and j pointers with the known word length so
when we do another substring operation, we fall exactly onto the word with i being an inclusive index and j being 
exclusive. We append the word and then adjust our i pointer for the next iteration by setting it to j which is at
the start of the next encoded word. 

Time complexity is O(N) for both functions since we iterate over the list of words in encode, and we iterate through
the encoded word once in decode. Space complexity in encode and decode is O(L) where L is the length of all the strings in the 
input list of strings.
'''


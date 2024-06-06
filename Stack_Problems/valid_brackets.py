'''
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

TEST CASES:

Input: s = "[]"
Output: true

Input: s = "([{}])"
Output: true

Input: s = "[(])"
Output: false
'''

def is_valid(s:str) -> bool:
    hashmap = {")": "(", "}": "{", "]": "["}
    stack = []

    for c in s:
        if c not in hashmap:
            stack.append(c)
            continue
        if not stack or stack[-1] != hashmap[c]:
            return False
        stack.pop()

    return not stack

'''
TC is O(N) as we only iterate once over the input string. SC is O(N) as worst case our stack would be the length of our 
input. In this algorithm we use a map where the key value is the right bracket and value is the left bracket. As we iterate
through the string, if we get a left bracket we push it into the stack and continue iterating. If we get a right bracket,
if the stack is empty, or the top most element in the stack is not equal to the value of the right bracket, we do not have
valid parentheses. If our condition is satisfied and find the closing bracket, we pop the top most element and begin checking
for the next left bracket within the stack.
'''


'''
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.

TEST CASES:
Input: tokens = ["1","2","+","3","*","4","-"]
Output: 5
Explanation: ((1 + 2) * 3) - 4 = 5
'''

def evalRPN(tokens: list[str]) -> int:
    stack = []

    for c in tokens:
        if c == "+":
            stack.append(stack.pop() + stack.pop())
        elif c == "-":
            e1 = stack.pop()
            e2 = stack.pop()
            stack.append(e2 - e1)
        elif c == "*":
            stack.append(stack.pop() * stack.pop())
        elif c == "/":
            e1 = stack.pop()
            e2 = stack.pop()
            stack.append(int(e2 - e1))
        else:
            cast = int(c)
            stack.append(cast)

    return stack[-1]

'''
TC is O(N) as we will iterate through the entire list of tokens. The SC is O(N) as worst case all the
operators are at the very end, our stack could grow to N elements. In this problem, we append elements
as we are iterating through the tokens until we hit an operator. When that occurs, we pop 2 elements 
and do the operation on them, we then return the calculated value back into the stack, then we continue
the process and adding to the stack. This pattern will calculate the correct RPN bc/ we are doing the
operations on the nearest elements on the latter half, while doing the operations at the end of the tokens
on already calculated values at the beginning of the stack which we get to as we are popping throughout 
the iterations. 
'''
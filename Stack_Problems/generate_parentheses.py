'''
You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

TEST CASES:

Input: n = 1
Output: ["()"]

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
'''

def generateParenthesis(n: int) -> list[str]:
        
    stack = []
    res = []

    def backtrack(openN, closedN):
        if openN == closedN == n:
            res.append("".join(stack))
            return
            
        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closedN)
            stack.pop()

        if closedN < openN:
            stack.append(")")
            backtrack(openN, closedN + 1)
            stack.pop()

    backtrack(0, 0)
    return res

'''
Ngl this problem was crazy, backtracking has my head going crazy has my head going crazy my head going crazy
head going crazy going crazy crazycmd
'''

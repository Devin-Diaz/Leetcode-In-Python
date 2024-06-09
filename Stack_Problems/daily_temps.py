'''
You are given an array of integers temperatures where temperatures[i] represents the 
daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before
a warmer temperature appears on a future day. If there is no day in the future where a 
warmer temperature will appear for the ith day, set result[i] to 0 instead.

TEST CASES:

Input: temperatures = [30,38,30,36,35,40,28]
Output: [1,4,1,2,1,0,0]

Input: temperatures = [22,21,20]
Output: [0,0,0]
'''

def brute_force(temperatures: list[int]) -> list[int]:
    res = [0] * len(temperatures)

    for i in range(len(temperatures)):
        counter = 0
        for j in range(i + 1, len(temperatures)):
            counter += 1
            if temperatures[j] > temperatures[i]:
                break
            
            if j == len(temperatures) - 1: counter = 0
        
        res[i] = counter
    
    return res

'''
Brute force solution has a TC of O(N^2) and a SC of O(1) exluding our output array.
We utilize nested loops where our outer keeps track of our current temp, then our inner
loop checks if there is a greater temp. We have a counter set up that will increment on 
each iteration, if we find a temp greater we break out and set the value of that counter
to the current index of where i is since it correlates with the temp we are on. If we reach
the end of all iterations in our j loop and we never found a greater element, it means for 
that temp there was never a warmer temperature thus our counter is set to 0. 
'''

def optimal_sol(temperatures: list[int]) -> list[int]:
    res = [0] * len(temperatures) 
    stack = []

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            temp_val, temp_index = stack.pop()
            res[temp_index] = i - temp_index
        
        stack.append([t, i])

    return res

'''
The TC is O(N) and our SC is O(N) due to our stack that holds our temperature value and index 
associated with it. We begin by enumerating through our input list of temps. If our stack
is not empty and our current temperature on iteration is greater than the temperature at the top
of the stack, we pop that stacks value and index associated with it, we then cross reference that
stack index with our current enumerating index. By finding the difference, we can see how many
iterations or 'days' it took until we found a warmer temperature. We then append that to our output
list using our stack index. Then we keep the algorithm going by appending the enumerating value and
index to our stack. 
'''

'''
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
'''

def brute_force(prices: list[int]) -> int:
    max_profit = 0
    for i in range(len(prices)):
        for j in range(len(prices)):
            if prices[i] >= prices[j]: break
            else: max_profit = max(max_profit, prices[j] - prices[i])
    return max_profit

def optimal(prices: list[int]) -> int:
    max_profit, start = 0
    for end, coins in enumerate(prices):
        if prices[start] > coins:
            start = end
            continue
        else:
            max_profit = max(max_profit, coins - prices[start])
    return max_profit

'''
My thought process for O(N) solution:
        System 1:
            - Sliding window problem.
            - start window pointer starts at beginning.
            - End window pointer iterates over the list
            - comparing the end window with start window. 
            - If end window is less than starting window, adjust start window pointer.
            - If end window is larger than start window, we fall in calcs
            - utilizing max function to check difference and keep track of
                profit on each iteration of the loop.

        System 2:
            - utilizing a for loop. Our end window is our i for the loop. 
                saying for end in range end being our pointer always moving.
            - create a global variable for our 'start window pointer'.
            - This will always get checked at the start of every new iteration.
            - We do this because we want to check 
            - global variable that will keep track of max profit
'''
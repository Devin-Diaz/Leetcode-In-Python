'''
There are n cars traveling to the same destination on a one-lane highway.

You are given two arrays of integers position and speed, both of length n.

position[i] is the position of the ith car (in miles)
speed[i] is the speed of the ith car (in miles per hour)
The destination is at position target miles.

A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

Return the number of different car fleets that will arrive at the destination.
'''

def vroom_vroom(position: list[int], speed: list[int], target: int) -> int:
    pairs = [(p, s) for p, s in zip(position, speed)]
    pairs.sort(reverse=True)
    stack = []

    for p, s in pairs:
        stack.append((target - p) / s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)

'''
The TC is O(n logn) since we sort our pairs list and then iterate through that list. SC is O(N) since
we utilize a stack data structure and our pairs list of tuple pairs. In this problem, we sort and reverse
the zipped output list so the values at position and speed match each other via there indices. We can 
calculate the destination of a car by subtracting the position from target and dividing by the speed of
that car. We then push to the stack. When we have at least 2 cars in the stack, for the latest car pushed into
the stack, if the calculated destination time of that car is less than or equal to the second to last element in 
the stack, it indicates that we have a fleet since it tells us those cars met at some point and are now at the
same position. 
'''
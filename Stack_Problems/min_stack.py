'''
Design a stack class that supports the push, pop, top, and getMin operations.

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
Each function should run in 

O(1) time.

TEST CASES:
Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

Output: [null,null,null,null,0,null,2,1]

Explanation:
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); // return 0
minStack.pop();
minStack.top();    // return 2
minStack.getMin(); // return 1
'''

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if not self.min_stack or self.min_stack[-1] >= val:
            self.min_stack.append(val)

        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()

        self.stack.pop() 

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

'''
All operations of the min stack object or O(1). The overall space complexity is O(N) where N is the
number of elements pushed to the stack. This accounts for both stack and min stack which worst case
would store N elements. For pushing elements, no matter what we wil push to our regular stack, however
for our min stack we only push if it is empty, or the element prior is greater indicating that the most
recent element is our current minimum. For popping same scenario, we only pop from minimum stack if it is
the same value as the element being popped in the regular stack. The properties for the other are straight
forward as we return the top most element for minimum and for the regular stack. 
'''
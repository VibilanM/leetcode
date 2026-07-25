# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:
#   MinStack() initializes the stack object.
#   void push(int value) pushes the element value onto the stack.
#   void pop() removes the element on the top of the stack.
#   int top() gets the top element of the stack.
#   int getMin() retrieves the minimum element in the stack.

# You must implement a solution with O(1) time complexity for each function.

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minVal = []

    def push(self, value):
        if not self.minVal:
            self.minVal.append(value)
        else:
            if self.minVal[-1] >= value:
                self.minVal.append(value)
        self.stack.append(value)
        

    def pop(self):
        if self.minVal:
            if self.stack[-1] == self.minVal[-1]:
                y = self.minVal.pop()
        if self.stack:
            return self.stack.pop()
        

    def top(self):
        if self.stack:
            return self.stack[-1]
        

    def getMin(self):
        if self.minVal:
            return self.minVal[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
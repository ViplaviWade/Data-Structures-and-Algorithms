# Leetcode 155: Min Stack:  Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        minVal = self.stack[0]
        for i in range(1, len(self.stack)):
            if self.stack[i] < minVal:
                minVal = self.stack[i]
        return minVal
    
obj = MinStack()
obj.push(4)
obj.push(5)
obj.push(3)
obj.push(9)
print("Stack: ",obj.stack)

popped_element = obj.pop()
print("Popped Element: ", popped_element)
print("Stack: ",obj.stack)

top_element = obj.top()
print("Top Element: ", top_element)
print("Stack: ",obj.stack)

min_element = obj.getMin()
print("Minimum Element: ", min_element)
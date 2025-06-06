# Stack implementation using Linkedlist

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value): 
        new_node = Node(value)
        if self.head:
            new_node.next = self.head # Head is the top most element in the stack
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.data
    
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.head.data

    def isEmpty(self):
        return self.size == 0
    
    def stackSize(self):
        return self.size
    
myStack = Stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')
myStack.push('D')

print("Pop: ", myStack.pop())
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Stack Size: ", myStack.stackSize())
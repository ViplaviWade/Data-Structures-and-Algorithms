# Doubly Linked List implementation in Python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

node1 = Node(3)
node2 = Node(5)
node3 = Node(12)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4

node2.prev = node1
node3.prev = node2
node4.prev = node3

currentNode = node1
print("Forward Traversal:")
while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
print("Null")

currentNode = node4
print("Backward Traversal")
while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.prev
print("Null")
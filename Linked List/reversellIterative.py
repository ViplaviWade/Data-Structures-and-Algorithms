# Reversing a Singly Linkedlist using Iterative method
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end="->")
        currentNode = currentNode.next
    print("Null")
        

def reverseLinkedlist(head):
    prev = None
    current = head
    while current:
        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode
    return prev

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4

print("Linkedlist before reversing:")
traverseAndPrint(node1)
node1 = reverseLinkedlist(node1)
print("Linkedlist after reversing:")
traverseAndPrint(node1)

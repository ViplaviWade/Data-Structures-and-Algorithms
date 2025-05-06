# Reverse a linkedlist

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("Null")

def reverseLinkedlist(head):
    currentNode = head
    prev = None
    while currentNode:
        temp = currentNode.next
        currentNode.next = prev
        prev = currentNode
        currentNode = temp
    return prev

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Original Linkedlist:")
traverseAndPrint(node1)

lst = reverseLinkedlist(node1)
print("Linkedlist after reversal:")
traverseAndPrint(lst)
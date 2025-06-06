# Insert Node at a specific node in a Linked list

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

def insertNodeAtPosition(head, newNode, pos):
    if pos == 1:
        newNode.next = head
        return newNode
    currentNode = head
    for i in range(pos-2):
        if currentNode is None:
            break
        currentNode = currentNode.next
    newNode.next = currentNode.next
    currentNode.next = newNode
    return head

node1 = Node(7)
node2 = Node(3)
node3 = Node(2)
node4 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4

print("Original list:")
traverseAndPrint(node1)

newNode = Node(97)
insertNodeAtPosition(node1, newNode, 2)
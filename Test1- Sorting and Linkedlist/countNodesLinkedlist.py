# Count no of nodes in a Linkedlist

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def countNodes(head):
    count = 0
    currentNode = head
    while currentNode:
        count += 1
        currentNode = currentNode.next
    print("Number of nodes in this Singly Linkedlist is: ", count)

node1 = Node(3)
node2 = Node(5)
node3 = Node(9)
node4 = Node(12)
node5 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

countNodes(node1)
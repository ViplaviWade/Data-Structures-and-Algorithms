# Find lowest value in a Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findLowestValue(head):
    minVal = head.data
    currentNode = head.next
    while currentNode:
        if minVal > currentNode.data:
            minVal = currentNode.data
        currentNode = currentNode.next
    return minVal

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Lowest element in the list is: ", findLowestValue(node1))
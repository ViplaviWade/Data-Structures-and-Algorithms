# Find second largest element in a Linkedlist

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findSecondLargestElement(head):
    # Logic for this is sort the elements and then return the second largest
    currentNode = head
    while currentNode:
         
    print("Second largest element in Linked list is: ", )

node1 = Node(1)
node2 = Node(5)
node3 = Node(8)
node4 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4

findSecondLargestElement(node1)

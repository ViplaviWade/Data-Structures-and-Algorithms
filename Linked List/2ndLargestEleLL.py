# Find and print the second largest element in the Linkedlist

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def secondLargestElement(head):
    current = head
    largest = secondlargest = float('-inf')

    while current:
        value = current.data
        if value > largest:
            secondlargest = largest
            largest = value
        elif value != largest and value > secondlargest:
            secondlargest = value
        current = current.next
    
    if secondlargest == float('-inf'):
        return None
    return secondlargest

node1 = Node(3)
node2 = Node(5)
node3 = Node(2)
node4 = Node(10)
node5 = Node(7)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

num = secondLargestElement(node1)
print("Second largest number from the Linkedlist is: ", num)
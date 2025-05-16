# Delete a node having a specific value in a Circular Singly Linkedlist

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
    startNode = head
    current = startNode
    print(current.data, end=" -> ")
    current = startNode.next
    while current!= startNode:
        print(current.data, end=" -> ")
        current = current.next
    print("Null")

def deleteValue(head, val):
    if head == None:
        return None
    current = head
    prev = None
    
    while True:
        if current.data == val:
            if current == current.next: # Circular Singly Linkedlist with single element
                return None
            if current == head:
                prev = head
                while prev.next != head:
                    prev = prev.next
                prev.next = head.next
                return head
            else:
                prev.next = current.next
            return head
        prev = current
        current = current.next
        if current == head:
            break
    return head

node1 = Node(1)
node2 = Node(5)
node3 = Node(7)
node4 = Node(12)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1

print("Circular Singly Linkedlist before deleting the node:")
traverseAndPrint(node1)

node1 = deleteValue(node1, 7)

print("Circular Singly Linkedlist after deleting the node:")
traverseAndPrint(node1)

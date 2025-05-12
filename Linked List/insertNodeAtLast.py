# Insert a node at the end of a Singly Linkedlist

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("Null")

def insertNodeAtEnd(head, newNode):
    current = head
    while current:
        if current.next != None:
            current = current.next
        else:
            current.next = newNode
            return head
    return head

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
newNode = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4

print("Before insertion of new Node: ")
traverseAndPrint(node1)

node1 = insertNodeAtEnd(node1, newNode)

print("After insertion of Node")
traverseAndPrint(node1)
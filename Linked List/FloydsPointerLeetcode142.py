# Detect if a Linkedlist has a cycle, if yes, output the index where the tail connects the node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def detectCycleUsingFloyds(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            ptr1 = head
            ptr2 = slow
            while ptr1 != ptr2:
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            return ptr1
    return None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
# node5.next = node4

node = detectCycleUsingFloyds(node1)
if node == None:
    print("None")
else:
    print(node.data)
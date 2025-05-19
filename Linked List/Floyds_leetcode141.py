# Check if the linkedlist has a cycle using Floyds Cycle Detection

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
            return True
    return False
    

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
# node5.next = node1

res = detectCycleUsingFloyds(node1)
print(res)
if res:
    print("Linkedlist contains a Cycle")
else:
    print("Linkedlist does not contain a Cycle")
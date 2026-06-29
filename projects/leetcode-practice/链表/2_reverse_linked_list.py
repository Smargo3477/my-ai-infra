class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
    
def reverse(head):


    if head is None:
        return head
   
    if head.next is None:
        return head
    
     
    prev = None
    curr = head
    next_temp = None
   

    while curr is not None:
       next_temp = curr.next
       curr.next = prev
       prev = curr
       curr = next_temp 

    return prev
    
node1 = Node(1)
node2 = Node(3)
node3 = Node(7)
node4 = Node(8)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


def display(head):
    curr = head
    while curr is not None:
        print(curr.val,end = "->" )
        curr = curr.next

    print("None")

display(node1)

rev_node = reverse(node1)

display(rev_node)
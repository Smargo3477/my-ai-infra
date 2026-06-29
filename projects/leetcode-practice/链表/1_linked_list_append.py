class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

def append(head,new_val):
    new_node = Node(new_val)

    if head is None:
        return new_node

    curr = head
    while curr.next is not None:
        curr = curr.next

    curr.next = new_node

    return head  

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3

# 现在调用你的 append 函数，把 4 接上
new_head = append(node1, 4)
new_head2 = append(node1,5)
# 打印验证一下结果
curr = new_head
while curr:
    print(curr.value, end=" -> ")
    curr = curr.next
print("None")
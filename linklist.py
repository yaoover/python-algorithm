class ListNode:
    def __init__(self, item):
        self.item = item
        self.next = None

def create_linklist_head(li):
    head = ListNode(li[0])
    for element in li[1:]:
        node = ListNode(element)
        node.next = head
        head = node
    return head

def create_linklist_tail(li):
    head = ListNode(li[0])
    tail = head
    for element in li[1:]:
        node = ListNode(element)
        tail.next = node
        tail = node
    return head

def print_linklist(lk):
    while lk:
        print(lk.item, end=',')
        lk = lk.next

lk = create_linklist_head([1,2,3,4])
lk1 = create_linklist_tail([1,2,3,4,6,7,8,9])
print_linklist(lk1)
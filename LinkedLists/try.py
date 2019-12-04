class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add(self, item):
        newNode = Node(item)
        if self.head == None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
    def printList(self):
        list_foramat = []
        if self.head == None:
            return []
        current = self.head
        while current:
            list_foramat.append(current.value)
            current = current.next
        return list_foramat

def partition(ll, x):
    smaller_head = None
    smaller_tail = None
    greater_equal_head = None
    greater_equal_tail = None
    if ll.head == None:
        return None
    current = ll.head
    while current:
        next = current.next
        current.next = None
        if current.value<x:
            if smaller_head == None:
                smaller_head = smaller_tail = current
            else:
                smaller_tail.next = current
                smaller_tail = current
        else:
            if greater_equal_head == None:
                greater_equal_head = greater_equal_tail = current
            else:
                greater_equal_tail.next = current
                greater_equal_tail = current
        current = next
    if smaller_head == None:
        return greater_equal_head
    else:
        smaller_tail.next = greater_equal_head
        smaller_tail = greater_equal_head
        return smaller_head
list1 = LinkedList()
list1.add(3)
list1.add(5)
list1.add(8)
list1.add(5)
list1.add(10)
list1.add(2)
list1.add(1)
a = partition(list1,5)


def printList1(ll):
        list_foramat = []
        if ll == None:
            return []
        current = ll
        while current:
            list_foramat.append(current.value)
            current = current.next
        return list_foramat
print(printList1(a))
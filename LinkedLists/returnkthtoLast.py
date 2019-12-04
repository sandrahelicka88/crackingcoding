import unittest

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add(self, item):
        temp = Node(item)
        if self.head == None:
            self.head = self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
    def length(self):
        counter = 0
        current = self.head
        while current:
            counter+=1
            current = current.next
        return counter
    

def returnkthTolast(ll,k):
    current = runner = ll.head
    if current == None:
        return None
    size = ll.length
    for i in range(k):
        runner = runner.next
    while runner:
        current = current.next
        runner = runner.next
    return current.value

ll = LinkedList()
ll.add(14)
ll.add(13)
ll.add(5)
ll.add(6)
ll.add(8)
ll.add(13)
ll.add(8)
    
class Test(unittest.TestCase):
    def test_kthtoLast(self):
        output = returnkthTolast(ll,3)
        self.assertEqual(output,8)
        output = returnkthTolast(ll,5)
        self.assertEqual(output,5)
        output = returnkthTolast(ll,2)
    
if __name__ == '__main__':
    unittest.main()
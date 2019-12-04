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
        newNode = Node(item)
        if self.head == None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
    def size(self):
        counter = 0
        current = self.head
        while current:
            counter+=1
            current = current.next
        return counter
    
def kthTolast(ll,k):
    current = ll.head
    length = ll.size()
    if k>length or k<1:
        raise IndexError('Index out of range')
    for _ in range(length-k):
        current = current.next
    return current.value

ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(5)
ll.add(6)


class Test(unittest.TestCase):
    def test_kthTolast(self):
        with self.assertRaises(IndexError):kthTolast(ll,10)
        output = kthTolast(ll,3)
        self.assertEqual(output,4)
        output = kthTolast(ll,6)
        self.assertEqual(output,1)

if __name__ == '__main__':
    unittest.main()
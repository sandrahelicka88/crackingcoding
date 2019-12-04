import unittest
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def addtoBegining(self, item):
        temp = Node(item)
        if self.head == None:
            self.head = self.tail = temp
        else:
            temp.next = self.head
            self.head = temp
    def add(self,item):
        temp = Node(item)
        if self.head == None:
            self.head = self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
    def convertToList(self):
        list_foramt = []
        current = self.head
        if current == None:
            return []
        while current:
            list_foramt.append(current.value)
            current = current.next
        return list_foramt


def removeDups(ll):
    current = ll.head
    if current == None:
        return None
    lookUp = set([current.value])
    while current.next:
        if current.next.value in lookUp:
            current.next = current.next.next
        else:
            lookUp.add(current.next.value)
            current = current.next
    return ll

#remove dups without additional buffer
def removeDupFollowUp(ll):
    current = ll.head
    if current == None:
        return None
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    return ll



ll = LinkedList()
ll.add(5)
ll.add(8)
ll.add(5)
ll.add(7)
ll.add(1)
ll.add(1)
ll.add(8)
l2 = LinkedList()

class Test(unittest.TestCase):
    def test_dups(self):
        removeDups(ll)
        self.assertEqual(ll.convertToList(),[5,8,7,1])
        removeDups(l2)
        self.assertEqual(l2.convertToList(),[])


if __name__ == '__main__':
    unittest.main()
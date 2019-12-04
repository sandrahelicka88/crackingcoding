import unittest

class Node:
    def __init__(self,value):
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
    def __len__(self):
        count = 0
        if self.head == None:
            return 0
        current = self.head
        while current:
            count+=1
            current = current.next
        return count

def intersectionLists(l1,l2):
    if len(l1) == len(l2) == 0:
        return None
    if l1.tail.value != l2.tail.value:
        return False
    if len(l1)!=len(l2):
        shorter = l1 if len(l1)<len(l2) else l2
        longer = l1 if len(l1)>len(l2) else l2
        current = longer.head
        current2 = shorter.head
        difference = len(longer) - len(shorter)
        for i in range(difference):
            current = current.next
        while current.value!= current2.value:
            current = current.next
            current2 = current2.next
        return current.value

# lists for 1st test case when lists have different length
l1 = LinkedList()
l2 = LinkedList()
l1.add(3)
l1.add(1)
l1.add(5)
l1.add(9)
l1.add(7)
l1.add(2)
l1.add(1)
l2.add(4)
l2.add(6)
l2.add(7)
l2.add(2)
l2.add(1)

#lists for second test case when tails are different
l3 = LinkedList()
l4 = LinkedList()
l3.add(4)
l3.add(6)
l3.add(8)
l3.add(10)
l4.add(6)
l4.add(6)
l4.add(7)
l4.add(7)
l4.add(5)
l4.add(2)
#3rd test for empty lists
l5 = LinkedList()
l6 = LinkedList()   
#4th test for lists with no intersection
l7 = LinkedList()
l7.add(2)
l7.add(3)
l7.add(4)
l8 = LinkedList()
l8.add(2)
l8.add(6)
l8.add(1) 
class Test(unittest.TestCase):
    def test_intersection(self):
        output = intersectionLists(l1,l2)
        self.assertEqual(output, 7)
        output2 = intersectionLists(l3,l4)
        self.assertFalse(output2)
        output3 = intersectionLists(l5,l6)
        self.assertEqual(output3,None)
        output4 = intersectionLists(l7,l8)
        self.assertEqual(output4,False)




if __name__ == '__main__':
    unittest.main()
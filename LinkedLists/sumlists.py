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
    def addToBeginning(self, item):
        newNode = Node(item)
        if self.head == None:
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    def __len__(self):
        count = 0
        if self.head == None:
            return 0
        current = self.head
        while current:
            count+=1
            current = current.next
        return count
    def list_format(self):
        listF = []
        if self.head == None:
            return []
        current = self.head 
        while current:
            listF.append(current.value)
            current = current.next
        return listF

def sumLists(l1,l2):  
    if l1.head == None or l2.head ==None:
        return None
    if len(l1) != len(l2):
        paddingList(l1,l2)
    node1 = l1.head
    node2 = l2.head
    node3 = LinkedList()
    carry = 0
    while node1 and node2:
        result = carry
        if node1:
            result+=node1.value
            node1 = node1.next
        if node2:
            result+=node2.value
            node2 = node2.next
        node3.add(result%10)
        carry = result//10
    if carry:
        node3.add(carry)
    return node3

def paddingList(l1,l2):
    if len(l1)>len(l2):
        for i in range(len(l1)-len(l2)):
            l2.addToBeginning(0)
    else:
        for i in range(len(l2)-len(l1)):
            l1.addToBeginning(0)
    lists = l1,l2
    for lis in lists:
        return lis
#1 data for 1st test case when len(l1) == len(l2)
l1 = LinkedList()
l1.add(7)
l1.add(1)
l1.add(6)
l2 = LinkedList()
l2.add(5)
l2.add(9)
l2.add(2)
paddingList(l1,l2)
print(l1.list_format())
print(l2.list_format())
# data for 2nd test case (both lists are empty)
l3 = LinkedList()
l4 = LinkedList()
#data for case when len(l1)!=len(l2)
l5 = LinkedList()
l5.add(3)
l5.add(2)
l6 = LinkedList()
l6.add(5)
l6.add(9)
l6.add(3)



class Test(unittest.TestCase):
    def test_sumLists(self):
        output = sumLists(l1,l2)
        self.assertEqual(output.list_format(),[2,1,9])
        output2 = sumLists(l3,l4)
        self.assertEqual(output2,None)
        output3 = sumLists(l5,l6)
        self.assertEqual(output3.list_format(),[5,2,6])



if __name__ == '__main__':
    unittest.main()
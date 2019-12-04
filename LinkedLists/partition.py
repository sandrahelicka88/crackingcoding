import unittest
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


def partition(node, x):
    less_than_x_head = None
    less_than_x_tail = None
    greater_equal_x_head = None
    greater_equal_x_tail = None
    
    while node:
        #keep track of node.next
        next = node.next
        #set current node to point to None
        node.next = None
        if node.value<x:
            if less_than_x_head == None:
                less_than_x_head = node
                less_than_x_tail = node
            else:
                less_than_x_tail.next = node
                less_than_x_tail = node
        else:
            if greater_equal_x_head == None:
                greater_equal_x_head = node
                greater_equal_x_tail = node
            else:
                greater_equal_x_tail.next = node
                greater_equal_x_tail = node
        node = next
        #check if less_than_h == None
    if less_than_x_head == None:
        return greater_equal_x_head
    else:
        less_than_x_tail.next = greater_equal_x_head
        less_than_x_tail = greater_equal_x_head
        return less_than_x_head
n1 = Node(3)
n2 = Node(5)
n3 = Node(8)
n4 = Node(5)
n5 = Node(10)
n6 = Node(2)
n7 = Node(1)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7

class Test(unittest.TestCase):
    def test_partition(self):
        result = partition(n1,5)#to jak polaczylam te nody razem to znaczy ze do funkcji jak podam n1 to jest lista nodow? jakos mi to wyglada ze n1 w funkcji partition jest rowny 3, czyli pojedynczemu nodowi? 
        self.assertEqual(self.node_to_list(result),[3,2,1,5,8,5,10])

    def node_to_list(self,node):
        nodelist = []
        current = node
        while current:
            nodelist.append(current.value)
            current = current.next
        return nodelist
        

if __name__ == '__main__':
    unittest.main()
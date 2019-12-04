import unittest

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def deleteMiddle(node):
    if node.next == None:
        return None
    node.value = node.next.value
    node.next = node.next.next


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

#empty node


class Test(unittest.TestCase):
    def test_deletemiddle(self):
        output = deleteMiddle(n5) # deleting last node
        self.assertEqual(self.node_toList(n1),[1,2,3,4,5])
        output = deleteMiddle(n3) #deleting middle node
        self.assertEqual(self.node_toList(n1),[1,2,4,5])

    def node_toList(self, node):
        list_form = []
        if node == None:
            return []
        while node:
            list_form.append(node.value)
            node = node.next
        return list_form


if __name__ == '__main__':
    unittest.main()
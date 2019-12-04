import unittest
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def detectLoop(head):
    slow = fast = head
    while fast and fast.next:#loop exists
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break

    if fast == None or fast.next ==None:# no loop 
        return None
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow



class Test(unittest.TestCase):
    def test_loop(self):
        #node1 for 1 tst case *NO LOOP
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        output = detectLoop(node1)
        self.assertEqual(output, None)
        #2nd case loop exists
        node5.next = node2
        output = detectLoop(node1)
        self.assertEqual(output,node2)
        self.assertEqual(output.value,2)

if __name__ == '__main__':
    unittest.main()
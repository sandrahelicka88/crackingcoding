import sys
import unittest
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validate_bst(root, min = -sys.maxsize, max = sys.maxsize):
    if root == None:
        return True
    if root.value>min and root.value<max and validate_bst(root.left, min ,root.value) and validate_bst(root.right, root.value, max):
        return True
    else:
        return False

class Test(unittest.TestCase):
    def test_bst(self):
        root = None
        self.assertTrue(validate_bst(root))
        root = Node(10)
        self.assertTrue(validate_bst(root))
        left = Node(4)
        right = Node(14)
        root.left = left
        root.right = right
        leftleft = Node(3)
        leftright = Node(6)
        left.left = leftleft
        left.right = leftright
        self.assertTrue(validate_bst(root))
        leftleftleft = Node(20)
        leftleft.right = leftleftleft
        self.assertFalse(validate_bst(root))

if __name__ == '__main__':
    unittest.main()



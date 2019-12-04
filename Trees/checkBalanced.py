import sys
import unittest

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def checkHeight(node):
    if node == None:
        return -1
    left_height = checkHeight(node.left)
    if left_height == -sys.maxsize:
        return -sys.maxsize
    right_height = checkHeight(node.right)
    if right_height == -sys.maxsize:
        return -sys.maxsize
    highDifference = left_height - right_height
    print(abs(highDifference),'abs')
    if abs(highDifference)>1:
        return -sys.maxsize
    else:
        return max(left_height,right_height)+1

def isBalance(node):
    return checkHeight(node)!= -sys.maxsize

root = TreeNode(3)
rl = TreeNode(4)
rr = TreeNode(4)
root.left = rl
root.right = rr
rrr = TreeNode(12)
rr.right = rrr
print(checkHeight(root))

class Test(unittest.TestCase):
    def test_balanced(self):
        root = None
        self.assertTrue(isBalance(root))
        root =TreeNode(3)
        self.assertTrue(isBalance(root))
        rl =TreeNode(4)
        rr = TreeNode(6)
        root.left = rl
        root.right = rr
        self.assertTrue(isBalance(root))
        b=TreeNode(8)
        bb = TreeNode(9)
        rr.left = b
        b.left = bb
        self.assertFalse(isBalance(root))



if __name__ == '__main__':
    unittest.main()
'''4.6 Successor: Write an algorithm to find the next node (i.g inorder successor) of a given node in a binary search tree.You may assume that each node has a link to its parent.'''

import unittest
#time complexity is O(h) where h is height of the tree, space complexity 0(n) n recusive calls  

class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def findSuccesor(node):
    if node == None:
        return None
    if node.right:
        return findMin(node.right)
    else:
        return getNextParent(node)


def getNextParent(node):
    if not node.parent:
        return None
    if node.parent.value> node.value:
        return node.parent
    else:
        return getNextParent(node.parent)

def findMin(node):
    current = node
    while current.left:
        current = current.left
    return current
''
root = TreeNode(20)
node8 = TreeNode(8)
node22 = TreeNode(22)
node4 = TreeNode(4)
node12 = TreeNode(12)
node10 = TreeNode(10)
node14 = TreeNode(14)
root.left = node8
root.right = node22
node8.parent = root
node22.parent = root
node8.left = node4
node8.right = node12
node4.parent = node8
node12.parent = node8
node12.left = node10
node12.right = node14
node10.parent =node12
node14.parent = node12

class Test(unittest.TestCase):
    def findNextSuccesor(self):
        output = findSuccesor(node10)
        self.assertEqual(output,12)

        output2 = findSuccesor(node8)
        self.assertEqual(output2,10)
         
if __name__ == '__main__':
    unittest.main()
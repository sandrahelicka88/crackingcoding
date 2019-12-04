import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def lowestCommonAncestor(root, n1,n2):
    if root == None:
        return None
    if root.data == n1 or root.data== n2:
        return root.data
    left_lca = lowestCommonAncestor(root.left,n1,n2)
    right_lca = lowestCommonAncestor(root.right,n1,n2)
    if left_lca and right_lca:
        return root.data
    if left_lca!=None:
        return left_lca
    else:
        return right_lca

root = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
root.left = node2
root.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

class Test(unittest.TestCase):
    def test_ancestor(self):
        output = lowestCommonAncestor(root,4,5)
        self.assertEqual(output,2)
        output2 = lowestCommonAncestor(root,2,7)
        self.assertEqual(output2,1)
        output3 = lowestCommonAncestor(root,2,8)
        self.assertEqual(output3,2)

if  __name__ == '__main__':
    unittest.main()
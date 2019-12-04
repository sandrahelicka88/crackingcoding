import unittest
'''Check Subtree: T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an algorithm to determine if T2 is a subtree of T1.'''
#space complexity O(n+m) for unbalanced trees , time complexity O(n*m) for unbalance trees
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def areIdentical(root1,root2):
    if root1 == None and root2 == None:
        return True
    if root1 == None or root2 == None:
        return False
    return root1.data == root2.data and areIdentical(root1.left, root2.left) and areIdentical(root1.right, root2.right)

def isSubtree(T, S): # return True if S is subtree of T
    if S == None:
        return True
    if T == None:
        return False
    if areIdentical(T,S):
        return True
    return isSubtree(T.left,S) or isSubtree(T.right,S)

T = Node(26) 
T.right = Node(3) 
T.right.right  = Node(3) 
T.left = Node(10) 
T.left.left = Node(4) 
T.left.left.right = Node(30) 
T.left.right = Node(6) 

S = Node(10) 
S.right = Node(6) 
S.left = Node(4) 
S.left.right = Node(30) 

S2 = Node(10)
S2.right = Node(6)
S2.left = Node(3)
S2.left.right = Node(30)
  

class Test(unittest.TestCase):
    def test_subtree(self):
        output = isSubtree(T,S)
        self.assertTrue(output)
        output2 = isSubtree(T,S2)
        self.assertFalse(output2)


if __name__ == '__main__':
    unittest.main()
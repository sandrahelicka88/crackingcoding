'''Rank from Stream: Imagine you are reading in a stream of integers. Periodically, you wish to be able to look up the rank of a number x(the number of values less than or equal to x). Implement the data structures and algorithms to support these operations. That is, implement the method track(int x)., which is called when each number is genereated, and the method getRankOfNumber(int x), which returns the number of values lest than or equal to x(not including the instance of x itself)'''
 
#time complexity O(log n) on balanced trees or O(n) on unbalanced trees
#space complexity is O(h) where h is height of the tree
import unittest
class Node: 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None
        self.leftSize = 0
 
def insert(root, data): #inserting new node
    if root == None:
        root = Node(data)  
     
    if data <= root.data:
        if root.left != None:
            root.left = insert(root.left,data)
        else:
            root.left = Node(data)
        root.leftSize += 1# updating left subtree
    else: 
        if root.right != None:
            root.right = insert(root.right, data) 
        else:
            root.right = Node(data)
    return root 
def getRank(root, x):
    if root.data == x:
        return root.leftSize
    if x<root.data:
        if root.left == None:
            return -1
        else:
            return getRank(root.left,x)
    else:
        if root.right == None:
            return -1
        else:
            rightsize = getRank(root.right,x)
            if rightsize == -1:
                return -1
            else:
                return root.leftSize + 1 + rightsize

class Test(unittest.TestCase):
    def test_rank(self):
        root= Node(20)
        list1 = [15,25,10,23,5,13,24]
        for elem in list1:
            insert(root,elem)
        output = getRank(root,24)
        self.assertEqual(output,6)
        output2 = getRank(root,3)
        self.assertEqual(output2,-1)
        output3 = getRank(root,30)
        self.assertEqual(output3,-1)
        insert(root,3)
        insert(root,10)
        output4 = getRank(root,24)
        self.assertEqual(output4,8)




if __name__ == '__main__':
    unittest.main()
'''Given a binary tree, design an algorithm which creates a linked list of all the nodes at ech depth(for example if you have a tree with depth D, you will have D linked lists)'''

#time complexity O(n) where n is number of tree nodes and space complexity is O(log n) for balanced binary tree, each call adds a new level to the stack, and for unbalanced binary tree space is O(n)?????????
import unittest
class TreeNode:
    def __init__(self, data):                                                      
        self.data = data
        self.left = None
        self.right = None


class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def list_depths(node, depth , levels = []):
    if not node:
        return
    if depth == 0:
        levels.append(LinkedListNode(node.data))
    else:
        if depth >= len(levels):
            levels.append(LinkedListNode(node.data))
        else:
            level = levels[depth]
            while level:
                previous = level# atu rozumiem ze sie robi te polaczenia miedzy linked listami ktore utworzylismy wczesniej??
                level = level.next
            previous.next = LinkedListNode(node.data)
    list_depths(node.left, depth+1, levels)
    list_depths(node.right, depth+1, levels
    )
    return levels


def create_bst(arr,start,end):
    if start>end:
        return None
    middle = (start+end)//2
    root = TreeNode(arr[middle])
    root.left = create_bst(arr,start,middle-1)
    root.right = create_bst(arr,middle+1,end)
    return root


class Test(unittest.TestCase):
    def test_depths(self):
        a = range(2,10)
        bst = create_bst(a,0,7)
        lists = list_depths(bst,0)
        self.assertEqual(len(lists), 4)
        self.assertEqual(lists[0].data, 5)
        self.assertEqual(lists[1].data, 3)
        self.assertEqual(lists[1].next.data, 7)
        self.assertEqual(lists[2].data, 2)
        self.assertEqual(lists[2].next.data, 4)
        self.assertEqual(lists[2].next.next.data, 6)
        self.assertEqual(lists[2].next.next.next.data,8)
        self.assertEqual(lists[3].data,9)



if __name__ == '__main__':
    unittest.main()
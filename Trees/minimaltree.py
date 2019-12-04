import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def arrayToTree(array, start, end):
    if start>end:
        return None
    middle = int((start+end)/2)
    root = Node(array[middle])
    root.left = arrayToTree(array,start,middle-1)
    root.right = arrayToTree(array, middle+1, end)
    return root

def minimalTree(array):
    return arrayToTree(array, 0, len(array)-1)

def print_Tree(tree):
    if tree == None:
        return
    print(tree.data)
    print('left->')
    print(tree.left)
    print('right->')
    print(tree.right)


class Test(unittest.TestCase):
    def test_minimalTree(self):
        array = [1,2,3,4,5,6,7,8,9,10]
        bst = minimalTree(array)
#tylko wlasnie nie wiem jak mam to zadanie przetestowac ..'''





if __name__ == '__main__':
    unittest.main()
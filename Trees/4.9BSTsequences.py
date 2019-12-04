'''BST SEquences: A binary search tree was created by traversing through an array from left to right and inserting each elem. Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree'''

#space complexity is O(n) where n is length of result list, time complexity is n**2 as we have nested loops
import unittest
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def wave_lists(first,second,results,prefix): #first:list,second:list,results:list,prefix:list
    if not first or not second:
        results.append(prefix+first+second)
        return
    first_item, first_rest = first[0], first[1:]
    wave_lists(first_rest,second,results,prefix+[first_item])
    second_item, second_rest = second[0], second[1:]
    wave_lists(first,second_rest,results,prefix+[second_item])

def all_sequences(root):
    if root == None:
        return None
    answer = []
    prefix = [root.val]
    left = all_sequences(root.left) or [[]]
    print(left, 'left','1 etap')
    right = all_sequences(root.right) or [[]]
    print(right, 'right','1 etap')
    for i in range(len(left)):
        print(i),'i'
        for j in range(len(right)):
            print(j,'j')
            waved = []
            wave_lists(left[i],right[j],waved,prefix)
            print(waved, 'waved')
        answer.extend(waved)
    return answer


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
root2 = TreeNode(10)
node5 = TreeNode(5)
node6 = TreeNode(6)
node14 = TreeNode(14)
root2.left = node5
root2.right = node14
node5.right = node6
root3 = TreeNode(15)
root3.right= TreeNode(22)
print(all_sequences(root2))

class Test(unittest.TestCase):
    def test_bstsequences(self):
        output = all_sequences(root)
        self.assertEqual(output,[[2,1,3],[2,3,1]])
        output2 = all_sequences(root2)
        self.assertEqual(output2,[[10,5,6,14],[10,5,14,6],[10,14,5,6]])
        output3 = all_sequences(root3)
        self.assertEqual(output3,[[15,22]])

if __name__ == '__main__':
    unittest.main()
import unittest
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def count_paths(root, target_sum):
    running_total_tracker = {}
    running_total = 0
    return count_paths_helper(
        root, 
        target_sum, 
        running_total_tracker, 
        running_total
    )
 
def count_paths_helper(node, target_sum, tracker, running_total):
    if not node:
        return 0
 
    matches = 0
    running_total += node.value
 
    if running_total == target_sum:
        matches += 1
     
    diff = running_total - target_sum
    if diff in tracker:
        matches += tracker
 
    if running_total in tracker:
        tracker[running_total] += 1
    else:
        tracker[running_total] = 1
 
    matches += tracker[count_paths_helper(node.left, target_sum, tracker, running_total)]
    matches += tracker[count_paths_helper(node.right, target_sum, tracker, running_total)]
 
    tracker[running_total] -= 1
 
    return matches
root = Node(10)
n5 = Node(5)
nmin3 = Node(-3)
root.left = n5
root.right = nmin3
n3 = Node(3)
n2 = Node(2)
n5.left = n3
n5.right = n2
n33 = Node(3)
nodmin2 = Node(-2)
n3.left = n33
n3.right = nodmin2
n1 = Node(1)
n2.right = n1
n11 = Node(11)
nmin3.right = n11


class Test(unittest.TestCase):
    def test_sumPaths(self):
        output = count_paths(root,8)
        self.assertEqual(output,3)

if __name__ == '__main__':
    unittest.main()
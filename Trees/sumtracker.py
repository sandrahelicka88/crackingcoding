class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_paths(root, target_sum):
    tracker = {}
    running_total = 0
    return count_paths_helper(root, target_sum, tracker, running_total)


def count_paths_helper(node, target_sum, tracker, running_total):
    if node == None:
        return 0
    matches = 0
    running_total+=node.value
    if running_total == target_sum:
        matches+=1
    diff = running_total-target_sum
    if diff in tracker:
        matches+=tracker
        
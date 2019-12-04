import random
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(10)
node5 = Node(5)
node6 = Node(6)
node1 = Node(1)
node15 = Node(15)
node12 = Node(12)
node16 = Node(16)
root.left = node5
root.right = node15
node5.left = node1
node5.right = node6
node15.left = node12
node15.right = node16


def traverse(root, lista = []):
    if root:
        lista = traverse(root.left)
        lista.append(root.data)
        lista = traverse(root.right)
    return lista

array = traverse(root)
print(array)
print(random.choice(array))
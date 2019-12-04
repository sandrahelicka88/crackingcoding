import unittest
class StackOfPlates:
    def __init__(self, capacity):
        self.values = []
        self.capacity = capacity
    def push(self, item):
        if self.values == []:
            self.values.append([item])
        else:
            if len(self.values[-1])>= self.capacity:
                self.values.append([item])
            else:
                self.values[-1].append(item)
    def pop(self):
        if self.values == []:
            return None
        if len(self.values[-1]) == 1:
            poppedItem = self.values[-1].pop()
            del self.values[-1]
            return poppedItem
        else:
            return self.values[-1].pop()

#FollowUp implementing pop at particular index
class StackOfPlatesFollowUp:
    def __init__(self, capacity):
        self.values = []
        self.capacity = capacity
    def push(self, item):
        if self.values == []:
            self.values.append([item])
        else:
            if len(self.values[-1])>= self.capacity:
                self.values.append([item])
            else:
                self.values[-1].append(item)
    def popAt(self, index):
        stack = self.values[index]
        removed_item = stack.pop() 
        if self.values[index] == []:
            del self.values[index]
        return removed_item
    
    
    
class Test(unittest.TestCase):
    def test_stackofplates(self):
        stackPlates = StackOfPlates(3)
        stackPlates.push(1)
        stackPlates.push(2)
        stackPlates.push(3)
        stackPlates.push(4)
        stackPlates.push(5)
        stackPlates.push(6)
        stackPlates.push(7)
        stackPlates.push(8)
        self.assertEqual(stackPlates.pop(),8)
        self.assertEqual(stackPlates.pop(),7)
        self.assertEqual(stackPlates.values, [[1,2,3],[4,5,6]])
        self.assertEqual(stackPlates.pop(),6)
        self.assertEqual(stackPlates.values, [[1,2,3],[4,5]])
        self.assertEqual(stackPlates.pop(),5)
        self.assertEqual(stackPlates.pop(),4)
        self.assertEqual(stackPlates.values, [[1,2,3]])
        self.assertEqual(stackPlates.pop(),3)
        self.assertEqual(stackPlates.pop(),2)
        self.assertEqual(stackPlates.pop(),1)
        self.assertEqual(stackPlates.pop(),None)
        self.assertEqual(stackPlates.values,[])
    def test_stackFollowUp(self):
        stack1 = StackOfPlatesFollowUp(2)
        stack1.push(1)
        stack1.push(2)
        stack1.push(3)
        stack1.push(4)
        self.assertEqual(stack1.popAt(1),4)
        self.assertEqual(stack1.values,[[1,2],[3]])
        self.assertEqual(stack1.popAt(0),2)
        self.assertEqual(stack1.values,[[1],[3]])
        self.assertEqual(stack1.popAt(0),1)
        self.assertEqual(stack1.values, [[3]])


if __name__ == '__main__':
    unittest.main()
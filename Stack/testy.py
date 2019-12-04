import unittest
class ThreeinOne:
    def __init__(self, stacksize):
        self.numstacks = 3 #number of stacks
        self.stacksize = stacksize #size of single stack
        self.sizes = [0]* self.numstacks #array of sizes of each stack 
        self.array = [0]*(self.numstacks*self.stacksize) #array of all stacks
    def isEmpty(self,stacknum):
        return self.sizes[stacknum]==0
    def isFull(self, stacknum):
        return self.sizes[stacknum] == self.stacksize
    def indexOftop(self, stacknum):
        offset = stacknum*self.stacksize
        return offset + self.sizes[stacknum]-1
    def pop(self,stacknum):
        if self.isEmpty(stacknum):
            raise IndexError('Stack is empty')
        value = self.array[self.indexOftop(stacknum)]
        self.array[self.indexOftop(stacknum)] = 0
        self.sizes[stacknum] -= 1
        return value
    def push(self,item,stacknum):
        if self.isFull(stacknum):
            raise IndexError('Stack is full')
        self.sizes[stacknum] += 1
        self.array[self.indexOftop(stacknum)] = item
    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            raise IndexError('Stack is empty')
        return self.array[self.indexOftop(stacknum)]

class Test(unittest.TestCase):
    def test_stack(self):
        threeOne = ThreeinOne(2)# size of each stack is 2
        self.assertEqual(threeOne.isEmpty(1),True) #we check if second stack is empty
        self.assertEqual(threeOne.isEmpty(0),True) #we check if first stack is empty
        self.assertEqual(threeOne.isEmpty(2),True) #we check inf third stack is empty
        threeOne.push(3,1)# push 3 in second stack
        self.assertEqual(threeOne.peek(1),3)
        threeOne.push(2,2)# push 2 in third stack
        threeOne.push(22,2)#push 22 in third stack
        self.assertLessEqual(threeOne.peek(2),22)
        with self.assertRaises(IndexError):threeOne.push(33,2)#push 33 in second stack-> give us Index error as stacksize is 2(line 34)
        threeOne.push(1,0)#push 1 in first stack
        self.assertEqual(threeOne.peek(0),1)



if __name__ == '__main__':
    unittest.main()



    
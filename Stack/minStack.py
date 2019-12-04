import unittest

class MinStack:
    def __init__(self):
        self.values = []
        self.minValues = []
    def push(self, item):
        self.values.append(item)
        if self.minValues == [] or item<self.minValues[-1]:
            self.minValues.append(item)
    def pop(self):
        if self.minValues != [] and self.minValues[-1] == self.values[-1]:
            self.minValues.pop()
        if self.values!= []:
            return self.values.pop()
        else:
            return None
    def minElem(self):
        if self.minValues == []:
            return None
        else:
            return self.minValues[-1]


class Test(unittest.TestCase):
    def test_min(self):
        minstack = MinStack()
        minstack.push(5)
        self.assertEqual(minstack.minElem(),5)
        minstack.push(7)
        self.assertEqual(minstack.minElem(), 5)
        minstack.push(1)
        minstack.push(16)
        minstack.pop()
        self.assertEqual(minstack.minElem(),1)

if __name__ == '__main__':
    unittest.main()

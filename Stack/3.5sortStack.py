import unittest
class Stack:
    def __init__(self):
        self.values = []
    def push(self, item):
        self.values.append(item)
    def pop(self):
        return self.values.pop()
    def isEmpty(self):
        return self.values == []
    def peek(self):
        return self.values[-1]



def sort(st1):
    st2 = Stack()
    while not st1.isEmpty():
        temp = st1.pop()
        while not st2.isEmpty() and st2.peek()>temp:
            st1.push(st2.pop())
        st2.push(temp)
    while not st2.isEmpty():
        st1.push(st2.pop())
    return st1

class Test(unittest.TestCase):
    def test_sort(self):
        st1 = Stack()
        st1.push(16)
        st1.push(10)
        st1.push(4)
        st1.push(6)

        st1.push(9)
        st1.push(17)
        st1.push(3)
        sort(st1)
        self.assertEqual(st1.pop(), 3)
        self.assertEqual(st1.pop(),4)
        self.assertEqual(st1.pop(),6)

if __name__ == '__main__':
    unittest.main()
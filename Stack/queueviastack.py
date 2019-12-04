import unittest
class Queue:
    def __init__(self):
        self.newestOnTop = []
        self.oldestOnTop = []
    def enqueue(self, item):
        self.newestOnTop.append(item) #always add elem to first stack(newestonTop)
    def dequeue(self):
        self.shiftStacks()
        return self.oldestOnTop.pop()

    def peek(self):
        self.shiftStacks()
        return self.oldestOnTop[-1]

    def shiftStacks(self):
        if self.oldestOnTop == []:#perform shifting elem only when oldestOnTop is empty
            while self.newestOnTop !=[]:
                self.oldestOnTop.append(self.newestOnTop.pop())
        

class Test(unittest.TestCase):
    def test_queue(self):
        myQueue = Queue()
        myQueue.enqueue(1)
        myQueue.enqueue(2)
        myQueue.enqueue(3)
        myQueue.enqueue(4)
        myQueue.enqueue(5)
        self.assertEqual(myQueue.dequeue(),1)
        self.assertEqual(myQueue.peek(),2)
        self.assertEqual(myQueue.dequeue(),2)

if __name__ == '__main__':
    unittest.main()[]
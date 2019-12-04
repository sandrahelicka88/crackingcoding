import unittest
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add(self, item):
        newNode = Node(item)
        if self.head == None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
    def __len__(self):
        count = 0
        if self.head == None:
            return 0
        current = self.head
        while current:
            count+=1
            current = current.next
        return count
    


def isPalindrome(ll):#using stack time O(n) space O(n)    
    stack = []
    slower = ll.head
    runner = ll.head
    while runner and runner.next:
        stack.append(slower.value)
        slower = slower.next
        runner = runner.next.next
    if runner:
        slower = slower.next
    while len(stack)!= 0:
        poppedItem = stack.pop()
        if poppedItem != slower.value:
            return False
        slower = slower.next
    return len(stack)==0

def copyList(ll):
    newList = LinkedList()
    current = ll.head
    while current:
        newList.add(current.value)
        current = current.next
    return newList
def reverseList(ll):
    prev = None
    current = ll.head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    ll.head = prev
    return ll


def isPalindrome2(ll):# Time O(n), Space O(1)
    copy = copyList(ll)
    reveresedcopy = reverseList(copy)
    current1 = ll.head
    current2 = reveresedcopy.head
    for i in range(len(ll)/2+1):
        if current1.value!=current2.value:
            return False
        current1 = current1.next
        current2 = current2.next
    return True
        
l1 = LinkedList()#1st test case
l1.add(0)
l1.add(1)
l1.add(2)
l1.add(1)
l1.add(0)
l2 = LinkedList()#2nd test case
l2.add(1)
l2.add(2)
l2.add(2)
l2.add(1)
l3 = LinkedList() #3rd test case
l3.add(1)
l3.add(2)
l3.add(3)   

class Test(unittest.TestCase):
    def test_palindrome(self):
        output = isPalindrome(l1)# func using stack
        output2 = isPalindrome2(l1) #funct using revered list
        self.assertTrue(output)
        self.assertTrue(output2)
        output = isPalindrome(l2) #func using stack
        output2 = isPalindrome2(l2) #func using reversed list
        self.assertTrue(output)
        output = isPalindrome(l3) #func using stack
        output2 = isPalindrome2(l3) #func using revered list
        self.assertFalse(output)
        self.assertFalse(output2)

if __name__ == '__main__':
    unittest.main()

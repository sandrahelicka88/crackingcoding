'''Group Anagrams: Write a method to sort an array of strings so that all the anagrams are next to each other
EXAMPLE: ['eat','tea','tan','ate','nat','bat']
OUTPUT: [
          ['ate','eat','tea'],
          ['nat','tan'],
          ['bat']
]
'''
import unittest
def groupAnag(list1):# space complexity 0(n) , time complexity 0( a  s log s) where a is length of list1 and each string need to be sort (sorting requiring s log s) 
    result = []
    lookUp = {} # dictionary for mapping sorted version of word to actual word
    for word in list1:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in lookUp:
            lookUp[sorted_word] = [word]
        else:
            lookUp[sorted_word].append(word)
    print(lookUp)
    for value in lookUp.values():
        result.append(value)
    return result

print(groupAnag(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))

class Test(unittest.TestCase):
    def test_groupAnagram(self):
        output = groupAnag(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
        self.assertEqual(output,[['tan', 'nat'], ['bat'], ['eat', 'tea', 'ate']])


if __name__ == '__main__':
    unittest.main()
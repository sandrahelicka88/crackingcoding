import unittest
def isAnagram(string1, string2):
    if len(string1)!=len(string2):
        return False
    char_set = [0 for _ in range(ord('z')-ord('a')+1)]
    for ch in string1:
        val = valChar(ch)
        if val !=-1:
            char_set[val]+=1
    for ch in string2:
        val = valChar(ch)
        char_set[val]-=1
        if char_set[val]==-1:
            return False
    return True

def valChar(c):
    a = ord('a')
    z = ord('z')
    c = ord(c)
    if a<=c<=z:
        return c-a
    else:
        return -1

class Test(unittest.TestCase):
    data = [
        ('aaz', 'zza', False),
        ('anagram', 'nagaram', True),
        ('rat', 'car', False),
        ('qwerty', 'qeywrt', True)
    ]
    def test_anagram(self):
        for string1, string2, expected in self.data:
            result = isAnagram(string1, string2)
            self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

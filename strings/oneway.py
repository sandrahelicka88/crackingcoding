#One away 1.5
import unittest
def oneaway(string1, string2):#check if there is 1 or 0 differences
    if abs(len(string1)-len(string2))>1:
        return False
    m = len(string1)
    n = len(string2)
    i = 0
    j = 0
    count = 0
    while i<m and j<n:
        if string1[i]!=string2[j]:
            if count ==1:
                return False
            if m>n:    #string1 is longer
                i+=1
            elif m<n:  #string2 is longer
                j+=1
            else:      #strings are equal
                i+=1
                j+=1
            count+=1
        else:
            i+=1
            j+=1
    if i<m or j<n: #if last char is extra in any string 
        count+=1
    return count<=1

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = oneaway(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()


from collections import Counter
def areDuplicates(array):
    duplicates = False
    lookUp = Counter()
    for item in array:
        if item not in lookUp:
            lookUp[item]=1
        else:
            return True
    return False





print(areDuplicates(['a','a','c']))

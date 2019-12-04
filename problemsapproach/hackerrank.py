def findLongestSub(string):
    maxSubstring = 0
    counts = 0
    if len(string)==0:
        return 0
    i =0
    for j in range(1,len(string)):
        if string[i] != string[j]:
            i+=1
            counts+=1
        maxSubstring = max(maxSubstring,counts)
        

        
    
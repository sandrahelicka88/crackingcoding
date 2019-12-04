def nextLarger(num):
    c = num
    c0 = 0
    c1 = 0
    while c>0 and c&1==0:
        c0+=1
        c>>=1
    while c>0 and c&1==1:
        c1+=1
        c>>=1
    
    if c0+c1 == 31 or c0+c1 ==0:
        return -1
    p = c0+c1
    a = 1<<p
    b = a-1
    b = ~b
    num = num&b
    d = 1<<(c1+1


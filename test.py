from collections import defaultdict



def getHitsList(a):
    hits = []
    for i in range(len(a)):
        hits.append(a[i])
    return hits    


def findLCS(s1,s2):
    m = len(s1)
    n = len(s2)
    MAX = n + m
    i = 0
    lists = getHitsList(s1)
    row1 = []
    row1.append(0)
    row1.append(MAX)
    row1_size = 1
    index = 0
    for j in range(0,n):
        if s2[j] == lists[j] and index == 0:
            index = 1
            row2 = []
            row2.append(0)
            row2.append(MAX)
            row2_size = 1
            r1p1=0;
            r1p2=1;
            r2p1=1;
            loop = True;
            while loop:
                matchPos = m
                if matchPos >= n:
                    for i in range(0,m):
                        if s1[i] == s2[i]:
                            r1p1 = r1p1 + 1
                            row1.append(s2[i])
                            row1_size = row1_size + 1
                else:
                    if matchPos >= m:
                        for i in range(0,n):
                            if s1[i] == s2[i]:
                                r2p2 = r2p2 + 1
                                row2.append(s1[i])
                                row2_size = row2_size + 1
                loop = False
                j = n
        if row1_size > 0:
            row1_size = row1_size
        elif row2_size > 0:
            row1_size = row2_size
    return row1_size-1                 
            
                                



strs1 = "kaleem mrld"
strs2 = "hello world"
count = findLCS(strs1,strs2)
print(count)
    
    



def getHitsList(A):
    arr = A.split(" ")
    hit_list = []
    for i in range(len(A)):
        hit_list.append(arr[i])
    return hit_list


def LCS_V2(A,B):
    ROW_2_Size = 0
    ROW_1_Size = 0
    ROW_1 = []
    ROW_2 = []
    m = len(A)
    n = len(B)
    infinity = m + n
    matchPos = 0
    list_of_Hits = getHitsList(A)
    ROW_1.append(0)
    ROW_1.append(infinity)
    ROW_1.append(1)
    for i in range(1,n):
        if B[i] in list_of_Hits:
            k = 0
            ROW_2.append(0)
            ROW_2.append(infinity)
            ROW_2.append(1)
            R1_ptr1 = 0
            R1_ptr2 = 1
            R2_ptr1 = 1
            while k < n:
                if list_of_Hits[k] == B[k]:
                    if k>=len(list_of_Hits) or ROW_1[R1_ptr2] >= infinity:
                        if ROW_1[R1_ptr1] < infinity:
                            while ROW_1[R1_ptr2] < infinity:
                                ROW_2[R2_ptr1] = ROW_1[R1_ptr2]
                                R2_ptr1 = R2_ptr1 + 1
                                ROW_2[R2_ptr1] = infinity
                                ROW_2_Size = ROW_2_Size + 1
                                R1_ptr1 = R1_ptr2
                                R1_ptr2 = R1_ptr2 + 1
                        else:
                            if matchPos <= ROW_1[R1_ptr1] and matchPos <= ROW_1[R1_ptr2]:
                                ROW_2[R2_ptr1] = matchPos
                                R2_ptr1 = R2_ptr1 + 1
                                ROW_2[R2_ptr1] = infinity
                                ROW_2_Size = ROW_2_Size + 1
                                R1_ptr1 = R1_ptr2
                                R1_ptr2 = R1_ptr2 + 1
                                k = k + 1
                                    
                        
    return ROW_2_Size-1 
            
print(LCS_V2("LCS testing","testing of LCS".split(" ")))    
    

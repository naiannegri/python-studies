import numpy as np
def solution(matrix):
    n_rows = len(matrix)
    n_col = len(matrix[0])
    square_row = []
    rp, cp = 0, 0 
    square=[]
    count = 0
    while rp <= n_rows - 2: 
        while cp <= n_col-2:
            for i in range(rp, rp + 2):
                for j in range(cp, cp + 2):
                    square_row.append(matrix[i][j])
            cp+=1
            square.append(square_row)
            square_row = []
        rp+=1
        cp=0
    uniques = np.unique(square,axis=0)
    return len(uniques)


solution([[1,2,1], 
 [2,2,2], 
 [2,2,2], 
 [1,2,3], 
 [2,2,1]])
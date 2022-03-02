def solution(matrix):
    line=0
    column=0
    result=0
    for i in range(len(matrix)):
        line+=1
        for j in range(len(matrix[0])):
            column+=1
            print(len(matrix[0]),i,j)
            #print(matrix[i][j])
            if line == 1:
                result+=matrix[i][j]
            else:
                slice=[matrix[i][j] for i in range(0,i)]
                if 0 in slice:
                    pass
                else:
                    result+=matrix[i][j]
    print(result)


matrix=[[1,1,1], [2,2,2], [3,3,3]]
matrix2=[[0,1,1,2], [0,5,0,0], [2,0,3,3]]
solution(matrix2)


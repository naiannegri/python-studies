import numpy as np
def solution(picture):
    count=0
    ast="*"
    for name in picture:
        first="*" + name + "*"
        picture[count] = first
        count+=1
    #matrix=np.zeros((len(picture)+2,len(picture[0])))
    matrix=[]
    matrix.append(ast*len(picture[0]))
    for name in picture:
        matrix.append(name)
    matrix.append(ast*len(picture[0]))
    return matrix
picture=["abc",
           "ded"]
solution(picture)
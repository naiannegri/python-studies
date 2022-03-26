import numpy as np

def formSpiralMatrix(arr, mat):
    top = 0;
    bottom = row - 1;
    left = 0;
    right = col - 1;
 
    index = 0;
 
    while (True):
         
        if(left > right):
            break;
 
        # print top row
        for i in range(left, right + 1):
            mat[top][i] = arr[index];
            index += 1;
        top += 1;
 
        if (top > bottom):
            break;
 
        # print right column
        for i in range(top, bottom+1):
            mat[i][right] = arr[index];
            index += 1;
        right -= 1;
 
        if (left > right):
            break;
 
        # print bottom row
        for i in range(right, left-1, -1):
            mat[bottom][i] = arr[index];
            index += 1;
        bottom -= 1;
 
        if (top > bottom):
            break;
 
        # print left column
        for i in range(bottom, top-1, -1):
            mat[i][left] = arr[index];
            index += 1;
        left += 1;
# Function to print the spiral matrix
def printSpiralMatrix(mat):
    for i in range(row):
        for j in range(col):
            print(mat[i][j],end= " ");
        print();


def solution(n):

    i = 0
    arrA = list(range(1,row*col))
    print(matrix)
    mat= [[0 for i in range(col)] for j in range(row)]
    formSpiralMatrix(arrA,mat)
    printSpiralMatrix(mat)

n=3
matrix=np.zeros((n,n))
row = len(matrix)
col = len(matrix[0])
solution(3)
def diagonalDifference(arr):
    # Write your code here
    # print(len(arr))
    sumAllRight=0
    sumAllLeft=0
    for i in range (len(arr)):
        sumAllRight+=arr[i][i]
    for i in range(len(arr)):
        sumAllLeft+=arr[len(arr)-1-i][i]
    return abs(sumAllRight - sumAllLeft)
arr = [[1,2,3],[4,5,6],[9,8,9]]
diagonalDifference(arr)
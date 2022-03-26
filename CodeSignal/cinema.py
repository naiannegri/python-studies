def solution(nCols, nRows, col, row):
    result = ((nCols - col)+1) * (nRows - row)
    print(result)
    return result

solution(16,11,5,3)
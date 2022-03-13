from itertools import groupby
 
def solution(text):
    listAll=[]
    [listAll.append(list(group)) for key, group in groupby(text)]
    print(listAll)
    result=''
    j=0
    for i in range(len(listAll)):
        if len(listAll[i]) == 1:
            result += listAll[i][j]
        else:
            result+=str(len(listAll[i]))+listAll[i][j]
        print(result)
    return result

solution("aabbbc")
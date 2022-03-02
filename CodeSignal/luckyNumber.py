def solution(n):
    nString = str(n)
    digitMap=map(int,nString)
    digitList=list(digitMap)
    half=int(len(digitList)/2)
    firstHalf=digitList[:half]
    lastHalf=digitList[half:]
    print(lastHalf)
    if sum(firstHalf)==sum(lastHalf):
        return True
    else:
        return False


n=1230
solution(n)

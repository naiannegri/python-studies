def solution(n):
    highNum = int(str(n)[1:])
    strN = str(n)
    i = 1
    while i < len(str(n)):
        test = int(strN.replace(strN[i],"",1))
        if test > highNum:
            highNum = test 
        i+=1
    print(highNum)
    return highNum

solution(1001)
import collections
def solution(a,b):
    count=0
    counterA = collections.Counter(a)
    counterB = collections.Counter(b)
    check = counterA == counterB
    for i in range(len(a)):
        if a[i] == b[i]:
            pass
        else:
            count+=1
    if check == True and count <= 2:
        print(True)
        return True
    else:
        print(False)
        return False


#a=[4, 6, 3]
#b=[3, 4, 6]
a=[1,2,3]
b=[1,3,2]
solution(a,b)
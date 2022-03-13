def solution(st):
    if st == st[::-1]:
        return st
    i=0
    stRev=''
    tryStr=st[::-1]
    while tryStr != tryStr[::-1]:
        stRev += st[i]
        if len(stRev) >= 1:
            tryStr = st+stRev[::-1]
        i+=1 
        print(tryStr)
    print("abababa")
    return st + st[i::-1]



solution("ababab")
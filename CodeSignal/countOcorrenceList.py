import collections
def solution(names):
    newList = [] 
    for name in names:
        if name in newList:
            k = 1
            while "{}({})".format(name,k) in newList:
                k+=1
            name = "{}({})".format(name,k) 
        newList.append(name)
    print(newList)
    return newList
        


        

solution(["doc", "doc", "image", "doc(1)", "doc"])
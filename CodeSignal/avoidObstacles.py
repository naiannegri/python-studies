import functools

def solution(inputArray):
    sortedList = sorted(inputArray)
    maxNumber = functools.reduce(lambda a,b: a if a > b else b, sortedList)
    allValues = list(range(0,maxNumber + 2))
    mapResult = map(lambda number: None if number in sortedList else number, allValues)
    nonObst = list(mapResult)
    print(nonObst)
    filterResult = filter(None, nonObst)
    nonObst = list(filterResult)
    if 0 not in sortedList:
        nonObst.insert(0,0)
    print(sortedList,nonObst)
    sumValues=0
    b = 0
    jumpValues=[]
    obstValues=[]
    while b != len(nonObst) : 
        minJump = nonObst[b]
        for i in range(len(nonObst)):
            sumValues += minJump
            if sumValues in sortedList:
                obstValues.append(minJump)
                break
            else:
                if i == (len(nonObst) - 1):
                    jumpValues.append(minJump)
        sumValues=0
        b+=1
    filterResults=filter(None, jumpValues)
    jumpValues=list(filterResults)

    return jumpValues[0]



inputArray = [1, 4, 10, 6, 2]
solution(inputArray)
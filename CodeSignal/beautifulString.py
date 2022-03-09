from collections import Counter

def solution(inputString):
    counter = Counter(inputString)
    sortedDict = dict(sorted(counter.items()))
    sortedKeys = list(sortedDict.keys())
    alphaBet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    count = 0
    valuesView = sortedDict.values()
    valueIterator = iter(valuesView)
    firstValue = next(valueIterator)
    for key,value in sortedDict.items():
        if firstValue >= value and count != 0:
            firstValue = value
        elif firstValue < value:
            print(False)
            return False
        count+=1
    if sortedKeys != alphaBet[:len(sortedKeys)]:
        return False
    else:
        return True






solution("bbbaacdafe")
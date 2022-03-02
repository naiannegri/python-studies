def checkSize(inputArray):
    letterCount=0
    listValues=[]
    for word in inputArray:
        for letter in word:
            letterCount +=1
        listValues.append(letterCount)
        letterCount=0
    return listValues

def solution(inputArray):
    listValues=checkSize(inputArray)
    listNames=[]
    max_value = max(listValues)
    for number in listValues:
        if number == max_value:
            indices = [i for i, x in enumerate(listValues) if x == number]
    for value in indices:
        listNames.append(inputArray[value])
    return listNames

Array=["aba", 
 "aa", 
 "ad", 
 "vcd", 
 "aba"]
solution(Array)

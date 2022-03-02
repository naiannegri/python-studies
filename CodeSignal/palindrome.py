def solution(inputString):
    stringLength = len(inputString)
    slicedString = inputString[stringLength::-1]
    return slicedString == inputString
solution("aabaa")

import re
def solution(inputString):
    newStr = ''
    sumAll = 0
    for k in inputString.split("\n"):
        newStr += re.sub(r"[^0-9]+", ' ', k)
    listAll = newStr.split(" ")
    tryDig = list(filter( str.isdigit, listAll))
    print(listAll)
    for number in tryDig:
        sumAll += int(number)
    print(sumAll)
    return sumAll
solution("abcdefghijklmnopqrstuvwxyz1AbCdEfGhIjKlMnOpqrstuvwxyz23,74 -")
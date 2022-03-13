import re
def solution(a):
    newStr = ''
    for k in a.split("\n"):
        newStr += re.sub(r"[^a-zA-Z0-9]+", ' ', k)
    listStr = newStr.split(" ")
    biggerWord = listStr[0]
    for word in listStr:
        if len(word) > len(biggerWord):
            biggerWord = word
    print(biggerWord)
    return biggerWord


solution("You are the best!!!!!!!!!!!! CodeFighter ever!")
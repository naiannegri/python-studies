import re

def solution(inputString):
    findIndex = re.search(r"\d", inputString)
    return inputString[findIndex.start()]


solution("a a_933")
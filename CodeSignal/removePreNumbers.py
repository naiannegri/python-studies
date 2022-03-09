def solution(inputString):
    newStr = "" 
    if inputString[0].isdigit():
        for letter in inputString:
            if letter.isdigit():
                newStr += letter
            else:
                break
    print(newStr)
    return newStr
solution("12abc34")
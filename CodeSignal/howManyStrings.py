def solution(inputArray):
    countString = []
    for letter in inputArray:
        if letter in countString:
            pass
        else:
            countString.append(letter)
    return len(countString)

solution("cabca")
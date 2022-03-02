import collections
def solution(inputString):
    countEven=0
    countOdds=0
    countLetters=collections.Counter(inputString)
    values=countLetters.values()
    for keys in countLetters.values():
        if keys % 2 == 0:
            countEven+=1
        else:
            countOdds+=1
    if countOdds == 0 or countOdds <= 1:
        print(True)
        return True
    else:
        print(False)
        return False


inputString="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc"
solution(inputString)
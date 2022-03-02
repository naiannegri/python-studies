import re
def solution(inputString):
    count = 0
    lst=list(range(1,9+1))
    print(lst)
    test=inputString.split(".")
    matchResult = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$",inputString)
    for number in test:
        if number.isdigit():
            for digit in number:
                print(count,digit)
                if int(digit) == 0 and count == 1:
                    print(False)
                    return False
                if int(digit) == 0 and count == 0:
                    if len(number) > 1:
                        print(False)
                        return False
                count+=1
            count=0
    return bool(matchResult) and all(map((lambda number: number if 0 <= int(number) <= 255 else False), matchResult.groups()))
inputString = "01.1.1.0"
solution(inputString)
    
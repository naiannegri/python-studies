def solution(time):
    getHour = time.split(":")
    i = 0
    if 0 <= int(getHour[0]) < 24 and 0 <= int(getHour[1]) < 60:
        print(True)
        return True
    else:
        print(False)
        return False


solution("19:66")

import re
def solution(inputString):
    r = re.compile(r"\A([\dA-F]{2}[-]){5}([\dA-F]{2})\Z")
    if r.match(inputString):
        print(True)
        return True
    else:
        print(False)
        return False

solution("FF-FF-AB-CD-EA-BC")
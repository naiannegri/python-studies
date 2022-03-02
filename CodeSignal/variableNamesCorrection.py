import re
#Correct variable names consist only of English letters,
#  digits and underscores and they can't start with a digit.

import string
def solution(name):
    return name.isidentifier()




name = "qq-q"
solution(name)
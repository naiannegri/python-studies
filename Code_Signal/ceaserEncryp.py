import string
def caesarCipher(s):
    # Write your code here
    k=1
    listUpper = string.ascii_uppercase*100
    listLower = string.ascii_lowercase*100
    print(string.ascii_lowercase)
    for i in range(len(s)):
        letter = s[i]
        if letter.isupper():
            listPos = listUpper.find(letter)
            s=s[:i] + listUpper[listPos + k] + s[i+1:]
        elif letter.islower():
            listPos = listLower.find(letter)
            s=s[:i] + listLower[listPos + k] + s[i+1:]
    print(s)
    return s
s = "Always-Look-on-the-Bright-Side-of-Life"
caesarCipher(s,k)
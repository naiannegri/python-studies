

def reverseInParentheses(s):
        return eval('"' + s.replace('(', '"+("').replace('")[::-1]+"') + '"')

s = "foo(bar(baz))blim"
reverseInParentheses(s)
def solution(address):
    result = address.split('@')
    return result[len(result)-1]

solution("\"very.unusual.@.unusual.com\"@usual.com")
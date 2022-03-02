def solution(sequence):
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            a=i
        else:
            a=-1

    if a == -1:
        return True
    if sequence[a-1:a] + sequence[a+1:] == -1:
        return True
    return False
sequence = [1, 2, 3, 4, 99, 5, 6]
solution(sequence)

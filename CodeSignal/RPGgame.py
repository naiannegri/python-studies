def solution(experience, threshold, reward):
    if (experience + reward) < threshold:
        print(False)
        return False
    else:
        print(True)
        return True


solution(10,15,4)
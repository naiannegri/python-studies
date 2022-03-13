def solution(votes, k):
    winner = max(votes)
    count=0
    for i in range(len(votes)):
        newVal = votes[i]+k
        if newVal > winner:
            count+=1
    if count == 0 and votes.count(winner) > 1:
        return count
    elif count == 0 and votes.count(winner) <= 1:
        return 1
    return count
solution([5, 1, 3, 4, 1],0)
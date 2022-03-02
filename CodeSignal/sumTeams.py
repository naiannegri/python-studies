def solution(a):
    sumTeam1=sum(a[0::2])
    sumTeam2=sum(a[1::2])
    list=[sumTeam1,sumTeam2]
    return list

a=[50, 60, 60, 45, 70]
solution(a)
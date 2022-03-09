def solution(upSpeed, downSpeed, desiredHeight):
    dayCounter = 0
    nightHeight = upSpeed - downSpeed
    downSpeed = upSpeed - downSpeed
    print(downSpeed)
    while upSpeed < desiredHeight:
        dayCounter += 1
        upSpeed += nightHeight
        downSpeed += nightHeight
    return dayCounter+1

solution(100,10,910)
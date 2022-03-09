def solution(bishop, pawn):
    listValues = {"a": 8, "b": 7, "c": 6, "d": 5, "e": 4, "f": 3, "g": 2, "h": 1}
    for name in bishop:
        if name.isdigit():
            valueYBishop = int(name)
        else:
            valueXBishop = int(listValues[name])
    for name in pawn:
        if name.isdigit():
            valueYPawn = int(name)
        else:
            valueXPawn = int(listValues[name])
    canTakeDown(valueXBishop, valueYBishop, valueXPawn, valueYPawn)

def canTakeDown(bishopX, bishopY, pawnX, pawnY) :
 
 
    # If pawn is at angle
    # 45 or 225 degree from
    # bishop's Position
    if (pawnX - bishopX == pawnY - bishopY) :
        print(True)
        return True
     
    # If pawn is at angle
    # 135 or 315 degree from
    # bishop's Position
    elif (-pawnX + bishopX == pawnY - bishopY):
        print(True)
        return True
     
    else:
        return False

solution("a1","c3")
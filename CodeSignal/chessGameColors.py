def solution(cell1, cell2):
    valuesA = [0,1,0,1,0,1,0,1]
    valuesB = valuesA[::-1]
    valuesC = valuesB[::-1]
    valuesD = valuesC[::-1]
    valuesE = valuesD[::-1]
    valuesF = valuesE[::-1]
    valuesG = valuesF[::-1]
    valuesH = valuesG[::-1]
    listCell1 = list(map(lambda values: values,cell1))
    listCell2 = list(map(lambda values: values,cell2))
    if listCell1[0] == "A":
        color = valuesA[int(listCell1[1])-1]
    elif listCell1[0] == "B":
        color = valuesB[int(listCell1[1])-1]
    elif listCell1[0] == "C":
        color = valuesC[int(listCell1[1])-1]
    if listCell1[0] == "D":
        color = valuesD[int(listCell1[1])-1]
    elif listCell1[0] == "E":
        color = valuesE[int(listCell1[1])-1]
    elif listCell1[0] == "F":
        color = valuesF[int(listCell1[1])-1] 
    elif listCell1[0] == "G":
        color = valuesG[int(listCell1[1])-1]
    elif listCell1[0] == "H":
        color = valuesH[int(listCell1[1])-1]
    if listCell2[0] == "A":
        color2 = valuesA[int(listCell2[1])-1]
    elif listCell2[0] == "B":
        color2 = valuesB[int(listCell2[1])-1]
    elif listCell2[0] == "C":
        color2 = valuesC[int(listCell2[1])-1]
    if listCell2[0] == "D":
        color2 = valuesD[int(listCell2[1])-1]
    elif listCell2[0] == "E":
        color2 = valuesE[int(listCell2[1])-1]
    elif listCell2[0] == "F":
        color2 = valuesF[int(listCell2[1])-1] 
    elif listCell2[0] == "G":
        color2 = valuesG[int(listCell2[1])-1]
    elif listCell2[0] == "H":
        color2 = valuesH[int(listCell2[1])-1]  
    print(color,color2)
    if color == color2:
        print(True)
        return True
    else:
        print(False)
        return False   

cell1 = "A1"
cell2 = "A2"
solution(cell1,cell2)
import numpy as np

def calculate(listA):
    try:
        newArray = np.array(listA)
        newMatrix = newArray.reshape((3,3))

        #axis1
        axis1, axis1_2, axis1_3 = newMatrix[:,0],newMatrix[:,1],newMatrix[:,2]

        #axis2
        axis2, axis2_2, axis2_3 = newMatrix[0], newMatrix[1], newMatrix[2]

        #media
        meanAxis1, meanAxis1_2, meanAxis1_3 = np.mean(axis1), np.mean(axis1_2), np.mean(axis1_3)
        meanAxis2, meanAxis2_2, meanAxis2_3 = np.mean(axis2), np.mean(axis2_2), np.mean(axis2_3)
        meanFlat = np.mean(listA)
        print(newMatrix,axis1, axis1_2, axis1_3)

        #variância
        varAxis1, varAxis1_2, varAxis1_3 = np.var(axis1), np.var(axis1_2), np.var(axis1_3)
        varAxis2, varAxis2_2, varAxis2_3 = np.var(axis2), np.var(axis2_2), np.var(axis2_3)
        varFlat = np.var(listA)

        #sd
        stdAxis1, stdAxis1_2, stdAxis1_3 = np.std(axis1), np.std(axis1_2), np.std(axis1_3)
        stdAxis2, stdAxis2_2, stdAxis2_3 = np.std(axis2), np.std(axis2_2), np.std(axis2_3) 
        stdFlat = np.std(listA)

        #max
        axis1Array = [axis1,axis1_2,axis1_3]
        axis1Matrix = np.array(axis1Array)
        axis1Max = list(np.amax(axis1Matrix,axis=0))

        axis2Array = [axis2,axis2_2,axis2_3]
        axis2Matrix = np.array(axis2Array)
        axis2Max = list(np.amax(axis2Matrix,axis=0))

        maxList = np.amax(listA)
        print(axis1Max)


        #min
        axis1Min = list(np.amin(axis1Matrix,axis=0))
        axis2Min = list(np.amin(axis2Matrix,axis=0))
        minList = np.amin(listA)

        #sumValues
        sumAxis1, sumAxis1_2, sumAxis1_3 = np.sum(axis1), np.sum(axis1_2), np.sum(axis1_3)
        sumAxis2, sumAxis2_2, sumAxis2_3 = np.sum(axis2), np.sum(axis2_2), np.sum(axis2_3)
        sumList = np.sum(listA)

        
        dictValues = {'mean': [[meanAxis1, meanAxis1_2, meanAxis1_3], [meanAxis2, meanAxis2_2, meanAxis2_3], meanFlat],
        'variance': [[varAxis1, varAxis1_2, varAxis1_3], [varAxis2, varAxis2_2, varAxis2_3], varFlat],
        'standard deviation': [[stdAxis1, stdAxis1_2, stdAxis1_3], [stdAxis2, stdAxis2_2, stdAxis2_3], stdFlat],
        'max': [axis2Max, axis1Max, maxList],
        'min': [axis2Min, axis1Min, minList],
        'sum': [[sumAxis1, sumAxis1_2, sumAxis1_3], [sumAxis2, sumAxis2_2, sumAxis2_3], sumList]}
        print(dictValues)
    except:

        raise ValueError('List must contain nine numbers.')

    return dictValues

    

calculate([2,6,2,8,4,0,1,])
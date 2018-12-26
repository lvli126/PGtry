import numpy as np
import math

def process_comparision(numMatrix1,numMatrix2,energyMatrix1,energyMatrix2,theta1,theta2)
#numMatrix1,energyMatrix1,theta1 represent hits collection, energy deposition and incidence direction of test1.
#numMatrix2,energyMatrix2,theta2 represent hits collection, energy deposition and incidence direction of test2.
#only compare half of matrix because of symmetry    
    numMX=numMatrix1.shape[0]
    numMY=numMatrix1.shape[1]
    numMZ=numMatrix1.shape[2]
    for i in range(numMX)
        for j in range(numMY)
            for k in range(numMZ)
                if (numMatrix1[i][j][k]==numMatrix2[i][j][k] or (numMatrix1[i][j][k]!=numMatrix2[i][j][k] and 
                   (numMatrix1[i][j][k]==0 or numMatrix2[i][j][k]==0))):
                    print("numMatrix are same")
                else:
                    print("numMatrix are different")
                if (energyMatrix1[i][j][k]==energyMatrix2[i][j][k] or (energyMatrix1[i][j][k]!=energyMatrix2[i][j][k] and 
                   (energyMatrix1[i][j][k]==0 or energyMatrix2[i][j][k]==0))):
                    print("energyMatrix are same")
                else:
                    print("energyMatrix are different")
                                              


   
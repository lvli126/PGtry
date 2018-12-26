import numpy as np
import math

def process_translation(g):
    for i in range(0,3):
        g[1][i]-=g[0][i+3]
    g[0][3:6]=np.array([0,0,0])
    return g

def process_rotation(g,theta):
    dirx=g[0][0]
    diry=g[0][1]
    m=np.sqrt(pow(dirx,2)+pow(diry,2))
    matrix_z=np.array([[dirx/m,-diry/m,0],[diry/m,dirx/m,0],[0,0,1]])
    g[0][0:3]=np.dot(g[0][0:3],matrix_z)
    dirx2=g[0][0]
    dirz2=g[0][2]
    n=np.sqrt(pow(dirx2,2)+pow(dirz2,2))
    matrix_y=np.array([[math.cos(theta)*dirx2/n+math.sin(theta)*dirz2/n,0,math.sin(theta)*dirx2/n-math.cos(theta)*dirz2/n],
                       [0,1,0],
                       [-math.sin(theta)*dirx2/n+math.cos(theta)*dirz2/n,0,math.cos(theta)*dirx2/n+math.sin(theta)*dirz2/n]])
#    matrix_y=np.array([[-dirz2/n,0,-dirx2/n],[0,1,0],[dirx2/n,0,-dirz2/n]])
    g[1][0:3]=np.transpose(np.dot(np.dot(np.transpose(g[1][0:3]),matrix_z),matrix_y))
    g[0][0:3]=np.dot(g[0][0:3],matrix_y)
#    g[0][3:6]=np.transpose(g[1][0:3,0])

#    g[0][0:3]=np.dot(g[0][0:3],matrix_y)
#    g[0][0:3]=np.dot(np.dot(g[0][0:3],matrix_z),matrix_y)
#    print(lin1)
#    print(lin2)

    return g

def process_run(data,theta):
    l=data.shape[0]
    for i in range(0,l):
        process_translation(data[i])
#        print(data)    
        process_rotation(data[i],theta)
    return data

data=np.load('try.npy')
result=process_run(data,math.pi/2)
print(result)      
   

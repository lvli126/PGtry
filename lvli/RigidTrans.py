import numpy as np
import math

def process_translation(g):
    for i in range(0,3):
        g[1][i]-=g[0][i+3]
    g[1][2]+=10
    g[0][3:6]=[0,0,10]
    #g[0][3:5]=np.transpose(g[1][0:2,0])
    return g

def process_rotation(g,theta):
    dirx=g[0][0]
    diry=g[0][1]
    m=np.sqrt(pow(dirx,2)+pow(diry,2))
#rotation matrix around axis z: Rotate the incident direction around the z-axis to the x-axis
    matrix_z=np.array([[dirx/m,-diry/m,0],[diry/m,dirx/m,0],[0,0,1]])
    g[0][0:3]=np.dot(g[0][0:3],matrix_z)
    dirx2=g[0][0]
    dirz2=g[0][2]
    n=np.sqrt(pow(dirx2,2)+pow(dirz2,2))
#rotation matrix around y-axis: Rotate the x-axiss around the y-axis to the z-axis
    matrix_y=np.array([[-dirz2/n,0,-dirx2/n],[0,1,0],[dirx2/n,0,-dirz2/n]])
#    g[0][3:6]=np.transpose(g[1][0:3,0])
#rotation matrix around y-axis: Rotate the z-axiss around the y-axis to other direction
    matrix_y2=np.array([[np.cos(theta),0,-np.sin(theta)],[0,1,0],[np.sin(theta),0,np.cos(theta)]])
    g[1][0:3]=np.transpose(np.dot(np.dot(np.dot(np.transpose(g[1][0:3]),matrix_z),matrix_y),matrix_y2))
    g[0][0:3]=np.dot(np.dot(g[0][0:3],matrix_y),matrix_y2)
#    g[0][0:3]=np.dot(g[0][0:3],matrix_y)
#    g[0][0:3]=np.dot(np.dot(g[0][0:3],matrix_z),matrix_y)
#    print(lin1)
#    print(lin2)

    return g

def process_run(data,theta):
    l=data.shape[0]
    for i in range(0,l):
        data[i]=process_translation(data[i])    
        data[i]=process_rotation(data[i],theta)
    return data

data=np.load('try.npy')
result=process_run(data,math.pi/4)
print(result)      
   

import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np
filename = input('enter filename')
coordt = np.load("D:/MUSEN Materials/Musen export/" + filename + ".npy",allow_pickle='True').item()
#print (coordt)
fig = plt.figure(figsize=(15,6))
ax = p3.Axes3D(fig)
limits = [-0.01,0.01,-0.01,0.01]
ax.axis(limits)
x = [0, 0]
y = [0, 0]
z = [0.01, -0.01]

print (coordt.keys())
points, = ax.plot(x, y, z, '.')
def update_points(num, x, y, z, points):
    x = [0, 0, -0.01, 0.01]
    y = [0, 0, 0, 0]
    z = [0.01, -0.01, 0 , 0 ]
    if num!=0 and num != 1:
        n = int((num*5)*(10**-4)*10000)/10000
        #print(n)
        for k in coordt[n].keys():
            x.append(coordt[n][k][0])
            y.append(coordt[n][k][1])
            z.append(coordt[n][k][2])


        points.set_data(x, y)
        points.set_3d_properties(z, 'z')
    return points
ani = animation.FuncAnimation(fig, update_points, frames=len(coordt.keys())-4, fargs=(x, y, z, points))

plt.show()

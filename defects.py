
import matplotlib.pyplot as plt
import numpy as np
coordt = np.load("D:\MUSEN Materials\Musen export\dict2m2.npy",allow_pickle='True').item()
print (coordt)

x = [0,0]
y = [0,0]
z = [0.01,-0.01]

xl = np.linspace(-0.005,0.005,1000)
yl = np.full((1000),0.005)
zl = np.full((1000),-0.01)

xl1 = np.linspace(-0.005,0.005,1000)
yl1 = np.full((1000),-0.005)
zl1 = np.full((1000),-0.01)


xl2 = np.linspace(-0.005,0.005,1000)
yl2 = np.full((1000),0.005)
zl2 = np.full((1000),0.01)

xl4 = np.linspace(-0.005,0.005,1000)
yl4 = np.full((1000),-0.005)
zl4 = np.full((1000),0.01)


yl5 = np.linspace(-0.005,0.005,1000)
xl5 = np.full((1000),0.005)
zl5 = np.full((1000),-0.01)


yl6 = np.linspace(-0.005,0.005,1000)
xl6 = np.full((1000),-0.005)
zl6 = np.full((1000),-0.01)

yl7 = np.linspace(-0.005,0.005,1000)
xl7 = np.full((1000),0.005)
zl7 = np.full((1000),0.01)

yl8 = np.linspace(-0.005,0.005,1000)
xl8 = np.full((1000),-0.005)
zl8 = np.full((1000),0.01)

zl9 = np.linspace(-0.01,0.01,1000)
xl9 = np.full((1000),0.005)
yl9 = np.full((1000),0.005)

zl10 = np.linspace(-0.01,0.01,1000)
xl10 = np.full((1000),-0.005)
yl10= np.full((1000),-0.005)

for t in range(2,11):
    for k in coordt[t*(10**-3)].keys():
        x.append(coordt[t*(10**-3)][k][0])
        y.append(coordt[t*(10**-3)][k][1])
        z.append(coordt[t*(10**-3)][k][2])

    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot( projection = '3d')
    sc = ax.scatter(x,y,z,'r')
    sc = ax.scatter(xl,yl,zl,c = 'b')
    sc = ax.scatter(xl1,yl1,zl1,c = 'b')
    sc = ax.scatter(xl2,yl2,zl2,c = 'b')
    sc = ax.scatter(xl4,yl4,zl4,c = 'b')
    sc = ax.scatter(xl5,yl5,zl5,c = 'b')
    sc = ax.scatter(xl6,yl6,zl6,c = 'b')
    sc = ax.scatter(xl7,yl7,zl7,c = 'b')
    sc = ax.scatter(xl8,yl8,zl8,c = 'b')
    sc = ax.scatter(xl9,yl9,zl9,c = 'b')
    sc = ax.scatter(xl10,yl10,zl10,c = 'b')

    plt.show()

    x = [0, 0]
    y = [0, 0]
    z = [0.01, -0.01]

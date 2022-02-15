import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
filename1 = input('Please enter filename1')
filename2 = input('Please enter filename2')
data = pd.read_csv("D:/MUSEN Materials/Musen export/" + filename1 + ".txt",sep=' ',header=None)
datapart = pd.read_csv("D:/MUSEN Materials/Musen export/" + filename2+ ".txt",sep = ' ',header=None)
filename = input('Enter the filname')
ind = []
for i in range(1,len(data.columns)):
    if data[i][0] == 2 or data[i][0] == 12 or data[i][0] == 18:
        ind.append(i)
print (data)
print('ind ',ind)
data = data.drop([2,5,6], axis='columns')
datapart = datapart.drop([2,3,4], axis='columns')
bonds = {}
# getting the time of bonds breakage
n = 0
for j in data.index:
    m = 0
    n += 1

    for i in data.columns:
        try:
            if data[i][j] == 2 and data [i+1][j] !=0:
                #print('*')
                if data [i+6][j] == 18:
                # print('-')
                    if data [i+7][j] == 0:
                        print('+')
                        bonds.update({data[1][j]:[data [i+1][j],data [1][j],data [3][j],data [4][j]]})
                        break
                    else:
                        continue
        except Exception:
            pass
print('part1')

# creating a dictionary with times and bonds broken during these times
times = []
m=0
for i in data.columns:
    m += 1

    if data[i][1] == 2 and data [i+1][1] !=0:
        times.append(data[i+1][1])
np.save("D:\MUSEN Materials\Musen export\Times.npy",times)
print('part2')
#print('bonds ',bonds)

newbonds = {}
m=0
for j in times:
    m += 1

    ar = []
    #print(j)
    for i in bonds.keys():
            if bonds[i][0] == j:
                ar.append(bonds[i])
    newbonds.update({j:ar})

print('part3')
#print(newbonds[0.015])
# geting coordinates of the particles
print('datapart.columns ',datapart.columns)
particles = {}
for j in datapart.index:
    ar2 = {}
    m=0
    for i in datapart.columns:
        m += 1
        if i >4:
            if datapart[i][j] == 2:
                #print(data[i+1][j])
                if datapart [i+2][j] == 12:
                    ar2.update({datapart[i+1][j]:[datapart[i+3][j],datapart[i+4][j],datapart[i+5][j]]})
    particles.update({datapart[1][j]:ar2})

print('part4')
#print('particles ',particles)

#getting the cordinates of the bonds


#print (newbonds[0.015])
coordt = {}
print (particles)
for j in times:
    m = 0
    coord = {}
    print(j)
    for i in newbonds[j]:
        try:
            #print([(particles[newbonds[j][m][2][j][0] + particles[newbonds[j][m][3]][j][0]) / 2,(particles[newbonds[j][m][2]][j][1] + particles[newbonds[j][m][3]][j][1]) / 2,(particles[newbonds[j][m][2]][j][2] + particles[newbonds[j][m][3]][j][2]) / 2])
            coord.update({newbonds[j][m][1]:[(particles[newbonds[j][m][2]][j][0] + particles[newbonds[j][m][3]][j][0])/2,(particles[newbonds[j][m][2]][j][1] + particles[newbonds[j][m][3]][j][1])/2,(particles[newbonds[j][m][2]][j][2] + particles[newbonds[j][m][3]][j][2])/2]})
        except Exception:

            pass
        m+=1
        #print (coord)
    coordt.update({j:coord})
print(coordt)
print('part4')
t = 0.006
#print(coordt[t])
#print(coordt[t].keys())n
np.save("D:/MUSEN Materials/Musen export/" + filename + ".npy" ,coordt)

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


for k in coordt[t].keys():
    x.append(coordt[t][k][0])
    y.append(coordt[t][k][1])
    z.append(coordt[t][k][2])

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
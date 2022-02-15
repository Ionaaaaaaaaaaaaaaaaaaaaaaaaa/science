import pandas as pd
import matplotlib.pyplot as plt
import math as m
import numpy as np
data = pd.read_csv("D:/MUSEN Materials/Musen export/161 bonds.txt",sep=' ',header=None)
datapart = pd.read_csv("D:/MUSEN Materials/Musen export/161 particles.txt",sep = ' ',header=None)
ind = []

for i in range(1,len(data.columns)):
    if data[i][0] == 2 or data[i][0] == 12 or data[i][0] == 18:
        #print('*')
        ind.append(i)
#print(ind)
data = data.drop([2,3,4], axis='columns')
datapart = datapart.drop([2,3,4], axis='columns')
#print(datapart)
bonds = {}
# getting the time of bonds breakage
n = 0
#print(data[9])
for j in data.index:
    m = 0
    n += 1
    for i in data.columns:
        if data[i][j] == 2 and data [i+1][j] !=0:
            #print('*')
            #print(data[i+1][j])

            if data [i+6][j] == 18:
               # print('-')
                if data [i+7][j] == 0:
                   # print('+')
                    bonds.update({data[1][j]:[data [i+1][j],data [1][j],data [5][j],data [6][j]]})
                    break
                else:
                    continue
print('part1')
#print('//n')
# creating a dictionary with times and bonds broken during these times
times = []
m=0
for i in data.columns:
    if data[i][1] == 2 and data [i+1][1] !=0:
        times.append(data[i+1][1])
print('part2')
#print(times)
#print(bonds)
#print('//n')
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
#print('//n')
print('part3')
#print('new',newbonds)
# geting coordinates of the particles
#print(datapart.columns)
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
   # print('//n')
print('part4')
#print('part',particles)

#getting the cordinates of the bonds


#print (newbonds[0.015])
coordt = {}
for j in times:
    m = 0
    coord = {}
    #print(j)
    #print (len(newbonds[j]))
    if j == 0.015:
        break
    m=0
    for i in newbonds[j]:

        n += 1
        m = m+1
        #if m > len(newbonds[j])-10:
           # break
        try:
            coord.update({newbonds[j][m][1]:[(particles[newbonds[j][m][2]][j][0] + particles[newbonds[j][m][3]][j][0])/2,(particles[newbonds[j][m][2]][j][1] + particles[newbonds[j][m][3]][j][1])/2,(particles[newbonds[j][m][2]][j][2] + particles[newbonds[j][m][3]][j][2])/2]})
            #print({newbonds[j][m][1]: [(particles[newbonds[j][m][2]][j][0] - particles[newbonds[j][m][3]][j][0]) / 2,
                           #      (particles[newbonds[j][m][2]][j][1] - particles[newbonds[j][m][3]][j][1]) / 2,
                              #   (particles[newbonds[j][m][2]][j][2] - particles[newbonds[j][m][3]][j][2]) / 2]})
        except Exception:
            pass
        m+=1
    #print (coord)
    coordt.update({j:coord})
    #print('//n')
print('part4')
print(coordt.keys())
t = 0.011
print('8888',coordt)
np.save("D:\MUSEN Materials\Musen export\dict.npy",coordt)
x = [0,0]
y = [0,0]
z = [0.01,-0.01]
xl = np.linspace(-5,5,1000)
yl = np.full((1000),5)
zl = np.full((1000),-10)

xl1 = np.linspace(-5,5,1000)
yl1 = np.full((1000),-5)
zl1 = np.full((1000),-10)


xl2 = np.linspace(-5,5,1000)
yl2 = np.full((1000),5)
zl2 = np.full((1000),10)

xl4 = np.linspace(-5,5,1000)
yl4 = np.full((1000),-5)
zl4 = np.full((1000),10)


yl5 = np.linspace(-5,5,1000)
xl5 = np.full((1000),5)
zl5 = np.full((1000),-10)


yl6 = np.linspace(-5,5,1000)
xl6 = np.full((1000),-5)
zl6 = np.full((1000),-10)

yl7 = np.linspace(-5,5,1000)
xl7 = np.full((1000),5)
zl7 = np.full((1000),10)

yl8 = np.linspace(-5,5,1000)
xl8 = np.full((1000),-5)
zl8 = np.full((1000),10)

zl9 = np.linspace(-10,10,1000)
xl9 = np.full((1000),5)
yl9 = np.full((1000),5)

zl10 = np.linspace(-10,10,1000)
xl10 = np.full((1000),-5)
yl10= np.full((1000),-5)



#print(coordt[t])
for k in coordt[t].keys():
        x.append(coordt[t][k][0])
        y.append(coordt[t][k][1])
        z.append(coordt[t][k][2])


fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot( projection = '3d')
#print(y)
sc = ax.scatter(x,y,z)
sc = ax.scatter(xl,yl,zl)
sc = ax.scatter(xl1,yl1,zl1)
sc = ax.scatter(xl2,yl2,zl2)
sc = ax.scatter(xl4,yl4,zl4)
sc = ax.scatter(xl5,yl5,zl5)
sc = ax.scatter(xl6,yl6,zl6)
sc = ax.scatter(xl7,yl7,zl7)
sc = ax.scatter(xl8,yl8,zl8)
sc = ax.scatter(xl9,yl9,zl9)
sc = ax.scatter(xl10,yl10,zl10)
plt.show()
defects = {}
flag = 0
for j in times:
    if flag == 0:
        try:
            le = len(coordt[j])
            print(le)
            if le > 1:
                print (le)
                n = 0
                for i in coordt[j].keys():
                    n+=1
                    defects.update({'defect_'+ str(n):[i]})
            #flag = 1
            if le > 1:
                ti = j
                break

        except Exception:
            pass
print (defects)
used = []
for j in times:

        try:
            if len(coordt[j]) >1:
                for i in coordt[j].keys():
                   # print (i)
                    for m in defects.keys():
                        for n in defects[m]:
                            if i not in defects[m]:
                                if i not in used:
                                    try:
                                        print (abs(np.sqrt((coordt[j][i][0] - coordt[j][n][0])**2 + (coordt[j][i][1] - coordt[j][n][1])**2 + (coordt[j][i][2] - coordt[j][n][2])**2)))
                                        if abs(np.sqrt((coordt[j][i][0] - coordt[j][n][0])**2 + (coordt[j][i][1] - coordt[j][n][1])**2 + (coordt[j][i][2] - coordt[j][n][2])**2)) <=0.005:
                                            defects[m].append(i)
                                            used.append(i)
                                        else:
                                            defects.update({'defect_'+ str(i):[i]})
                                    except Exception:
                                        pass
        except Exception:
            pass
print (defects)
coordb = {}
for m in coordt.keys():
    for n in coordt[m].keys():
        coordb.update({n:coordt[m][n]})
print (coordb)
X = {}
Y = {}
Z = {}
for j in defects.keys():
     X.update({'x ' + j:[]})
     for i in defects[j]:
         X['x ' + j].append(coordb[i][0])
     Y.update({'x ' + j: []})
     for i in defects[j]:
        Y['x ' + j].append(coordb[i][1])
     Z.update({'x ' + j: []})
     for i in defects[j]:
        Z['x ' + j].append(coordb[i][2])
print(X)
print (Y)
print (Z)
plt.figure(figsize = (20,10))
n = 0
i = 'x defect_1'
ax = fig.add_subplot(projection='3d')
sc = ax.scatter(X[i], Y[i], Z[i])
#plt.show()
#plt.savefig("D:/MUSEN Materials/figs/fg" + str(n)+ '.png')


#getting the defects
#ar3 = {}
#defdict = {}
#print(coordt[0.011].keys())
#for i in coordt[0.006].keys():
#
#    ar4 = []
#    for j in coordt[0.006].keys():
#        #print(type(((coordt[0.011][i][0]) ** 2 - (coordt[0.011][j][0]) ** 2) + ((coordt[0.011][i][1]) ** 2 - (coordt[0.011][j][1]) ** 2) + ((coordt[0.011][i][2]) ** 2 - (coordt[0.011][j][2]) ** 2)))
#        if coordt[0.006][j] != coordt[0.006][i]:
#            if np.sqrt(abs(((coordt[0.006][i][0]) ** 2 - (coordt[0.006][j][0]) ** 2) + ((coordt[0.006][i][1]) ** 2 - (coordt[0.006][j][1]) ** 2) + ((coordt[0.006][i][2]) ** 2 - (coordt[0.006][j][2]) ** 2))) < 0.002:
#                   ar4.append(j)
#    ar3.update({i:ar4})

#print (ar3[70])
#weights = [len(ar3[i]) for i in ar3.keys()]
#weights.sort()
#print (weights)
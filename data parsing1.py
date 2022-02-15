import pandas as pd
import matplotlib.pyplot as plt
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
print(data[9])
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
print(times)
print(bonds)
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
print('new',newbonds)
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
print('part',particles)

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

x = [0,0]
y = [0,0]
z = [0.01,-0.01]
print(coordt[t])
for k in coordt[t].keys():
        x.append(coordt[t][k][0])
        y.append(coordt[t][k][1])
        z.append(coordt[t][k][2])


fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot( projection = '3d')

print(y)
sc = ax.scatter(x,y,z)
plt.show()
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

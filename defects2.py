import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
filename1 = input('Please enter filename1')
filename2 = input('Please enter filename2')
coordt = np.load("D:/MUSEN Materials/Musen export/" + filename1 + ".npy",allow_pickle='True').item()
# print (coordt)
r = float(input('Please Enter radius'))
data = pd.read_csv("D:/MUSEN Materials/Musen export/" + filename2 + ".txt",sep=' ',header=None)
m = 0

coordb = {}
for m in coordt.keys():
    for n in coordt[m].keys():
        coordb.update({n: coordt[m][n]})

times = []
for i in data.columns:
    m += 1

    if data[i][1] == 2 and data [i+1][1] != 0:
        times.append(data[i+1][1])

used = []
defects = {}
flag = 0
for j in times:
    #print (j)
    if flag == 0:
        try:
            le = len(coordt[j])
            #print(le)
            if le > 0:
                #print (le)
                n = 0
                for i in coordt[j].keys():
                    n+=1
                    defects.update({'defect_'+ str(n):[i]})
                    used.append(i)
            # flag = 1
            if le > 1:
                ti = j
                break

        except Exception:
            pass
#print (defects)
for j in times:
        print (j)
        # try:
        if len(coordt[j]) >0:
                d = 0
                for i in coordt[j].keys():
                    d += 1
                    #print (d/len(coordt[j].keys()))
                    ip = 0
                    tn = False
                    while tn == False:
                        #print (defects)
                        ar = [i for i in defects.keys()]
                        #print (ar)
                        m = ar[ip]

                        for n in defects[m]:
                            #print (i)
                            # print(m)
                            if i not in used:
                                        #try:

                                        # print(coordt[j][i][0])
                                        # print ('nnn')
                                        # print (i,n)

                                        # print('--------------')
                                        # print (abs(np.sqrt((coordt[j][i][0] - coordt[j][n][0])**2 + (coordt[j][i][1] - coordt[j][n][1])**2 + (coordt[j][i][2] - coordt[j][n][2])**2)))
                                        if abs(np.sqrt((coordt[j][i][0] - coordb[n][0])**2 + (coordt[j][i][1] - coordb[n][1])**2 + (coordt[j][i][2] - coordb[n][2])**2)) <= r:
                                            defects[m].append(i)
                                            used.append(i)
                                        else:
                                            defects.update({'defect_'+ str(i):[i]})
                        ip += 1
                                        #except Exception:
                        if ip == len(ar):
                            tn = True
                            #  pass
        print(defects)
        #except Exception:
            #pass
print (defects)
np.save("D:\MUSEN Materials\Musen export\defects.npy",defects)
coordb = {}
for m in coordt.keys():
    for n in coordt[m].keys():
        coordb.update({n:coordt[m][n]})
#print (coordb)
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
print (X)
print (Y)
print (Z)

fig = plt.figure(figsize = (20,10))
n = 0
i = 'x defect_2'
ax = fig.add_subplot(projection='3d')
sc = ax.scatter(X[i], Y[i], Z[i])
#plt.show()
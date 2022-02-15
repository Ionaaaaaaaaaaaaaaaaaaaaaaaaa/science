import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
dictname = input('Please enter filename1 ')
filename = input('Please enter the filename ')
coordt = np.load("D:/MUSEN Materials/Musen export/" + dictname + ".npy",allow_pickle='True').item()
# print (coordt)
m = 0
#print(coordt)
dictr = {}
for i in coordt.keys():
    for j in coordt[i]:
        #print (coordt[i][j])
        dictr.update({j:coordt[i][j]})
print (dictr)
R = []
for n in dictr.keys():
    for m in dictr.keys():
        R.append(abs(np.sqrt((dictr[n][0] - dictr[m][0])**2 + (dictr[n][1] - dictr[m][1])**2 + (dictr[n][2] - dictr[m][2])**2)))
np.save("D:/MUSEN Materials/Musen export/" + filename + ".npy" ,R)
print ('Minimal distance',min(R))
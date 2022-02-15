import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("D:\MUSEN Materials\Musen export\exttime export - Copy.txt",sep=' ',header=None)
datapart = pd.read_csv("D:\MUSEN Materials\Musen export\exttime part.txt",sep = ' ',header=None)
ind = []
for i in range(1,len(data.columns)):
    if data[i][0] == 2 or data[i][0] == 12 or data[i][0] == 18:
        ind.append(i)

print('ind ',ind)
data = data.drop([2,5,6], axis='columns')
datapart = datapart.drop([2,3,4], axis='columns')
print (data)
print (datapart)
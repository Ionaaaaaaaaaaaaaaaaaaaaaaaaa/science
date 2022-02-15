import pandas as pd
import matplotlib.pyplot as plt


# Working with data about stresses
modelname = input('Please enter the name of the model you want to assess ')
bondstype = input('Please enter the type of bonds you want to assess ')
Save_file = input ('Please enter YES if you want to save figure')
if Save_file == 'YES' :
    file_name = input('Please enter the filename for the results ')
datatype1 = 'stress'
datatype2 = 'emission'
dfimport = pd.read_csv("D:/MUSEN Materials/" + modelname  +"/" +modelname+ datatype1 + ".mdem.csv",sep = ';',header=0)
df = dfimport
df[' Min'] = abs(df[' Min'])
print(dfimport)

# Working with acoustic emission data
DfAcimport = pd.read_csv("D:/MUSEN Materials/" + modelname  +"/" +modelname+ datatype2 + ".mdem.csv",sep = ';',header = 0)
DfAc = DfAcimport
print (DfAc)
DfAc['Emission'] = DfAc[' Value']/2
for i in range(0, len(DfAc['Emission']) - 1):
    DfAc['Emission'][i] = abs(DfAc[' Value'][i + 1] - DfAc[' Value'][i])
DfAc['Emission'][len(DfAc[' Value'])-1] = DfAc['Emission'][len(DfAc[' Value'])-2]
DfAc = DfAc.drop([' Value'], axis='columns')
print (DfAc)


# Demonstration of results with grafs
plt.figure(figsize=(20,10))

plt.subplot(1,2,1)
plt.plot(df)
plt.title('Max local stress for model with bonds ' + bondstype)
plt.xlabel('Time')
plt.ylabel('Max local stress')


plt.subplot(1,2,2)
plt.plot(DfAc)
plt.title('Intensity of emission for model with bonds ' + bondstype)
plt.xlabel('Time')
plt.ylabel('Intensity of emission')
if Save_file == 'YES' :
    plt.savefig('D:/MUSEN Materials/' + modelname + '/Python figs/' + modelname + ' ' + bondstype + ' ' + file_name + ' not divided.png')
plt.show()


import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,1,10000)

f1 = np.sqrt(np.sqrt(1-x)/(1-2/3*x))
plt.figure(figsize=(10,5))
plt.plot(x,f1,c = 'b')
plt.xlabel('δ',fontdict={'fontsize': 25, 'fontweight': 'medium'})
plt.ylabel('ρ',fontdict={'fontsize': 25, 'fontweight': 'medium'})
plt.show()
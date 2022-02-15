import matplotlib.pyplot as plt
import numpy as np
import math as m

x = np.linspace(0,2,10000)

f1 = np.sqrt((2-x**2)/(9*m.pi/4+x*(7+x**2)/2 + 2*(x**2-2)))

plt.figure(figsize=(10,5))
plt.plot(x,f1,c = 'b')
plt.xlabel('δ',fontdict={'fontsize': 25, 'fontweight': 'medium'})
plt.ylabel('ρ',fontdict={'fontsize': 25, 'fontweight': 'medium'})
plt.show()
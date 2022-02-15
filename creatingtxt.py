import numpy as np
import pandas as pd
coordt = np.load("D:\MUSEN Materials\Musen export\dict2.npy",allow_pickle='True').item()
coordtdf = pd.DataFrame(coordt)
coordtdf.to_csv("D:\MUSEN Materials\Musen export\coordtdf.csv")
print (coordtdf)
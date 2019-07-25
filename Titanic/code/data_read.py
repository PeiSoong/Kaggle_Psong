"""
data_read.py : explore data
author : Psong
"""

# 
import numpy as np
import pandas as pd

# 
data_train = pd.read_csv("data/train.csv")
# print(data_train)

# 
data_train.info()
# 
import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams["font.sans-serif"] = ["SimHei"] # 中文显示问题
fig = plt.figure()
fig.set(alpha = 0.2)
# 
plt.subplot2grid((2, 3), (0, 0))
data_train.Survived.value_counts().plot(kind = 'bar')
plt.title(u"获救情况")
plt.ylabel(u"人数")
plt.show()


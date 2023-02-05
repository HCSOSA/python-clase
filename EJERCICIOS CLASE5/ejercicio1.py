import numpy as np
import matplotlib.pyplot as plt

array=np.array([[1,2,3,4],[1,2,3,4]])

x=[1,3,4,5]
y=np.sin(x)
fig,ax=plt.subplot()
ax.plot(x,y)
plt.show()  
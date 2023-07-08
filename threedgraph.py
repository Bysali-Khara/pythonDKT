import matplotlib.pyplot as plt
import numpy as np 
from mpl_toolkits import mplot3d

flg=plt.figure()

ax=plt.axes(projection="3d")
x=[0,1,2,3,4,5,6]
y=[0,1,34,56,78,34]
z=[4,56,33,90,45,67]

ax.plot3D(x,y,z,'green')
plt.rcParams['grid.color'] = "violet"
ax.scatter3D(x,y,z,c=z,cmp)
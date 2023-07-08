import numpy as np 
import matplotlib.pyplot as plt
x = []
y = []
c = ["red","blue","yellow"]
n=int(input("Enter number of values:"))
for i in range(0,n):
    ch1=int(input("Enter the values of x-axis:"))
    x.append(ch1)
for i in range(0,n):
    ch2=int(input("Enter the values of y-axis:"))
    y.append(ch2)
#for i in range(0,n):
    #ch3=input("Enter color:")
    #c += str(ch3)
plt.bar(x,y, color = c)

plt.show()
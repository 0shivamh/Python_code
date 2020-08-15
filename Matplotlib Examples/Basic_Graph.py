from matplotlib import pyplot as plt
from matplotlib import style

x=[1,2,3,4]
y=[5,6,7,8]

x1=[4,6,1,9]
y1=[5,7,8,1]

plt.title("Info")
plt.xlabel("X-Axis")#to label 
plt.ylabel("Y-Axis")

plt.grid(True,color='k')#bg color for grid

plt.plot(x,y,'g',label='line one')
plt.plot(x1,y1,'r',label='line Two')


plt.show()
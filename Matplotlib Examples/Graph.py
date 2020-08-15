from matplotlib import pyplot as plt
from matplotlib import style


x=[1,2,3,4]
y=[5,6,7,8]
plt.plot(x,y)
plt.title("Matplot Info")
plt.xlabel("X-Axis")#to label 
plt.ylabel("Y-Axis")

plt.grid(True,color='k')#bg color for grid
plt.show()

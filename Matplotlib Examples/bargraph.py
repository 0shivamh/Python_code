from matplotlib import pyplot as plt
#bar graph
plt.bar([1,2,5,7,9],[5,2,7,8,2],label="h1")
plt.bar([2,4,6,8,10],[8,6,2,5,6],label="h2",color='g')

plt.legend()
plt.xlabel("Percent")
plt.ylabel("Nums")
plt.title("Owerall Info")
plt.show()

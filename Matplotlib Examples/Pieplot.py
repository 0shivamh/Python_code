from matplotlib import pyplot as plt
from matplotlib import style as ss


slices =[7,2,2,13]
activities=['Mobile','Desktop','Tablet','other']
cols=['c','m','r','b']
plt.pie(slices,
labels=activities,
colors=cols,
startangle=90,
shadow=True,
explode=(0,0.1,0,0),
autopct='%1.1f%%')

plt.show()
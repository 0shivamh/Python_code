from matplotlib import pyplot as plt
from matplotlib import style as ss

visitors_ages=[22,55,34,67,89,32,12,20]
bins=[0,10,20,30,40,50,60,70,80,90]

plt.hist(visitors_ages,bins,histtype='bar',rwidth=.8)
plt.show()
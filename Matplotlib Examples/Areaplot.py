from matplotlib import pyplot as plt 
days =[1,2,3,4,5]
workings =[2,3,4,3,2]
eating=[2,3,4,3,2]
sleeping=[7,8,10,6,7]
playing=[13,8,7,5,8]
plt.plot([],[],color='m',label='workings',linewidth=5)
plt.plot([],[],color='c',label='eating',linewidth=5)
plt.plot([],[],color='r',label='sleeping',linewidth=5)
plt.plot([],[],color='k',label='playing',linewidth=5)
plt.stackplot(days,workings,eating,sleeping,playing)
plt.show()
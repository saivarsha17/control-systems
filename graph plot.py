import numpy as np
import matplotlib.pyplot as plt
l = np.linspace(-10,10,100)
L = []
M = []
X = []
def u(n):
    if (n >0):
        return 1
    else :
        return 0
def d(n):
    
    if (n==0):
        return 1
def x(n):
    return u(n)
def y(n):
    return u(n)-2*(np.exp(-n))*u(n)
def h(n):
    if(n==0):
        return -1+2*np.exp(-n)*u(n)
    else:
        return 2*np.exp(-n)*u(n)
        
for i in l:
    L.append(x(i))
    M.append(y(i))
    X.append(h(i))

plt.plot(l,L)

plt.plot(l,M)
plt.plot(l,X)
plt.plot(1.5,y(1.5),'o')
plt.text(1.5,y(1.5),(1.5,round(y(1.5),3)))

plt.legend(['y = x(t)','y = y(t)','y = h(t)'],loc = 'upper left')
plt.show()

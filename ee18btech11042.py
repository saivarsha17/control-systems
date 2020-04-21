import numpy as np
import matplotlib.pyplot as plt
import control 
G = control.tf([100,500],[1,3,4,12,0])
w = np.linspace(0.1,20,1000)
mag,phase,W = G.freqresp(w)
ax = plt.subplot(111,projection= 'polar')
ax.plot(phase.reshape((1000,))[-1000:],mag.reshape((1000,))[-1000:])
plt.plot(-1,0,'o')
plt.annotate('(-1,0)',(-1,0))
plt.show()


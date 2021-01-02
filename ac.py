import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10)

fig = plt.figure()
#plot leaky relu
ax = fig.add_subplot(121)
y_relu = np.array([0.2*item  if item<0 else item for item in x ]) 
ax.plot(x,y_relu)
ax.grid()
ax.set_title('(a) Leaky ReLu')

#plot mish
ax = fig.add_subplot(122)
y_mish=x*np.tanh(np.log(1+np.exp(x)))
ax.plot(x,y_mish)
ax.grid()
ax.set_title('(b) Mish')
plt.show()

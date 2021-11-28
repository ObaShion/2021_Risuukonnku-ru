import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline
N = 128
dt = 0.0002
freq = 523.23#周波数
amp = 1
t = np.arange(0, N*dt, dt)#x
f = amp * np.sin(2*np.pi*freq*t)#y
plt.xlabel('time(sec)', fontsize=14)
plt.ylabel('signal amplitude', fontsize=14)
plt.plot(t, f)
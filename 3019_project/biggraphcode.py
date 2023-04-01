import numpy as np
import matplotlib.pyplot as plt 
from scipy.signal import argrelextrema
data = np.loadtxt("student_023.txt", delimiter = " ") #Reading in data
time = []
brightness = []
for i in data:
    time.append(i[0])
    brightness.append(i[1])
brightness = np.array(brightness)
plt.plot(time, brightness) #Graph code
plt.title('Normalized Relative Brightness v.s. Time for a System with a 0.321M_Sun Star and a 11.564M_Earth planet', wrap = "True")
plt.xlabel('Time (seconds x $10^6$)')
plt.ylabel("Normalized Relative Brightness")
plt.savefig("Kolos-Furman_lightcurve_graph.png")
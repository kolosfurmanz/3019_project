import numpy as np
import matplotlib.pyplot as plt 
from scipy.signal import argrelextrema
import statistics as stats
data = np.loadtxt("student_023.txt", delimiter = " ")
time = []
brightness = []
for i in data:
    time.append(i[0])
    brightness.append(i[1])
brightness = np.array(brightness)
time1 = [i for i in time if i <= 10000] #filtering out most of the data to get the first minimum that occurs before 2 million seconds
brightness1 = brightness[:-(len(brightness) - len(time1))]
brightness4 = brightness[brightness.argmin() - int(len(time1)/2) - 1:brightness.argmin() + int(len(time1)/2)]
#These values are taken right at the minima of the graphs, the point at which the planet is blocking the most starlight
#The global minimum was the final minimum, which is what "argmin" is 
#Adding and subtracting the half of the length of the lists made this value be the midpoint
brightness2 = brightness[15694- int(len(time1)/2) - 1:15694 + int(len(time1)/2)]
brightness3 = brightness[23570 - int(len(time1)/2) - 1:23570 + int(len(time1)/2)]
#These index values above were found by looking at the data itself and seeing the local minima on the .txt file
plt.plot(time1, brightness1, color = 'red', label = 'Transit 2')
plt.plot(time1, brightness2, color = 'black', label = 'Transit 3')
plt.plot(time1, brightness3, color = 'green', label = 'Transit 4')
plt.plot(time1, brightness4, color = 'blue', label = 'Transit 5')
plt.title('Overplotted Transits with a Standard time of 10,000 Seconds')
plt.ylabel("Normalized Relative Brightness")
plt.xlabel("Time (seconds)")
plt.legend(loc = 'lower right')
plt.savefig('overplot.png')
depth1 = 1 - brightness[0]
depth2 = 1 - brightness[7720]
depth3 = 1 - brightness[15694]
depth4 = 1 - brightness[23570]
depth5 = 1 - brightness[brightness.argmin()]
#Depth calculated as 1 minus the brightness measured to get a distance
avgdepth = (depth1 + depth2 + depth3 + depth4 + depth5) / 5
print("The average brightness depth is approximately", '{0:1.3g}'.format(avgdepth))
planet_radius = 0.331*695500*np.sqrt(avgdepth)
#2nd value on right is solar radius from textbook
print("The planet's radius is approximately", '{0:1.3g}'.format(planet_radius), "km or", '{0:1.3g}'.format(planet_radius/6378), 
"Earth radii")
#6378 km used for Earth's radius, also from textbook 
sd1 = stats.stdev(1 - brightness1)
sd2 = stats.stdev(1 - brightness2)
sd3 = stats.stdev(1 - brightness3)
sd4 = stats.stdev(1 - brightness4)
sdavg = (sd1 + sd2 + sd3 + sd4) / 4
#Standard deviations found for all 4 datasets in graph, averaged to get global standard deviation for the transits 
sd = 0.331*695500*np.sqrt(sdavg)
print(sdavg)
print("The standard deviation of the planet's radius is approximately", '{0:1.3g}'.format(sd), "km or", '{0:1.3g}'.format(sd/6378), 
"Earth radii")
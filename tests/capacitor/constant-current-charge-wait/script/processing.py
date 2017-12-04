#!/usr/bin/python

import sys
import numpy as np
import csv
from numpy import genfromtxt
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

if(len(sys.argv) < 4):
    print("You must pass in a data file to perform this analysis")
    sys.exit(1)

capacity = float(sys.argv[2])
charge_curr = float(sys.argv[3])

#get the voltage data into a np array
voltage_data = genfromtxt(sys.argv[1],delimiter=',',skip_header=6)
volt = voltage_data[:,1]
time = voltage_data[:,5]

#find the point at which the source meter was turned off
point = np.argmax(volt)
stop_point = time[point]

#do some average of the data
b, a = butter(5, 0.1, btype='low', analog=False)
volt_filt = filtfilt(b, a, volt)

#replot the filtered values to get even spacing for derivation
time_interp = np.arange(0,time[-1],0.001)
volt_interp = np.interp(time_interp,time,volt_filt)
stop_point = int(stop_point*1000)

#plt.plot(time,volt_filt)
#plt.show()
#plt.plot(time_interp,volt_interp)
#plt.show()

#take the derivative of the data with respect to the time column
#deriv = np.gradient(volt_filt,voltage_data[:,5])
deriv = np.gradient(volt_interp, time_interp)
current = deriv*capacity
current[:stop_point] = current[:stop_point] - charge_curr
av = current
b, a = butter(5, 0.05, btype='low', analog=False)
av = filtfilt(b, a, current)
av = np.convolve(av,np.ones((1000,))/1000,mode='same')

#now for everything while I'm still supplying current, subtract 10uA
#mask = av > 0.000005
#av[mask] = av[mask] - 0.000010

plt.plot(time_interp,av)
plt.show()


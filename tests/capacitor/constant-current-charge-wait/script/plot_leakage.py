#!/usr/bin/env python3
import sys
import numpy as np
import csv
from numpy import genfromtxt
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
import argparse

#So that we can use ASAP smoothing
#it's not great but seems better than the butterworth filter
sys.path.insert(0, '../../../support/ASAP/python')
import ASAP

parser = argparse.ArgumentParser(description='Process and plot capacitor leakage data')
parser.add_argument('-d','--data_file',nargs='*',dest='data',action='append',help='Input data file from keithley source meter',required=True)
parser.add_argument('-c','--capacitance',nargs='*',dest='capacitance',action='append',type=float,help='Capacitance of the capacitor under test',required=True)
parser.add_argument('-i','--charge_current',nargs='*',dest='current',action='append',type=float,help='Charge current during the test',required=True)

def parse_test(filename, capacitance, charge_current):
    #get the voltage data into a np array
    voltage_data = genfromtxt(filename,delimiter=',',skip_header=6)

    #copy columns of the data out
    volt = voltage_data[:,1]
    time = voltage_data[:,5]

    #interpolate the signal - this will do better filtering and gradients
    time_interp = np.arange(0,time[-1],0.001)
    volt_interp = np.interp(time_interp,time,volt)


    #do a low pass filter of the data - dual sided butterworth filter will
    #not shift the data in time
    b, a = butter(5, 0.5, btype='low', analog=False)
    volt_filt = filtfilt(b, a, volt_interp)

    #After filtering, find the point at which the source meter was turned off
    stop_point = np.argmax(volt_filt)

    #take the derivative of the data with respect to the time column
    #I = C*(dv/dt)
    deriv = np.gradient(volt_filt, time_interp)
    current = deriv*capacitance

    #subtract the charge current to get the inefficiencies and leakage
    current[:stop_point] = current[:stop_point] - charge_current
    stop_time = time_interp[stop_point]

    #Smooth the current using ASAP - this seems to work better than
    #the butterworth filter
    current = ASAP.smooth(current,20000)
    time_interp_smooth = np.arange(0,time[-1],(time[-1]/np.size(current)))

    #moving average filter to make it look smoother
    current = np.convolve(current,np.ones((500,))/500,mode='valid')
    time_interp_smooth = np.convolve(time_interp_smooth,np.ones((500,))/500,mode='valid')

    #re-interpolate the voltage data so they are on the same time scale
    volt_filt = np.interp(time_interp_smooth,time_interp,volt_filt)

    #flip the leakage so that it's positive
    current = current*-1

    return time_interp_smooth,current,volt_filt,stop_time

#get the arguments
args = parser.parse_args()
if((len(args.data) != len(args.capacitance)) or (len(args.capacitance) != len(args.current))):
    print("You must have the same number of each argument!")
    sys.exit(1)

time = []
volt = []
curr = []
stop = []
for i in range(0,len(args.data)):
    t,c,v,s = parse_test(args.data[i][0],args.capacitance[i][0],args.current[i][0]);
    time.append(t)
    volt.append(v)
    curr.append(c)
    stop.append(s)

max_stop = max(stop)
for i in range(0,len(time)):
    plt.plot(time[i]+(max_stop-stop[i]),curr[i]*1e6,label=args.data[i][0].split('/')[-1].split('.')[0])

plt.ylabel("Capacitor charging losses + leakage (uA)")
plt.xlabel("Time (s)")
axes = plt.gca()
axes.set_ylim([0,4])
plt.axvline(x=max_stop-0.7,color='k',linewidth=0.5)
plt.text(max_stop-28,2.5,"Constant Current\nCharging")
plt.text(max_stop+8,2.5,"Zero Current")
plt.legend()
plt.title("Capacitor charge and stop losses")
plt.show()










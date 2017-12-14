#!/usr/bin/env python3
import sys
import numpy as np
import csv
from numpy import genfromtxt
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
import argparse


losses = np.array([437, 265, 173, 29, 1.1])
losses = losses*-1
losses = losses + 1440
losses = losses/1440
print(losses)

x = [40e-6, 200e-6, 20e-3, 0.1, 0.15]


plt.ylabel("Fraction of Available Energy Used")
plt.xlabel("Storage Capacity (mah)")
#axes = plt.gca()
#axes.set_ylim([0,4])
#plt.axvline(x=max_stop-0.7,color='k',linewidth=0.5)
#plt.text(max_stop-28,2.5,"Constant Current\nCharging")
#plt.text(max_stop+8,2.5,"Zero Current")
#plt.legend()
#plt.title("Capacitor charge and stop losses")
plt.plot(x, losses,marker='o')
plt.xscale('log')
plt.grid(True,which='both',ls='-.',alpha=0.5)
plt.show()
#









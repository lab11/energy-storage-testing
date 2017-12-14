#!/usr/bin/env python3
import sys
import numpy as np
import csv
from numpy import genfromtxt
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
from scipy.optimize import curve_fit
import argparse

thin_film_leak = 0.000000024
lithium_leak = 0.000004
thin_film_resistance = 100
lithium_resistance = 0.350
active_current = 0.005
active_thin_current = 0.0025
passive_current = 0.000005

t = np.arange(0., 1, 0.0000001);
lithium_losses = lithium_leak + (lithium_resistance*active_current**2)*t + (lithium_resistance*passive_current**2)*(1-t)
thin_film_losses = thin_film_leak + (thin_film_resistance*active_thin_current**2)*t + (thin_film_resistance*passive_current**2)*(1-t)


plt.plot(t,lithium_losses)
plt.plot(t,thin_film_losses)
plt.show()










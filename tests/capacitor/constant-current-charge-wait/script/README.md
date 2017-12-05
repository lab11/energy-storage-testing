Charge and wait
===============

The charge and wait test charges the capacitor at a constant current
until a set voltage, then it turns off current while the capacitor
leaks.
By taking the derivative of the voltage, we can get the current
going into and out of the capacitor during both phases of the test.
This allows us to calculate charging inefficiencies, and the leakage
after charging stops.

We generally find that most capacitors exhibit charging inefficiencies
from 5-25%, and that leakage current decays from the equivalent current
of these inefficiencies over the next 30-90s. Two processing scripts
help to show these numbers from the raw data.

## TSP Script
A script for the Keithley 2612B that performs the above test. It might
have to be modified for different size of capacitor or super
caps. Currently it works with ~100uF capacitors.

## Plot Leakage
The plot leakage script smooths the voltage readings, takes the derivative,
applies more filtering, then subtracts out the known current of the source
meter during charging. This allows us to plot charging inefficiencies + leakage
over time during the test. 

## Analyze Leakage
This script does similar processing to above but just prints out 
critical metrics such as the average leakage during charging and
the total coulombs absorbed during the leakage period (which is rather
constant across different testing times due to the exponential(ish) fall off
of leakage over time).

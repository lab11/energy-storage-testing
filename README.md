Energy Storage Characterization for Low-Power Sensor Nodes
==========================================================

For low-power sensor nodes, the type and size of energy storage defines the 
lifetime of the system. If the sensor node is energy harvesting, the energy
storage selection greatly impacts the efficiency of the harvester. Unfortunately
there is very little information about the myriad of energy storage options 
(including capacitors, super capacitors, and many types of batteries) that 
is useful for informing the system design of low-power nodes. Often
datasheets are incomplete, and even well written datasheets do not
characterize the charge/discharge of the energy stores in the order of
magnitude that they are charged and discharged on a low-power, energy harvesting
sensor node. Further, most battery research is focused on storing energy
for electric cars and the power grid, leading to a completely different
set of concerns and tests. 

The point of this repository is to serve as a landing page for information
on this topic. It will include information gleaned from papers, conversations
with other researchers, and our own testing methodologies, scripts and results.
If you have information to add, papers we should cite, tests that you think are useful, 
or thoughts
on the project _please_ submit a pull request or file an issue!

# Primary Cell (Non-Rechargeable) Batteries

We are concerned with the actual capacity and leakage of primary
cell batteries, and how discharge currents/patterns impact these two metrics. 

There is a great paper on how sensor node discharge patterns
impact capacity written by Feeney et al, which can be found [here](http://ieeexplore.ieee.org/document/6814721/).
The key idea is that high-pulsed discharge patterns may actually extend the
capacities of lithium primary cells beyond rated capacity, but we encourage
you to read the paper for more details. 

# Rechargeable Batteries

We are currently performing our own testing and compiling information
on both several types of lithium rechargeable batteries. Key metrics
are the charge/discharge efficiencies across several orders of magnitude,
of charge/discharge currents, static cell leakage current, and cell lifetime.
Most of these metrics are inter-dependent and also depend on other factors such
as state of charge.

Key ideas that we have learned so far, mainly from conversations with others,
is that cell lifetime has an inverse exponential relationship to depth of
discharge. Proper attribution/citations coming soon.

# Capacitors and Super Capacitors

We are currently performing our own testing and compiling information
on electrolytic, ceramic and tantalum capacitors as well as
several types of super capacitors. Key metrics are
charge/discharge efficiencies, absorption current, static leakage current, 
and capacitor lifetime. 

We generally find that the datasheet specifications for capacitor
leakage are very conservative compared to the observed static leakage current,
and are closer to the capacitors absorption current, which falls off exponentially.
This does not seem to be true for super capacitors, in which the observed
static leakage and absorption currents seem to exceed the datasheet rating.
More concrete testing methodology, scripts and results coming soon.

Our group has written briefly about the differences between tantalum
and ceramic capacitors for energy harvesting nodes in the past in
this [paper](https://web.eecs.umich.edu/~prabal/pubs/papers/yerva12grafting.pdf),
and we are confirming these results.

# sole
SOLE - Simulator Of Lifts and Elevators

SOLE is a Python based project which will simulate elevator operation within a given building including the creation or destruction of people within the simulation.

ROADMAP:
* Cross platform support (Windows and Linux). 
* Capacity for GUI display
* Vector graphics to allow for arbitrary scaling
* Open source audio for things like elevator dinging at floors
* Will allow for arbitrary building files
   * E.g. floors named unusually, exclusion of 13th floor
   * E.g. service elevators which have dedicated floor assignments (lobby to penthouse)
   * E.g. certain floors being residences vs businesses
* People will be extended to allow for ages, names, history
* Will provide for analysis of efficiencies, wait times, etc.
* Will allow for different queueing algorithms for the elevator itself
* Time system will be based on ticks, e.g. 1 second, with travel time between floors, speed of elevator door opening, etc. being based on real world times. The simulation will allow for arbitrary scaling of time, e.g. 20 ticks per real world second.
* Will allow for support of different types of elevators - e.g. historically slow freight elevators vs Star Trek turbolifts

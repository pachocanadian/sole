# SOLE - Simulator Of Lifts and Elevators

SOLE is a Python based project which will simulate elevator operation within a given building including the creation or destruction of people within the simulation.

## STANDARDS

* All code in repo to use Python Black (https://github.com/python/black)
* Cross platform support (Windows and Linux). 
* Vector graphics to allow for arbitrary scaling
* Open source audio for things like elevator dinging at floors

## Where are we going?

* Capacity for GUI display
* Will allow for arbitrary building files
   * E.g. floors named unusually, exclusion of 13th floor
   * E.g. service elevators which have dedicated floor assignments (lobby to penthouse)
   * E.g. certain floors being residences vs businesses
* People will be extended to allow for ages, names, history
   * E.g. want to provide an ActurialPerson class which will instantiate members according to a standard population distribution for height/weight/age/BMI
* Will provide for analysis of efficiencies, wait times, etc.
* Will allow for different queueing algorithms for the elevator itself
* Time system will be based on ticks, e.g. 1 second, with travel time between floors, speed of elevator door opening, etc. being based on real world times. The simulation will allow for arbitrary scaling of time, e.g. 20 ticks per real world second.
* Will allow for support of different types of elevators - e.g. historically slow freight elevators vs Star Trek turbolifts

## SIMULATOR FLOW

* Presently, there will be one and only one simulator.
* The simulator will host one and only one building.
* A building will be made up of at least two floors. Each floor will have a label. Typically labelled like ['Lobby', '1', 2', '3'].
* A building will be made up of at least one elevator. The elevator will connect two or more floors. Typically every elevator in a building will connect every floor, although there may exceptions to this. We impose the restriction that all floors must be connected - that is, that someone on any floor must be able to reach all other floors through some combination of elevators.
* The simulator will create people as it sees fit. In the typical case, people will be created on any of the floors with a destination of any other floor. That is, random start floor and random destination floor. Later simulators might purposefully create people in residential floors and send them to commercial floors or things like this.
* Upon creation people will move from their starting floor to their destination floor. Upon reaching their destination floor, in the initial case, they will be destroyed.
* Initially the elevator will impose no restrictions on people entering the elevator. However, we may allow for cases where the elevator imposes restrictions on # of bodies, overall weight, volume of space, etc.


## TEAM MEMBERS

Christian Pearson <christian.pearson@stemist.ca>
* Linux 4.15.0-51-generic #55-Ubuntu SMP x86_64 x86_64 x86_64 GNU/Linux
* IDE: Vim, VSCode

Mike Carr <mcarr@pachogrande.com>
* Windows 10 x64, Windows 7 x64
* IDE: PyDev

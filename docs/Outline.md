## Basic Elevator Behaviour Outline

A SOLE elevator behaves as follows:

A person on floor x requests an elevator so they can move to floor y. 
Receiving a request causes an elevator to start moving to floor x to pick up the person.
The elevator reaches floor x and stops, allowing the person to get onto it.
The elevator moves the person to floor y and stops, allowing the person to get off.

Additional requests are ignored until the elevator completes the first request it receieves. 

### Basic Elevator Example Scenario

Assuming one elevator idle at Lobby:

1) Person A at floor 2 requests an elevator to move them to floor 1.
2) Elevator at Lobby receives request and begins to move to floor 2
3) Elevator reaches floor 2, stops, and picks up person.
4) Person B requests an elevator to move Person B to Lobby [Request is ignored].
5) Elevator (person A onboard) begins moving to floor 1.
6) Elevator (person A onboard) reaches floor 1 and stops, letting person A off.
7) Elevator is now idle and can repeat step 1 for a new request.


### Basic Elevator Timeline and Ruleset 
-------------------
* Boarding an elevator takes 5 seconds.
* Leaving an elevator takes 5 seconds.
* Acceleration is instantaneous
* Elevator base velocity units are +1 m/s, 0 m/s or -1 m/s.
* People can only enter elevator once elevator is in "Doors Open" state.

Time (sec)   | Velocity	 | Elevation | Elevator State           | Current Floor | People aboard  | Person A State
------------ | --------  | --------- | --------------------     | ------------- | -------------  | -----------
0            |  +0 m / s |  0 m      | Idle                     |  Lobby        |  None	        | Idle
1	     |  +1 m / s |  1 m      | Moving		        |  None         |  None	        | Requesting
2            |  +1 m / s |  2 m      | Moving		        |  None         |  None	        | Requesting
3            |  +1 m / s |  3 m      | Moving		        |  None         |  None	        | Requesting
4            |  +1 m / s |  4 m      | Moving	                |  None         |  None	        | Requesting
5            |  0 m / s  |  5 m      | Doors Opening            |  Floor 2      |  None	        | Entering
6-10         |  0 m / s  |  5 m      | Doors Opening            |  Floor 2      |  None		| Entering
11-15        |  0 m / s  |  5 m      | Doors Open               |  Floor 2      |  None 	| Entering
16-20        |  0 m / s  |  5 m      | Loading		        |  Floor 2      |  None		| Entering
21-25        |  0 m / s  |  5 m      | Doors Closing            |  Floor 2      |  Person A	| Aboard
26           |  0 m / s  |  5 m      | Doors Closed	        |  Floor 2      |  Person A	| Aboard 
27           |  -1 m / s |  4 m      | Moving                   |  None         |  Person A	| Aboard
28	     |  -1 m / s |  3 m      | Moving	                |  None	        |  Person A	| Aboard
29-33        |  0 m / s  |  2.5 m    | Doors Opening            |  Floor 1      |  Person A	| Aboard
34	     |  0 m / s  |  2.5 m    | Doors Open		|  Floor 1	|  Person A	| Aboard	
35-39	     |  0 m / s  |  2.5 m    | Unloading		|  Floor 1      |  Person A     | Leaving
40	     |  0 m / s	 |  2.5 m    | Idle			|  Floor 1	|  None		| Idle



## Building Layout

Floor height: 2.5 m / floor

Elevation (m)	|	Floor		|	
---------------	|	-------		|
10		|	Floor 4		|
7.5		|	Floor 3 	|	
5		|	Floor 2 	|
2.5		|	Floor 1		|
0		|	Lobby		|


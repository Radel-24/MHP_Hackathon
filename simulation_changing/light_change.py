
# argv[1] gives port on where to connect to sumo simulation

import os
import sys
import traci


traci.init(int(sys.argv[1]))
traci.setOrder(int(sys.argv[2]))

step = 0
while traci.simulation.getMinExpectedNumber() > 0:
	if step == 10:
		traci.trafficlight.setRedYellowGreenState("0", "yyyy")
	step += 1
	traci.simulationStep()

traci.close()

# argv[1] gives port on where to connect to sumo simulation

import os
import sys
import traci


traci.init(int(sys.argv[1]))
traci.setOrder(int(sys.argv[2]))


lights = traci.trafficlight.getIDList()
while traci.simulation.getMinExpectedNumber() > 0:
	# for light in lights:
	# 	linkIds = traci.trafficlight.getControlledLinks(light)
	# 	for link in linkIds:
	# 		print("lights changed" + linkId)
	# 		blockingVeh = traci.trafficlight.getBlockingVehicles(light, 1)
	# 		if (len(blockingVeh) > 2):
	# 			# traci.trafficlight.setPhaseDuration(light, 1)
	# 			traci.trafficlight.setRedYellowGreenState("rrrr")

	traci.simulationStep()

traci.close()
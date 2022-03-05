
# argv[1] gives port on where to connect to sumo simulation

import os
import sys
import traci

if 'SUMO_HOME' in os.environ:
	tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
	sys.path.append(tools)
else:
	sys.exit("environment variable 'SUMO_HOME' not set")

sumoBinary = checkBinary('sumo-gui') # change to 'sumo' when running without gui
sumoCmd = [sumoBinary, "-c", sys.argv[1]]

traci.setOrder(2)

traci.start(sumoCmd)
step = 0
#while step < 1000:
while traci.simulation.getMinExpectedNumber() > 0:
	traci.simulationStep()
	if traci.inductionloop.getLastStepVehicleNumber("0") > 0:
		traci.trafficlight.setRedYellowGreenStat("0", "GrGr")
	#step += 1

traci.close()
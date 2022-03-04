
# argv[1] is name of sumo config file

import os
import sys
import traci
import traci.constants as tc
from sumolib.miscutils import getFreeSocketPort

if 'SUMO_HOME' in os.environ:
	tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
	sys.path.append(tools)
else:
	sys.exit("environment variable 'SUMO_HOME' not set")

freePort = sumolib.miscutils.getFreeSocketPort()

sumoBinary = checkBinary('sumo-gui') # change to 'sumo' when running without gui
sumoCmd = [sumoBinary, "-c", sys.argv[1], "--num-clients", "1"], port=freePort

traci.start(sumoCmd)
traci.setOrder(1)

vehID = 'left_204'

traci.vehicle.subscribe(vehID, (tc.VAR_ROAD_ID, tc.VAR_LANEPOSITION))
print(traci.vehicle.getSubscriptionResults(vehID))

while traci.simulation.getMinExpectedNumber() > 0:
	traci.simulationStep()
	print(traci.vehicle.getSubscriptionResults(vehID))




traci.close()
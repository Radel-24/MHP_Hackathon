
# argv[1] is name of sumo config file

import csv
import time
import os
import sys
import traci
import traci.constants as tc
import sumolib
import sumolib.miscutils
from sumolib.miscutils import getFreeSocketPort
from sumolib import checkBinary


if 'SUMO_HOME' in os.environ:
	tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
	sys.path.append(tools)
else:
	sys.exit("environment variable 'SUMO_HOME' not set")

freePort = sumolib.miscutils.getFreeSocketPort()

sumoBinary = checkBinary('sumo-gui') # change to 'sumo' when running without gui
traci.start([sumoBinary, "-c", sys.argv[1], "--num-clients", "1", "--emission-output", "emi.xml"], port=freePort)

# traci.start(sumoCmd)
traci.setOrder(1)

vehID = 'left_0'

traci.vehicle.subscribe(vehID, (tc.VAR_ROAD_ID, tc.VAR_LANEPOSITION))
print(traci.vehicle.getSubscriptionResults(vehID))

fieldnames = ["timestamp", "CO2", "fuel", "noise", "standing_cars"]

with open('data.csv', 'w') as csv_file:
	csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
	csv_writer.writeheader()


i = 0
while traci.simulation.getMinExpectedNumber() > 0:
	traci.simulationStep()
	#print("step:" + str(i))
	i += 1
	#print(traci.vehicle.getSubscriptionResults(vehID))
	#print("CO2: " + str(traci.vehicle.getCO2Emission(vehID)))
	info = {
		"timestamp": i,
		"CO2": traci.vehicle.getCO2Emission(vehID),
		"fuel": traci.vehicle.getFuelConsumption(vehID),
		"noise": traci.vehicle.getNoiseEmission(vehID),
		"standing_cars": 42
	}

	csv_writer.writerow(info)
	#print(x_value, total_1, total_2, total_3, total_4)

	time.sleep(1)


	 #print(traci.vehicle.getSubscriptionResults(vehID))
#for i in range(3):
#	traci.simulationStep()
#	print("step:" + str(i))
#	print(traci.vehicle.getSubscriptionResults(vehID))
#	print("CO2: " + str(traci.vehicle.getCO2Emission(vehID)))



traci.close()
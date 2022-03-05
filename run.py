import subprocess
import os
import sys
import sumolib
import traci
from sumolib import checkBinary
from sumolib.miscutils import getFreeSocketPort

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


subprocess.call(["python", "data_analyze/get_live_data.py", str(freePort), str(2)])
# subprocess.call("./sumoVisualizer/graph_visualizer.py", 3)

while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()

traci.close()
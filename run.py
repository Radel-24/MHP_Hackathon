import subprocess

subprocess.call(["data_analyze/get_live_data.py", "../../sumo/tests/complex/tutorial/traci_tls/data/cross.sumocfg"])
subprocess.call("./sumoVisualizer/graph_visualizer.py")
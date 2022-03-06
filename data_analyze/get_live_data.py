
# argv[1] is name of sumo config file

import csv
import sys
import traci
import traci.constants as tc
import sumolib
import sumolib.miscutils
from sumolib.miscutils import getFreeSocketPort
from sumolib import checkBinary
from decibel import dbsum


traci.init(int(sys.argv[1]))
traci.setOrder(int(sys.argv[2]))

fieldnames = ["timestamp", "car_amount", "CO2", "fuel", "noise", "standing_cars"]

with open('./sumoVisualizer/data.csv', 'w') as csv_file:
	csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
	csv_writer.writeheader()

i = 0
while traci.simulation.getMinExpectedNumber() > 0:
	i += 1

	vehicles = traci.vehicle.getIDList()
	total_co2 = 0
	total_fuel = 0
	total_noise = 0
	standing_cars = 0
	carAmount = len(vehicles)
	x = 0
	for vehicle in vehicles:
		if (traci.vehicle.getSpeed(vehicle) == 0): # is aiming start/stop automation
			standing_cars += 1
			continue
		total_co2 += traci.vehicle.getCO2Emission(vehicle)
		total_fuel += traci.vehicle.getFuelConsumption(vehicle)
		total_noise = dbsum([total_noise, float(traci.vehicle.getNoiseEmission(vehicle))])
		x += 1
		if x == 200:
			break

	with open('./sumoVisualizer/data.csv', 'a') as csv_file:
		csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
		info = {
			"timestamp": i,
			"car_amount": carAmount,
			"CO2": total_co2,
			"fuel": total_fuel,
			"noise": total_noise,
			"standing_cars": standing_cars
		}
		csv_writer.writerow(info)

	traci.simulationStep()

traci.close()
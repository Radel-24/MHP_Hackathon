
# this script analyzes the emission output file of the sumo simulation

# argv[1] gives the name of the emmisions file

from telnetlib import VT3270REGIME
from bs4 import BeautifulSoup
import sys

from decibel import dbsum

total_co2 = 0
total_co = 0
total_nox = 0
total_fuel = 0
total_noise = 0

file = sys.argv[1]

with open(file, 'r') as f:
	data = f.read()

vehicle = BeautifulSoup(data, 'xml')

vehicles = vehicle.find_all('vehicle')
for vehicle in vehicles:
	total_co2 += float(vehicle.get('CO2'))
	total_co += float(vehicle.get('CO'))
	total_nox += float(vehicle.get('NOx'))
	total_fuel += float(vehicle.get('fuel'))
	total_noise = dbsum([float(vehicle.get('noise')), total_noise])

print("Total CO2: " + str(round(total_co2, 2)) + " mg")
print("Total CO: " + str(round(total_co, 2)) + " mg")
print("Total NOx: " + str(round(total_nox, 2)) + " mg")
print("Total fuel: " + str(round(total_fuel, 2)) + " ml")
print("Total noise: " + str(round(total_noise, 2)) + " db")
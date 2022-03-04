from bs4 import BeautifulSoup
import sys

total_co2 = 0
total_co = 0
total_nox = 0
total_fuel = 0

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

print("Total CO2: " + str(round(total_co2, 2)) + " mg")
print("Total CO: " + str(round(total_co, 2)) + " mg")
print("Total NOx: " + str(round(total_nox, 2)) + " mg")
print("Total fuel: " + str(round(total_fuel, 2)) + " ml")
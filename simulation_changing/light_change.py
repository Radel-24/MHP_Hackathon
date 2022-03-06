
# argv[1] gives port on where to connect to sumo simulation

import os
import sys
import traci


traci.init(int(sys.argv[1]))
traci.setOrder(int(sys.argv[2]))


def greenCorridor(): # TODO imporve algorithm for setting only certanin lights green
	traci.trafficlight.setPhase("cluster_30340989_7196556440", 0)
	traci.trafficlight.setPhase("GS_8075882156", 2)
	traci.trafficlight.setPhase("cluster_30340990_7196556438", 2)
	traci.trafficlight.setPhase("cluster_268840038_7196556436_8398087652", 0)
	traci.trafficlight.setPhase("cluster_30340992_7196556434_8398087655", 0)
	traci.trafficlight.setPhase("cluster_30340993_7196556433_8398087657", 0)
	traci.trafficlight.setPhase("cluster_30340996_7196556428_8066827010", 0)
	traci.trafficlight.setPhase("cluster_30340997_7196556427_8075882162", 2)
	traci.trafficlight.setPhase("cluster_30340998_7196556426_8075882160", 0)
	traci.trafficlight.setPhase("cluster_30341002_7196556422_8075848379", 2)
	traci.trafficlight.setPhase("cluster_30340991_7196556435_8398087653", 0)
	traci.trafficlight.setPhase("cluster_268840624_5201275459_8398087658", 0)
	traci.trafficlight.setPhase("cluster_30340994_5201275461_7196556431_8075652029_8398087659_8398087660", 4)
	traci.trafficlight.setPhase("cluster_268840695_5201275464_7196556430_8066827008", 0)
	traci.trafficlight.setPhase("cluster_30340995_5201275465_7196556429_8066827012_8066827013_8066827015_8066827016_8066827017", 6)
	traci.trafficlight.setPhase("cluster_274184902_8066827011", 2)
	traci.trafficlight.setPhase("cluster_274184624_8075882161", 0)
	traci.trafficlight.setPhase("268838946", 0)
	traci.trafficlight.setPhase("cluster_268842694_7196556439", 0)
	traci.trafficlight.setPhase("cluster_30340992_7196556434_8398087655", 0)
	traci.trafficlight.setPhase("cluster_268840707_8398087656", 0)
	traci.trafficlight.setPhase("cluster_5840582514_8075848381", 2)
	traci.trafficlight.setPhase("cluster_30341001_7196556423_8075848383", 2)
	traci.trafficlight.setPhase("30340999", 4)
	
	
lights = traci.trafficlight.getIDList()
step = 0
while traci.simulation.getMinExpectedNumber() > 0:
	for light in lights:
		vehicles = traci.trafficlight.getRivalVehicles(light, 0)
	if (step % 300) < 100:
		greenCorridor()
	step += 1
	for vehicle in vehicles:
		state = traci.trafficlight.getPhase()

	traci.simulationStep()

traci.close()
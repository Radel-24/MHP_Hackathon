import imp
import random
from itertools import count
import pandas as pd
import matplotlib.style
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('dark_background')

# create subplots (multiple graphs)
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)

def animate(i):
	# read in data from csv file
	data = pd.read_csv('sumoVisualizer/data.csv')
	x = data['timestamp']
	y1 = data['CO2']
	y2 = data['fuel']
	y3 = data['noise']
	y4 = data['standing_cars']

	ax1.cla()
	ax2.cla()
	ax3.cla()
	ax4.cla()

	ax1.plot(x, y1, label='CO2', color='#36c5f0')
	ax2.plot(x, y2, label='fuel', color='#2eb67d')
	ax3.plot(x, y3, label='noise', color='#e01e5a')
	ax4.plot(x, y4, label='standing cars', color='#ecb22e')

	# ax1.legend(loc='upper left')
	ax1.set_title('CO2 (mg / s)')
	ax1.set_xlim(left=120)

	# ax2.legend(loc='upper left')
	ax2.set_title('fuel (ml / s)')
	ax2.set_xlim(left=120)

	# ax3.legend(loc='upper left')
	ax3.set_title('noise (db)')
	ax3.set_xlabel('timestamp')
	ax3.set_xlim(left=120)

	# ax4.legend(loc='upper left')
	ax4.set_title('standing cars')
	ax4.set_xlabel('timestamp')
	ax4.set_xlim(left=120)

	plt.tight_layout(pad=3.0)

ani = FuncAnimation(plt.gcf(), animate, interval=500) # gcf == get current figure

plt.tight_layout(pad=3.0)
plt.show()

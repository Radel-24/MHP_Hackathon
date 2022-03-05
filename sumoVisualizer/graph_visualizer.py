import imp
import random
from itertools import count
import pandas as pd
import matplotlib.style
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('seaborn')

fig1, (ax1, ax2) = plt.subplots(nrows=2, ncols=1) # create subplots (multiple graphs), adding sharex=True helps to make cleaner
# fig2, ax3 = plt.subplots()

def animate(i):
	# read in data from csv file
	data = pd.read_csv('data.csv')
	x = data['timestamp']
	y1 = data['CO2']
	y2 = data['fuel']
	# y3 = data['traffic_amount_3']
	# y4 = data['traffic_amount_4']

	ax1.cla()
	ax2.cla()
	# ax3.cla()

	# each plot is a line
	ax1.plot(x, y1, label='CO2')
	# ax1.plot(x, y2, label='Street 2')
	ax2.plot(x, y2, label='fuel', color='#ff0000')
	# ax3.plot(x, y4, label='Street 4')

	ax1.legend(loc='upper left')
	ax1.set_title('CO2')
	ax1.set_ylabel('CO2')

	ax2.legend(loc='upper left')
	ax2.set_title('fuel')
	ax2.set_xlabel('time')
	ax2.set_ylabel('fuel')

	# ax3.legend(loc='upper left')
	# ax3.set_title('Street traffic data3')
	# ax3.set_xlabel('time3')
	# ax3.set_ylabel('cars on street3')

	plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=1000) # gcf == get current figure

plt.tight_layout()
plt.show()













# plt.style.use('seaborn')

# def animate(i):
# 	# read in data from csv file
# 	data = pd.read_csv('data.csv')
# 	x = data['x_value']
# 	y1 = data['traffic_amount_1']
# 	y2 = data['traffic_amount_2']
# 	y3 = data['traffic_amount_3']

# 	plt.cla()

# 	# each plot is a line
# 	plt.plot(x, y1, label='Street 1')
# 	plt.plot(x, y2, label='Street 2')
# 	plt.plot(x, y3, label='Street 3')

# 	plt.legend(loc='upper left')
# 	plt.title('Street traffic data')
# 	plt.xlabel('time')
# 	plt.ylabel('cars on street')

# 	plt.tight_layout()

# ani = FuncAnimation(plt.gcf(), animate, interval=1000) # gcf == get current figure

# plt.tight_layout()
# plt.show()
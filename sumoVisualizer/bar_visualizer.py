from matplotlib import pyplot as plt
import numpy as np

plt.style.use('dark_background')

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)

bar_width = 0.4

our_CO2 =  218401811.27 / (1000 * 1000)
our_standing = 813 / 60

original_CO2 = 461864270.67 /  (1000 * 1000)
original_standing = 1946 / 60

ax1.bar(1 + (bar_width / 2), our_CO2, width=bar_width, color="#77dd77", label="IntelliTraffic")
ax1.bar(1 - (bar_width / 2), original_CO2, width=bar_width, color="#e15241", label="Regular")

ax2.bar(1 + (bar_width / 2), our_standing, width=bar_width, color="#77dd77", label="IntelliTraffic")
ax2.bar(1 - (bar_width / 2), original_standing, width=bar_width, color="#e15241", label="Regular")


ax1.legend(loc='best')
ax2.legend(loc='best')


# show categories instead of indexes on x-axis
ax1.set_xticks(ticks=[1], labels=["CO2 (kg)"])
ax2.set_xticks(ticks=[1], labels=["travel time for 300 cars (min)"])


plt.tight_layout(pad=3.0)
plt.show()
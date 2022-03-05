from matplotlib import pyplot as plt
import numpy as np

plt.style.use('dark_background')

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)

bar_width = 0.4 # changeable

our_CO2 = 50000
our_fuel = 12
our_noise = 55
our_standing = 280

original_CO2 = 60000
original_fuel = 14
original_noise = 60
original_standing = 320


ax1.bar(1 - (bar_width / 2), our_CO2, width=bar_width, color="#444444", label="our")
ax1.bar(1 + (bar_width / 2), original_CO2, width=bar_width, color="#008fd5", label="original")

ax2.bar(1 - (bar_width / 2), our_fuel, width=bar_width, color="#444444", label="our")
ax2.bar(1 + (bar_width / 2), original_fuel, width=bar_width, color="#008fd5", label="original")

ax3.bar(1 - (bar_width / 2), our_noise, width=bar_width, color="#444444", label="our")
ax3.bar(1 + (bar_width / 2), original_noise, width=bar_width, color="#008fd5", label="original")

ax4.bar(1 - (bar_width / 2), our_standing, width=bar_width, color="#444444", label="our")
ax4.bar(1 + (bar_width / 2), original_standing, width=bar_width, color="#008fd5", label="original")


ax1.legend('upper right')
ax2.legend('upper right')
ax3.legend('upper right')
ax4.legend('upper right')


# show categories instead of indexes on x-axis
ax1.set_xticks(ticks=[1], labels=["CO2"])
ax2.set_xticks(ticks=[1], labels=["fuel"])
ax3.set_xticks(ticks=[1], labels=["noise"])
ax4.set_xticks(ticks=[1], labels=["standing cars"])


plt.tight_layout()
plt.show()
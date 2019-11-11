from random import choice
from random import random
import matplotlib.pyplot as plt

x_axis = range(100)
data = []


value = 0

normal = 0.1
normal_percentage = 0.9
extreme = 5 
extreme_percentage = 0.1
n = 100

normal_change = [normal, -normal]
extreme_change = [extreme, -extreme]


dat = 0
for i in range(100):
	
	value = value + choice(normal_change)
	if(random()<0.94):
		dat = value
	else:
		dat = value + choice(extreme_change)

	data.append(dat)

plt.plot( x_axis, data )
plt.axis([0, 100, -10, 10])
plt.ylabel("data")
plt.xlabel("x")
plt.show()

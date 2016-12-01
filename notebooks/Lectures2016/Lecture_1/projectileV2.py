import math
import pylab as plt
import numpy as np

h_start = float(raw_input('Input starting height (m): '))
v = float(raw_input('Input starting velocity (m/s): '))

theta_array = np.linspace(0,3.141519/2,11)

for theta in theta_array:
	g = 9.81
	vx = v*math.cos(theta)
	vy = v*math.sin(theta)

	R = vx/g * (vy + math.sqrt( vy*vy + 2*g*h_start ) )
	t = R/(vx)

	t_array = np.linspace(0,t,100)
	R_array = np.linspace(0,R,100)
	y_array = h_start + R_array*math.tan(theta) - g*R_array*R_array/(2*vx*vx)

	plt.plot(R_array,y_array)


plt.annotate('Starting Velocity: ' + str(v) + ' (m/s)' , xy=(0.75, 0.9), xycoords='axes fraction', fontsize=16,
                horizontalalignment='center', verticalalignment='bottom')
plt.annotate('Starting Height: ' + str(h_start) + ' (m)' , xy=(0.75, 0.845), xycoords='axes fraction', fontsize=16,
                horizontalalignment='center', verticalalignment='bottom')
plt.xlabel("Range (m)")
plt.ylabel("Height (m)")
plt.title("Projectile trajectories for varying launch angles")
plt.ylim(0,)
plt.show()
plt.savefig("test.png")

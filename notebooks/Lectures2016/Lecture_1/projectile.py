import math

h_start = float(raw_input('Input starting height (m): '))
theta = float(raw_input('Input starting angle (degrees): '))*3.14159/180
v = float(raw_input('Input starting velocity (m/s): '))

g = 9.81
vx = v*math.cos(theta)
vy = v*math.sin(theta)

R = vx/g * (vy + math.sqrt( vy*vy + 2*g*h_start ) )
time = R/(vx)

print "Range: " + str(round(R,2)) + " m"
print "Time of flight: " + str(round(time,2)) + " s"

t = 0.0
while t < time:
	print "Time: " + str(round(t,2)) + " s, Range : " + str(round(t*vx,2)) + " m"
	t += 1
'''
Authors: Sergio Mundo and Laura Lenkic

Date: 11/14/2017

Filename: prob1.py

Testing integrators on two-body problem and comparing RK4 integrator to leapfrog integrator.
'''

import numpy as np
import integrators as i
import matplotlib.pyplot as plt

# Masses*G, eccentricities, time steps, and output frequency for the plots.
Gm = [1, 1]
e = [0.5, 0.9]
h = [0.05, 0.003]
s = [4, 50]

# Do everything twice, once for e = 0.5 and once for e = 0.9.
for j in range(0,len(e)):
	# Calculate the period, number of steps, and relative speed of the two particles.
	P = np.pi*np.sqrt(2./(1+e[j])**3)
	ns = int(100*P/h[j])
	v = np.sqrt(2*(1-e[j]))

	# Set the initial conditions, and the list of functions to pass to integrators.
	ics = [-0.5, 0.5, 0, 0, 0, 0, 0, 0, -0.5*v, 0.5*v, 0, 0]
	functions = [i.vx]*2 + [i.vy]*2 + [i.vz]*2 + [i.vx_dot]*2 + [i.vy_dot]*2 + [i.vz_dot]*2

	# Set range time range for integrations
	time = [0,100*P,100*P/ns]

	# Call the RK4 and leapfrog integrators, and store the solutions.
	solutions_rk = i.rk4(functions,ics,Gm,time,0.)
	solutions_lf = i.leapfrog(functions,ics,Gm,time,0.)

	# Plot particle orbits from RK4 integrator.
	plt.plot(solutions_rk[0][0::s[j]],solutions_rk[2][0::s[j]],'.')
	plt.plot(solutions_rk[1][0::s[j]],solutions_rk[3][0::s[j]],'.')
	plt.ylim([-0.6,0.6])
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('Orbits of Two Particles from RK4 Integrator with e = '+str(e[j]))
	plt.savefig('Particle_Orbits_RK4'+str(e[j])+'.png',dpi=300)
	plt.show()

	# Calculate v dot r and r for the phase diagram, and then plot the phase diagram for the RK4 integrator.
	r = np.sqrt((solutions_rk[0]-solutions_rk[1])**2 + (solutions_rk[2]-solutions_rk[3])**2 + (solutions_rk[4]-solutions_rk[5])**2)
	vr1 = ((solutions_rk[6]-solutions_rk[7])*(solutions_rk[0]-solutions_rk[1]) + (solutions_rk[8]-solutions_rk[9])*(solutions_rk[2]-solutions_rk[3]) + (solutions_rk[10]-solutions_rk[11])*(solutions_rk[4]-solutions_rk[5]))/r

	plt.plot(r[0::s[j]],vr1[0::s[j]],'.')
	plt.xlabel(r'$r$')
	plt.ylabel(r'$v_{r}$')
	plt.title('Phase Diagram for Two Body Problem from RK4 Integrator with e = '+str(e[j]))
	plt.savefig('Phase_Diagram_RK4'+str(e[j])+'.png',dpi=300)
	plt.show()

	# Calculate the fractional energy change at each time step then plot the results as a function of time for the RK4 integrator.
	v1 = solutions_rk[6]**2 + solutions_rk[8]**2 + solutions_rk[10]**2
	v2 = solutions_rk[7]**2 + solutions_rk[9]**2 + solutions_rk[11]**2
	ET = 0.5*v1 + 0.5*v2 - 1./r
	E = (ET - ET[0])/abs(ET[0])
	time = np.arange(0,100*P,100*P/ns)

	plt.plot(time[0::s[j]],E[0::s[j]])
	plt.xlabel('Time')
	plt.ylabel('Fractional Change in Total Energy')
	plt.title('Fractional Change in Total Energy from RK4 Integrator with e = '+str(e[j]))
	plt.savefig('Frac_Energy_Change_RK4'+str(e[j])+'.png',dpi=300)
	plt.clf()

	# Do the same calculations and make the same plots as above but now for the leapfrog integrator.
	plt.plot(solutions_lf[0][0::s[j]],solutions_lf[2][0::s[j]],'.')
	plt.plot(solutions_lf[1][0::s[j]],solutions_lf[3][0::s[j]],'.')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('Orbits of Two Particles from Leapfrog Integrator with e = '+str(e[j]))
	plt.savefig('Particle_Orbits_LF'+str(e[j])+'.png',dpi=300)
	plt.clf()

	r = np.sqrt((solutions_lf[0]-solutions_lf[1])**2 + (solutions_lf[2]-solutions_lf[3])**2 + (solutions_lf[4]-solutions_lf[5])**2)
	vr1 = ((solutions_lf[6]-solutions_lf[7])*(solutions_lf[0]-solutions_lf[1]) + (solutions_lf[8]-solutions_lf[9])*(solutions_lf[2]-solutions_lf[3]) + (solutions_lf[10]-solutions_lf[11])*(solutions_lf[4]-solutions_lf[5]))/r

	plt.plot(r[0::s[j]],vr1[0::s[j]],'.')
	plt.xlabel(r'$r$')
	plt.ylabel(r'$v_{r}$')
	plt.title('Phase Diagram for Two Body Problem from Leapfrog Integrator with e = '+str(e[j]))
	plt.savefig('Phase_Diagram_LF'+str(e[j])+'.png',dpi=300)
	plt.clf()

	v1 = solutions_lf[6]**2 + solutions_lf[8]**2 + solutions_lf[10]**2
	v2 = solutions_lf[7]**2 + solutions_lf[9]**2 + solutions_lf[11]**2
	ET = 0.5*v1 + 0.5*v2 - 1./r
	E = (ET - ET[0])/abs(ET[0])
	time = np.arange(0,100*P,100*P/ns)
	
	plt.plot(time[0::s[j]],E[0::s[j]])
	plt.xlabel('Time')
	plt.ylabel('Fractional Change in Total Energy')
	plt.title('Fractional Change in Total Energy from Leapfrog Integrator with e = '+str(e[j]))
	plt.savefig('Frac_Energy_Change_LF'+str(e[j])+'.png',dpi=300)
	plt.clf()

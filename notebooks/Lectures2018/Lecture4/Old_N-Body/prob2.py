'''
Authors: Sergio Mundo and Laura Lenkic

Date: 11/21/2017

Filename: prob2.py

Code for the N-body simulation.
'''

import integrators as i
import numpy as np
import matplotlib.pyplot as plt
import sys

def nbody(integrator,softening,timestep,numsteps,outputfreq,filename):
	"""
	Does the N-body simulation of 250 particles orbiting a central star, while a secondary, low-mass star flies by, through the system.

	param integrator: integrator to be used for calculation, either RK4 of LF2 (fourth-order runge-kutta or second-order leapfrog)
	param softening: softening parameter
	param timestep: size of the timestep to use in the integration
	param numsteps: number of time steps to calculate in solution
	param outputfreq: desired output frequency
	param filename: file that contains the initial conditions for the particles
	"""
	# Check that the initial conditions file exists.
	try:
		icsfile = open(filename,'r')
	except (IOError):
		print "Invalid"
		sys.exit()
	
	# Set the time for the intgration.
	tmax = timestep*numsteps
	time = [0,tmax,timestep]

	# Read in the initial conditions from the initial conditions file.
	mass = []
	x = []
	y = []
	z = []
	xdot = []
	ydot = []
	zdot = []
	for line in icsfile:
		line = line.strip()
		columns = line.split()
		mass.append(float(columns[0]))
		x.append(float(columns[1]))
		y.append(float(columns[2]))
		z.append(float(columns[3]))
		xdot.append(float(columns[4]))
		ydot.append(float(columns[5]))
		zdot.append(float(columns[6]))

	# Determine the number of particles
	N = len(mass)

	# Create the list of initial conditions and functions to pass to the integrator.
	ics = x + y + z + xdot + ydot + zdot
	functions = [i.vx]*N + [i.vy]*N + [i.vz]*N + [i.vx_dot]*N + [i.vy_dot]*N + [i.vz_dot]*N

	# Call the appropriate integrator based on the user's input into the function.
	if (integrator == 'RK4'):
		solutions = i.rk4(functions,ics,mass,time,softening)
	elif (integrator == 'LF2'):
		solutions = i.leapfrog(functions,ics,mass,time,softening)
	else:
		print "You did not enter a valid integrator. Options are RK4 of LF2."
		sys.exit()

	# Calculate the kinetic energy of each particle.
	E_kin = []
	potential_E = []
	for k in range(3*N,4*N):
		mass_particle = mass[k-3*N]
		v2_particle = solutions[k]**2 + solutions[k+N]**2 + solutions[k+N*2]**2
		K = 0.5*mass_particle*v2_particle
		E_kin.append(K)
    
	# Calculate the potential energy of each particle.
	for p in range(N):
		for q in range(p+1,N):
			r = np.sqrt((solutions[p]-solutions[q])**2+(solutions[p+N]-solutions[q+N])**2+(solutions[p+N*2]-solutions[q+N*2])**2)
			potE = mass[p]*mass[q]/r
			potential_E.append(potE)        

	# Calculate the total energy, the fractional energy, and then plot the results.
	E = sum(E_kin) - sum(potential_E)
	E_frac = (E-E[0])/np.abs(E[0])
	t = np.arange(0, tmax, timestep)
	plt.plot(t,E_frac)
	plt.xlabel('$t$')
	plt.ylabel('$\mathrm{Fractional \ Energy \ Change}$')
	if (integrator == 'LF2'):
		plt.title('$\mathrm{Fractional \ Energy \ Change \ for \ Leapfrog (h = 0.0543)}$')
	else:
		plt.title('$\mathrm{Fractional \ Energy \ Change \ for \ RK4 (h = 0.0543)}$')
	plt.savefig('Energy_'+integrator+'.png',dpi=300)

	# Plot the positions of every particle in the xy-plane, at each time step, and save each "frame", which will be used to make an animation of the evolution of the system.
	cntr = 0
	for j in range(0,len(solutions[0]),outputfreq):
		fig = plt.figure()
		ax = fig.add_subplot(111)
		ax.set_xlim(-6,6)
		ax.set_ylim(-6,6)
		for k in range(0,N):
			ax.scatter(solutions[k][j], solutions[k+N][j], c='blue', marker='.', edgecolors='none')
			ax.scatter(solutions[N-2][j], solutions[N-2+N][j], c='orange',s=250, marker='.', edgecolors='none')
			ax.scatter(solutions[N-1][j], solutions[N-1+N][j], c='red',s=100, marker='.', edgecolors='none')

		plt.savefig('./animation/Frame'+'%04d'%cntr+'.png',dpi=300)
		cntr += 1
		plt.close(fig)

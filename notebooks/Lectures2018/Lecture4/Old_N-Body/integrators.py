'''
Authors: Sergio Mundo and Laura Lenkic

Date: 11/14/2017

Filename: integrators.py

Fourth-Order Runge-Kutta and Second-Order Leapfrog integrators and definition of equations to be integrated.
'''

import numpy as np
import sys

#---------------------------Velocity and Acceleration equations, separated into x, y, and z components---------------------------
def accel(GM,r1, r2, mag):
	return -GM*(r1 - r2)/(mag**3)

def vx(vals,coeff,particle,eps):
	vx_array = vals[3*len(vals)/6:4*len(vals)/6]
	vx = vx_array[particle]
	return vx

def vy(vals,coeff,particle,eps):
	vy_array = vals[4*len(vals)/6:5*len(vals)/6]
	vy = vy_array[particle]
	return vy

def vz(vals,coeff,particle,eps):
	vz_array = vals[5*len(vals)/6:6*len(vals)/6+1]
	vz = vz_array[particle]
	return vz

def vx_dot(vals,coeff,particle,eps):
	N = len(coeff)
	GM = coeff
	acc = np.zeros(3)
	x_array = vals[0:len(vals)/6]
	y_array = vals[len(vals)/6:2*len(vals)/6]
	z_array = vals[2*len(vals)/6:3*len(vals)/6]
	a = 0
	for j in range(N):
		if j != particle:
			mag = np.sqrt((x_array[particle] - x_array[j])**2 + (y_array[particle] - y_array[j])**2 + (z_array[particle] - z_array[j])**2 + eps**2)
			a += accel(GM[j],x_array[particle], x_array[j], mag)
                
	return a

def vy_dot(vals,coeff,particle,eps):
	N = len(coeff)
	GM = coeff
	acc = np.zeros(3)
	x_array = vals[0:len(vals)/6]
	y_array = vals[len(vals)/6:2*len(vals)/6]
	z_array = vals[2*len(vals)/6:3*len(vals)/6]
	a = 0
	for j in range(N):
		if j != particle:
			mag = np.sqrt((x_array[particle] - x_array[j])**2 + (y_array[particle] - y_array[j])**2 + (z_array[particle] - z_array[j])**2 + eps**2)
			a += accel(GM[j],y_array[particle], y_array[j], mag)
                
	return a

def vz_dot(vals,coeff,particle,eps):
	N = len(coeff)
	GM = coeff
	acc = np.zeros(3)
	x_array = vals[0:len(vals)/6]
	y_array = vals[len(vals)/6:2*len(vals)/6]
	z_array = vals[2*len(vals)/6:3*len(vals)/6]
	a = 0
	for j in range(N):
		if j != particle:
			mag = np.sqrt((x_array[particle] - x_array[j])**2 + (y_array[particle] - y_array[j])**2 + (z_array[particle] - z_array[j])**2 + eps**2)
			a += accel(GM[j],z_array[particle], z_array[j], mag)
                
	return a

def rk4(functions,ics,coeff,t,eps):
	"""
	Fourth-order Runge Kutta Integrator

	param functions: array of functions that are to be integrated
	param ics: array of initial conditions of problem
	param coeff: array of coefficients for functions
	param t: array of start point, end point, and time step to use in integration
	"""	
	# Vals stores each new calculated step in solution, to be used to calculate next step.
	vals = ics

	# Store estimated slopes, intermediate values of solutions, and final value of solution.
	k1 = np.zeros(len(functions))
	k2 = np.zeros(len(functions))
	k3 = np.zeros(len(functions))
	k4 = np.zeros(len(functions))
	int_vals = np.zeros(len(functions))
	dt = t[2]
	solutions = np.zeros((len(functions),int(t[1]/dt)))
	for i in range(len(functions)):
		solutions[i][0] = ics[i]

	cntr = 0
	N = len(functions)/6
	# Integrate from t = 0 to tmax, in time steps dt.
	for j in np.arange(0 + t[2], t[1]/t[2]):
		# First estimate of next point in solution.
		for i in range(0,len(functions)):
			# Keeps track of which particle calculations are being done for.
			particle = i%N
			k1[i] = functions[i](vals,coeff,particle,eps)
		for i in range(0,len(functions)):
			int_vals[i] = vals[i] + 0.5*dt*k1[i]

		# Second estimate, based on first.
		for i in range(0,len(functions)):
			particle = i%N
			k2[i] = functions[i](int_vals,coeff,particle,eps)
		for i in range(0,len(functions)):
			int_vals[i] = vals[i] + 0.5*dt*k2[i]

		# Third estimate, based on second.
		for i in range(0,len(functions)):
			particle = i%N
			k3[i] = functions[i](int_vals,coeff,particle,eps)
		for i in range(0,len(functions)):
			int_vals[i] = vals[i] + dt*k3[i]

		# Final estimate based on four slope estimates; store in solution.
		for i in range(0,len(functions)):
			particle = i%N
			k4[i] = functions[i](int_vals,coeff,particle,eps)
			solutions[i][cntr] = vals[i] + dt*((1./6.)*k1[i] + (1./3.)*k2[i] + (1./3.)*k3[i] + (1./6.)*k4[i])

		# Update to new point to use in integration of next point.
		vals = []
		for i in range(0, len(functions)):
			vals.append(solutions[i][cntr])

		cntr += 1

	return solutions
 
def leapfrog(functions,ics,coeff,t,eps):
	"""
	Second-order Leap Frog Integrator

	param functions: array of functions that are to be integrated
	param ics: array of initial conditions of problem
	param coeff: array of coefficients for functions
	param t: array of start point, end point, and time step to use in integration
	"""	
	# Vals stores each new calculated step in solution, to be used to calculate next step.
	vals = ics
	
	# Store intermediate values of solutions, and final value of solution.
	int_vals = np.zeros(len(functions))
	dt = t[2]
	solutions = np.zeros((len(functions),int(t[1]/dt)))
	# setting initial conditions
	for i in range(len(functions)):
		solutions[i][0] = ics[i]
 
 	step = len(functions)/2
 	cntr = 0
 	N = len(functions)/6
 	# Integrate from t = 0 to 100, in time steps dt.
	for j in np.arange(0 + t[2], t[1]/t[2]):
		
		# OPEN DRIFT: Calculate midstep of the in between functions
		for i in np.arange(0,len(functions)/2):
			int_vals[i] = vals[i] + 0.5*dt*vals[i+step]

		# KICK: Calculating the final for the main function
		for i in np.arange(len(functions)/2,len(functions)):
			particle = i%N
			solutions[i][cntr] = vals[i] + dt*functions[i](int_vals,coeff,particle,eps)
			
		# CLOSING DRIFT: Calculating the final for the in between functions
		for i in np.arange(0,len(functions)/2):
			solutions[i][cntr] = int_vals[i] + 0.5*dt*solutions[i+step][cntr]

		# Update to new point to use in integration of next point.
		vals = []
		for i in range(0, len(functions)):
			vals.append(solutions[i][cntr])

		cntr += 1

	return solutions
 
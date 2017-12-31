'''
Authors: Sergio Mundo and Laura Lenkic

Date: 11/21/2017

Filename: ics.py

Generate initial conditions for 250 particles in a disk around a central star while a second low-mass star flies by.
'''

import numpy as np

# Want x, y, and z coordinates for 250 particles.
NNN=250
N_pv = NNN
D_pv = 3

N_m = NNN
D_m = 1

# Generate random numbers between 0 and 1, to be used to calculate radius and true anomaly angle of each particle, which will then be used to calculate x and y coordinates.
TAA = np.random.random_sample((N_pv))
RAD = np.random.random_sample((N_pv))

# Arrays to store positions, masses, and velocities.
pos = np.zeros((NNN+2,3))
mass = np.zeros((NNN+2,3))
vel = np.zeros((NNN+2,3))

# Calculate the x and y coordinates based on x = r*cos(TAA) and y = r*sin(TAA), where r is set to be between 1 and 1.5. Then calculate the velocity of each particle based on
# its x and y coordinates. Then generate random numbers for the mass of each particle.
for i in range(0,NNN):
    pos[i][0] = np.cos(TAA[i]*2*np.pi)*(1.0+0.5*RAD[i])
    pos[i][1] = np.sin(TAA[i]*2*np.pi)*(1.0+0.5*RAD[i])
    pos[i][2] = 0.0

    vel[i] = -pos[i]*0.0
    vel[i] = [-np.sin(TAA[i]*2*np.pi)/(1.0+0.5*RAD[i])**(0.5),np.cos(TAA[i]*2*np.pi)/(1.0+0.5*RAD[i])**(0.5),0]

    inter = np.random.random(1)[0]
    mass[i][0] = inter*1e-6

# Set the mass of the central star, and star that flies by.
mass[NNN][0] = 1.0
mass[NNN+1][0] = .1

# Set initial position and velocity of star that flies by.
pos[NNN+1] = [4,5,0]
vel[NNN+1] = [-3,-3,0]

# Write initial conditions to file "Initial_Conditions.txt"
data = open('Initial_Conditions.txt','w')
for i in range(0,NNN+2):
	data.write(str(mass[i][0])+'\t\t'+str(pos[i][0])+'\t\t'+str(pos[i][1])+'\t\t'+str(pos[i][2])+'\t\t'+str(vel[i][0])+'\t\t'+str(vel[i][1])+'\t\t'+str(vel[i][2])+'\n')

data.close()

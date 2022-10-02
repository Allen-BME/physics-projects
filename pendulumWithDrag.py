"""
This program is inspired by and partly taken from 3blue1brown's youtube video: https://youtu.be/p_di4Zn4wz4
Author: Carter Allen
Date: 3/22/2022
Purpose: Ask user for initial angle (radians) and velocity. Plot the angle and velocity of a pendulum with drag force over time.
"""

import numpy as np
import matplotlib.pyplot as plt

# Physical Constants
g = 9.8
L = 2
mu = 0.1

# Definition of ODE (credit to Grant Sanderson of 3Blue1Brown)
def getThetaDoubleDot(theta, thetaDot):
    return -mu * thetaDot - (g / L) * np.sin(theta)

# Solution to the DE (credit to Grant Sanderson of 3Blue1Brown)
def theta(t):
    # Initialize changing values
    theta = float(input("Enter an initial angle: "))
    theta_dot = float(input("Enter an initial velocity: "))
    delta_t = 0.01 # time step
    increments = np.arange(0, t, delta_t)
    values = np.empty([increments.size+1, 2]) # empty array that will store values of theta and theta_dot
    values[0] = np.array([theta, theta_dot]) 
    for index, time in enumerate(increments): # from 0 to t in steps of delta_t
        theta_double_dot = getThetaDoubleDot(theta, theta_dot)
        theta += theta_dot * delta_t # tiny nudge in direction of R.O.C.
        theta_dot += theta_double_dot * delta_t # tiny nudge in direction of R.O.C.
        values[index+1] = [theta, theta_dot]
    return values

values = theta(60)

fig, ax = plt.subplots()
ax.plot(values[:,0], values[:,1])
plt.xlabel("Theta (radians)")
plt.ylabel("Velocity (m/s)")
plt.title("Theta vs Velocity of pendulum with drag force")
plt.grid()
plt.show()
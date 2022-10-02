"""
Author: Carter Allen
Date: 3/24/2022
Purpose: This program takes user inputted values for the inital velocity and launch angle of a projectile
    and returns a plot of the arc of the projectile. The program assumes that the inital height was at 0
    and that there is no air resistance.

# outdated. projectile.py handles multiple heights
"""

import numpy as np
import matplotlib.pyplot as plt

def projectile(velocity, theta, delta_t=0.01):
    """
    Takes an inital velocity, angle, and optionally a time increment and returns values for x and y of arc of motion.

    @param velocity: Initial magnitude of velocity for projectile. Must be non-zero and positive
    @param theta: Launch angle above positive x-axis. Must be between 0 and 180, non-inclusive
    @param delta_t: Optional size of time increments. Default is 0.01 seconds
    """
    delta_y = 0 # y0 is ground level
    v0y = velocity * np.sin(np.deg2rad(theta)) # y-component of velocity
    vfy = -v0y # because delta_y = 0
    time = (vfy - v0y) / -9.8

    increments = np.arange(0, time, delta_t)

    v0x = velocity * np.cos(np.deg2rad(theta)) # x component of velocity
    xf = round(v0x * time, 3) # x displacement
    x = np.linspace(0, xf, increments.size) # x values over time interval evenly spaced by delta_t

    y = np.empty(increments.size)
    for index, t in enumerate(increments):
        y[index] = v0y * t - 4.9 * (t*t) # y values over time interval evenly spaced by delta_t

    return x, y, time 

def plotArc(x, y, theta):
    """
    Takes a numpy array x, numpy array y, and theta and plots the arc.

    @param x: numpy array of x-values for projectile motion
    @param y: numpy array of y-values for projectile motion
    @param theta: launch angle above positive x-axis. Used to determine direction of x-axis
    """
    pfig, ax = plt.subplots()
    ax.plot(x, y)

    if theta <= 90: # if angle less than 90, positive x-axis
        if  np.amax(x) > np.amax(y): # both axes should be same size, make axes limits 1.05x the biggest value on either axis
            plt.xlim([0, 1.05 * np.amax(x)])
            plt.ylim([0, 1.05 * np.amax(x)])
        else:
            plt.xlim([0, 1.05 * np.amax(y)])
            plt.ylim([0, 1.05 * np.amax(y)])
    else: # if angle greater than 90, negative x-axis
        if  np.amax(np.absolute(x)) > np.amax(y):
            plt.xlim([-1.05 * np.amax(np.absolute(x)), 0])
            plt.ylim([0, 1.05 * np.amax(np.absolute(x))])
        else:
            plt.xlim([1.05 * -np.amax(y), 0])
            plt.ylim([0, 1.05 * np.amax(y)])

    plt.xlabel("X (m)")
    plt.ylabel("Y (m)")
    plt.title("Arc of launched projectile")
    plt.grid()
    plt.show()

# prompt user for inital values
print("This program plots the arc of a launched projectile.\nNOTE: It is assumed that the projectile is launched " \
     "from ground level and faces no air resistance\n")
velocity = float(input("What is the inital velocity of the projectile?: "))
while velocity <= 0:
    print("Velocity must be positive and non-zero.")
    velocity = float(input("What is the inital velocity of the projectile?: "))
theta = float(input("What is the launch angle of the projectile?: "))
while theta <= 0 or theta >= 180:
    print("Launch angle must be between 0 and 180.")
    theta = float(input("What is the launch angle of the projectile?: "))

x,y,time = projectile(velocity, theta)

plotArc(x, y, theta)

# ideas for expansion:

# find and display the max height
# angles between 
# GUI
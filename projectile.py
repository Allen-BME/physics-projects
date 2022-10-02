"""
This program was inspired by the classic physics 1 problem of a projectile. This assumes no air 
resistance. Using equally long x and y axes, the program shows the arc that a projectile would
take from a given height, angle, and velocity. 

Author: Carter Allen

Date Created: 3/25/2022
Last Updated: 10/1/2022

Purpose: This program takes user inputted values for the inital velocity, launch angle, and inital height of a projectile
    and returns a plot of the arc of the projectile. The program assumes that there is no air resistance.
"""

import numpy as np
import matplotlib.pyplot as plt
from os import system

# --- Pyinstaller stuff
import _cffi_backend

clear = lambda: system('cls')

def projectile(velocity, theta, initial_height, delta_t=0.01):
    """
    Takes an inital velocity, angle, height, and optionally a time increment and returns values for x and y of arc of motion.

    @param velocity: Initial magnitude of velocity for projectile. Must be non-zero and positive
    @param theta: Launch angle relative to positive x-axis. 
    @param initial_height: Height that projectile is launched from.
    @param delta_t: Optional size of time increments. Default is 0.01 seconds
    """
    delta_y = 0 - initial_height
    v0y = velocity * np.sin(np.deg2rad(theta)) # y-component of velocity
    vfy = -np.sqrt(v0y*v0y + 2*-9.8*delta_y)
    time = (vfy - v0y) / -9.8

    increments = np.arange(0, time, delta_t)

    v0x = velocity * np.cos(np.deg2rad(theta)) # x component of velocity
    xf = round(v0x * time, 3) # x displacement
    x = np.linspace(0, xf, increments.size) # x values over time interval evenly spaced by delta_t

    y = np.empty(increments.size)
    for index, t in enumerate(increments):
        y[index] = v0y * t - 4.9 * (t*t) + initial_height

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

    if np.amax != 0: # if x-motion is positive, show positive x-axis
        if  np.amax(x) > np.amax(y): # both axes should be same size, make axes limits 1.05x the biggest value on either axis
            plt.xlim([0, 1.05 * np.amax(x)])
            plt.ylim([0, 1.05 * np.amax(x)])
        else:
            plt.xlim([0, 1.05 * np.amax(y)])
            plt.ylim([0, 1.05 * np.amax(y)])
    else: # if x-motion is negative, show negative x-axis
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

if __name__ == "__main__":
    clear()
    print("This program plots the arc of a launched projectile.\nNOTE: It is assumed that the projectile " \
        "faces no air resistance\n")
    userWantContinue = True
    while userWantContinue: 
        velocity = float(input("What is the inital velocity of the projectile? (m/s): "))
        while velocity <= 0:
            print("Velocity must be positive and non-zero.")
            velocity = float(input("What is the inital velocity of the projectile? (m/s): "))
        theta = float(input("What is the launch angle of the projectile? (degrees above x-axis): "))
        initial_height = float(input("What is the initial height of the projectile? (m): "))
        while initial_height < 0:
            print("Sorry, initial height cannot be negative.")
            initial_height = float(input("What is the initial height of the projectile? (m): "))

        x,y,time = projectile(velocity, theta, initial_height)

        plotArc(x,y,theta)
        ans = input("\nDo you want to continue? [y/n]: ")
        while ans != 'y' and ans != 'n':
            print("Enter 'y' or 'n'")
            ans = input("Do you want to continue? [y/n]: ")

        if ans == 'n':
            userWantContinue = False
        if ans == 'y':
            clear()
    print("\n**************")
    print("Program ended.\n")
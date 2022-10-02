"""
This program was inspired by the classic physics 1 problem of a projectile. This assumes no air 
resistance. Using equally long x and y axes, the program shows the arc that a projectile would
take from a given height, angle, and velocity. 

Author: Carter Allen

Date Created: 3/25/2022
Last Updated: 10/1/2022

Purpose: Practice Physics I concepts and Python programming by modeling a projectile. 

Function: This program takes user inputted values for the inital velocity, launch angle, and inital
    height of a projectile and returns a plot of the arc of the projectile. The program assumes that 
    there is no air resistance.
"""


import numpy as np
import matplotlib.pyplot as plt
from os import system


def projectile(velocity, theta, initial_height, delta_t=0.01):
    """
    Takes an inital velocity, angle, height, and optionally a time increment and returns values for x
    and y of arc of motion.

    velocity = Initial magnitude of velocity for projectile. Must be non-zero and positive
    theta = Launch angle relative to positive x-axis. 
    initial_height = Height that projectile is launched from.
    delta_t = Optional size of time increments. Default is 0.01 seconds
    """

    #  height will always end at 0
    delta_y = 0 - initial_height

    # initial y velocity =
    # initial velocity * sin(theta)
    v0y = velocity * np.sin(np.deg2rad(theta))

    # find vfy and time with kinematics equation
    vfy = -np.sqrt(v0y*v0y + 2*-9.8*delta_y)
    time = (vfy - v0y) / -9.8

    # find the increments of time corresponding
    # to each position value that will be found
    increments = np.arange(0, time, delta_t)

    # no acceleration in x-axis
    # x velocity = velocity * cos(theta)
    v0x = velocity * np.cos(np.deg2rad(theta))

    # x displacement from constant velocity and time
    xf = round(v0x * time, 3) 

    # x values over time interval evenly spaced by delta_t
    x = np.linspace(0, xf, increments.size) 

    # find each corresponding y-value with kinematics
    y = np.empty(increments.size)
    for index, t in enumerate(increments):
        y[index] = v0y * t - 4.9 * (t*t) + initial_height

    return x, y, time 


def plotArc(x, y, theta):
    """
    Takes a numpy array x and numpy array y and plots the arc.

    x = numpy array of x-values for projectile motion
    y = numpy array of y-values for projectile motion
    """

    # initialize plot
    pfig, ax = plt.subplots()
    ax.plot(x, y)

     # if x-motion is positive, show positive x-axis
    if np.amax != 0:

        # both axes should be same size
        # make axes limits 1.05x the biggest value on either axis
        if  np.amax(x) > np.amax(y): 
            plt.xlim([0, 1.05 * np.amax(x)])
            plt.ylim([0, 1.05 * np.amax(x)])
        else:
            plt.xlim([0, 1.05 * np.amax(y)])
            plt.ylim([0, 1.05 * np.amax(y)])

    # if x-motion is negative, show negative x-axis
    else:

        if  np.amax(np.absolute(x)) > np.amax(y):
            plt.xlim([-1.05 * np.amax(np.absolute(x)), 0])
            plt.ylim([0, 1.05 * np.amax(np.absolute(x))])
        else:
            plt.xlim([1.05 * -np.amax(y), 0])
            plt.ylim([0, 1.05 * np.amax(y)])

    # finalize plot
    plt.xlabel("X (m)")
    plt.ylabel("Y (m)")
    plt.title("Arc of launched projectile")
    plt.grid()
    plt.show()


def ask_user_if_continue():
    ans = input("Would you like to continue? (y/n): ")
    while ans.lower() not in ['y', 'n']:
        print("Please enter either y or n...")
        ans = input("Would you like to continue? (y/n): ")
    return True if ans == 'y' else False


clear = lambda: system('cls')


# run this section if program is being directly run
if __name__ == "__main__":

    clear()

    print("*********************************************")
    print("Projectile:")
    print(" - angle measured in degrees")
    print(" - velocity measured in m/s")
    print(" - initial height measured in m")
    print(" - air resistance is NOT taken into account")
    print(" - plot the arc the projectile will make")
    print("*********************************************")

    userWantContinue = True
    while userWantContinue: 

        # prompt user for velocity
        print("What is the inital velocity of the projectile?")
        velocity = float(input("(m/s): "))
        while velocity <= 0:
            print("Velocity must be positive and non-zero.")
            velocity = float(input("What is the inital velocity of the projectile? (m/s): "))

        # prompt user for theta
        print("What is the launch angle of the projectile?")
        theta = float(input("(degrees above x-axis): "))

        # prompt user for initial height
        print("What is the initial height of the projectile?")
        initial_height = float(input("(m): "))
        while initial_height < 0:
            print("Sorry, initial height cannot be negative.")
            initial_height = float(input("What is the initial height of the projectile? (m): "))

        # find x and y positions and total time
        x,y,time = projectile(velocity, theta, initial_height)

        plotArc(x,y)

        user_wants_to_continue = ask_user_if_continue()

    print("Program ended.\n")
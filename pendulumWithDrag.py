"""
This program is inspired by and partly taken from 3blue1brown's youtube video: https://youtu.be/p_di4Zn4wz4

It aims to represent a pendulum with drag through differential equations. Imagine a pendulum at an initial
velocity theta_dot and angle theta. The pendulum will tend towards a state of rest hanging at the bottom.
It may loop around a couple of times before losing enough velocity, however, it will always start to
come to a rest. The relationship between theta and theta_dot can be represented with two axes of a graph
and the result of a given set of inital conditions can be represented as a line.

Author: Carter Allen

Date Created: 3/22/2022
Last Updated: 10/1/2022

Purpose: Play with the idea of differential equations in Python by looking at the case of a pendulum with
    drag. Given a set of inital conditions, roughly estimte how the system will change over the next
    60 seconds with an ODE.

Function: Ask user for initial angle (radians) and velocity. Plot the angle (x) and velocity (y) of a pendulum
    with drag force over time.

Notes:
    - It is difficult to interpret the graph. Start by finding the point of the given initial conditions 
      (red dot) and treat following the line as following the angle and velocity as time increases
    - Note how the graph always starts to circle around a velocity of 0 and an angle that is a multiple of 2 pi

TODO:
    - handle non-numerical inputs for velocity and theta
    - make what's happening in this mess clearer
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
def get_theta(t, theta, theta_dot):
    """
    t = length of time (s) to analyze
    theta = initial angle (radians)
    theta_dot = initial velocity (m/s)

    return: array of angles (theta) corresponding to 0.01 s steps in time
    """

    # Initialize changing values
    delta_t = 0.01
    increments = np.arange(0, t, delta_t)

    # empty array that will store values of theta and theta_dot
    values = np.empty([increments.size+1, 2]) 
    values[0] = np.array([theta, theta_dot]) 

    # from 0 to t in steps of delta_t
    for index, time in enumerate(increments): 
        theta_double_dot = getThetaDoubleDot(theta, theta_dot)

        # tiny nudge in direction of rate of change
        # (nudge in direction of 2nd deriv for theta_dot)
        # (nudge in direction of 1st deriv for theta)
        theta += theta_dot * delta_t 
        theta_dot += theta_double_dot * delta_t 
        values[index+1] = [theta, theta_dot]

    return values


def ask_user_if_continue():
    ans = input("Would you like to continue? (y/n): ")
    while ans.lower() not in ['y', 'n']:
        print("Please enter either y or n...")
        ans = input("Would you like to continue? (y/n): ")
    return True if ans == 'y' else False


# run this section if program is being directly run
if __name__ == "__main__":
    
    print("*********************************************")
    print("Pendulum with drag:")
    print(" - angle measured in radians")
    print(" - velocity measured in m/s")
    print(" - drag is taken into account")
    print(" - analyze results of 60s time period after")
    print("   initial conditions")
    print("*********************************************")

    user_wants_to_continue = True
    while user_wants_to_continue:

        # prompt user for input
        theta = float(input("Enter an initial angle: "))
        theta_dot = float(input("Enter an initial velocity: "))

        # get the values
        values = get_theta(
            t=60, theta=theta, theta_dot=theta_dot
        )

        # plot the results
        fig, ax = plt.subplots()
        ax.plot(values[:,0], values[:,1])
        ax.plot(values[0,0], values[0,1], "ro")
        plt.xlabel("Theta (radians)")
        plt.ylabel("Velocity (m/s)")
        plt.title("Theta vs Velocity of pendulum with drag force")
        plt.grid()
        plt.show()

        user_wants_to_continue = ask_user_if_continue()
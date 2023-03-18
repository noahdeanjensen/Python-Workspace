"""This program will calculate the height"""

# Noah Jensen
# 1300


# imported math libraries you need to do this via a virtual environment using
# the command line hopefully I've packaged them correctly so it works on your end.
import numpy as np
from sympy import *


def timetillground(height, velocity):
    """Here we get the time it takes to hit the ground"""
    # velocity equation is the equation given already now it is formated into an array
    velocityequation = [-16, velocity, height]
    # get the x intercepts and then print out value which is the greatest. The fuction orders
    # from largest to smallest hence the time[0]
    time = np.roots(velocityequation)
    print("The ball will hit the ground after approximately ",
          time[0], " seconds")


def maxheight(height, velocity):
    """In this function we find how high the ball has traveled """
    # since I was doing an equation I decided to actually use a t variable.
    t = symbols('t')
    # acceleration equation via taking derivative as an array
    accelerationequation = [-32, velocity, 0]
    # pass array into np.roots which will give us the x intercept

    time = np.roots(accelerationequation)
    # after getting x intercept plug value back in and print out value.

    startingequation = (height + (velocity*t) - (16*t*t))
    print("The maximum height of the ball is ",
          startingequation.subs(t, time[0]), " feet")

    timetillground(height, velocity)


def isvalid(height, velocity):
    """The is valid function checks whether the values are positive or not. 
    If they are negative it asks you to put in new values. """
    # check if values are less positve if not ask again
    if (height <= 0) or (velocity <= 0):
        print("Only positive values are accepted \n Please enter again")
        getinput()
    else:
        maxheight(height, velocity)


def getinput():
    """This function takes in the input and passes the values to the isValid function """
    # get values from user
    height = int(input("Please enter the height initial height of the ball "))
    velocity = int(input("Please enter the initial velocity of the ball "))
    # pass the values onto isvalid function
    isvalid(height, velocity)


getinput()


"""This program I decided to challenge myself and first create a virtual environment in
 vscode to be able to use the numpy and sympy 
libraries. For this program I decided to use my knowledge from
 calculus to solve the problem. I did not add a creative element sadly because I'll be 
honest I was slightly burnt out from school. Hopefully, it works on your side did not
 try testing in Docker plus I'm not a Dev Opps engineer if not 
I can show you in class. """

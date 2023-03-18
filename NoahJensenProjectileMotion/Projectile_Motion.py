"""This program will calculate the height and also graph the projectile"""

import numpy as np
from sympy import *


def timeTillGround(height, velocity):
    """Here we get the time it takes to hit the ground"""
    velocityequation = [-16,velocity, height]
    time= np.roots(velocityequation)
    print("The ball will hit the ground after approximately ",time[0], " seconds")
    
    
  

def maxheight(height,velocity):
    """In this function we find how high the ball has traveled """
    t = symbols('t')
    accelerationequation = [-32,velocity,0]
    time= np.roots(accelerationequation)
    startingEquation = (height + (velocity*t) - (16*t*t)) 
    print("The maximum height of the ball is ", startingEquation.subs(t,time[0])," feet")
    


    timeTillGround(height,velocity)

def isvalid(height, velocity):
    """The is valid function checks whether the values are positive or not. If they are negative it asks you to put in new values. """
    if (height <= 0) or (velocity <= 0):
        print("Only positive values are accepted \n Please enter again")
        getinput()
    else:
        maxheight(height,velocity)  


def getinput():
    """This function takes in the input and passes the values to the isValid function """
    height = int(input("Please enter the height initial height of the ball "))
    velocity = int(input( "Please enter the initial velocity of the ball "))
    isvalid(height, velocity)

getinput()


"""This program I decided to challenge myself and first create a virtual environment in vscode to be able to use the numpy and sympy 
libraries. For this program I decided to use my knowledge from calculus to solve the problem. """


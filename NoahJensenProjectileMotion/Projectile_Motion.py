"""This program will calculate the height and also graph the projectile"""

import numpy as np
from sympy import *

a = np.matrix('1 2; 3 4')

print(a)


def getinput():
    """This function takes in the input and passes the values to the isValid function """
    height = input("Please enter the height initial height of the ball ")
    velocity = input( "Please enter the initial velocity of the ball ")
    isvalid(height, velocity)
getinput()

def isvalid(height, velocity):

    if( (height <= 0) or (velocity <= 0) ):
        print("Only positive values are accepted \n Please enter again")
        getinput()
    else:
            print("hi")


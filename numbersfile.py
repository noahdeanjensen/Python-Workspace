"""For this program I will get the max, min, and count of the numbers in a text file """

#Here I import numpy to use some of its pre built in functions.
import numpy as np



def testforfile():

    """I will create a testforfile function to check if the file is truly found if not it 
    will throw an exception"""

    #start of my try statement
    try:

        #create a variable to load in my text file

        numbersfile = np.loadtxt("Numbers-1.txt")

        #Here call the amax function to get the max

        print("Max number:",np.amax(numbersfile))

        #Here I call the amin function to get the min

        print("Minimum number", np.amin(numbersfile))

        # use the built in count_nonzeros function to count all numbers greater or equal to zero
        print("Count of numbers", np.count_nonzero(numbersfile >=  0))



    #exception error for File not found
    except FileNotFoundError:

        print("The file or directory cannot be found ")


testforfile()

"""My creative element I chose for the file was to use a try and except statements
to handle the file not found error. I also decided to use the numpy library to make 
it easy to just find all these values. I previoulsy did this in my data analytics class."""

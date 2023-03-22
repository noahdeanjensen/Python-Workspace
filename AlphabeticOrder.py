"""This program will take in a string and check if the string has 3 consecutive characters"""

#Noah Jensen
#March 21, 2022
#CS 1300-01

def takeinput():
    """This function takes in the input from the user and checks if it contains characters."""
    wordTest = input(
        "Please enter a word to check if it has 3 conesecutive characters in the alphabet? ")
    # make lower to get all the same ascii value.
    wordTest = wordTest.lower()
    # creative element to check if what is entered is letters
    if wordTest.isalpha() == True:
        isTripleConsecutive(wordTest)
    else:
        # will inform you and have you enter again
        print("Please enter a word that does not contain anything "
              "other than letters in the alphabet. ")
        takeinput()


def isTripleConsecutive(wordTest):
    """This function will check if the word contains consecutive values"""
    # create a value as false by default
    result = False

    # iterate through knowing that the ascii values are in consecutive order
    # and that they will at most be three away from each other

    for i in range(len(wordTest)-2):

        if ord(wordTest[i]) == ord(wordTest[i+1])-1 == ord(wordTest[i+2])-2:
            result = True

    print(result)


def main():
    """Main function"""
    # call take input
    takeinput()


main()


"""The problem wasn't challenging however, the syntax to write the for loop was
given that I was converting to ascii values and moving indexes."""

"""This program will take in a string and check if it is a palindrome"""
wordentered = input('Please enter a word or phrase to check if it is a Palindrome ')


def ispalindrome(wordentered: str) -> str:
    """This function will take in a string then return a phrase indicating it is a Palindrome 
    or not"""

    # create empty string in case wordentered has anything other than alphunumerical values
    newstring = ""

    # for loop to iterate through check if the value is alphanumerical if it is
    #  it is added into new string
    for index in wordentered:
        if index.isalnum():
            newstring += index.lower()

    # check if the reversed string is equal to the non reversed string
    if newstring == newstring[::-1]:
        print(" The word entered is a Palindrome")

    # if not print the word is not a palindrome
    else:
        print(" The word entered is not a Palindrome")


ispalindrome(wordentered)
"""For my creative element I decided to use many built in functions in python so I did not 
have to create an alphanumerical checker function decreasing 
complexity in the code and lines used """

"""This program will take in a string and check if the string has 3 consecutive characters"""

def takeinput():
    """This function takes in the input from the user and checks if it contains characters."""
    wordTest = input("Please enter a word to check if it has 3 conesecutive characters in the alphabet? ")
    wordTest = wordTest.lower()
    if wordTest.isalpha()==True:
        isTripleConsecutive(wordTest)
    else:
        print("Please enter a word that does not contain anything other than letters in the alphabet. ")
        takeinput()


def isTripleConsecutive(wordTest):
    """This function will check if the word contains consecutive values"""
    
    
    
    isTripleConsecutive



def main():

    takeinput()

main()
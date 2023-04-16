"""This python script will read in and count the teams that have won four rosebowls or more. """

from collections import Counter
import os

def main():
    """Main function for script"""

    def read_file():

        """using try/else statement read file into list """
        try:
            here = os.path.dirname(os.path.abspath(__file__))

            filename = os.path.join(here, 'Rosebowl.txt')

            # open the file

            infile = open(filename, 'r', encoding="utf8")

            teams = []

            for line in infile:
                teams.append(line.strip("\n"))

            



        except FileNotFoundError:

            print("The file or directory cannot be found ")




    read_file()

main()

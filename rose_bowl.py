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

            # create list for teams

            teams = []

            # read team in and add to list

            for line in infile:
                teams.append(line.strip("\n"))

            infile.close()

            return teams

        except FileNotFoundError:

            print("The file or directory cannot be found ")

    def count_wins():
        """Count the amount of wins from the file"""

        teams = read_file()

        # create dictionary for teams

        teams_dictionary = Counter(teams)

        # find the teams that won 4 or more times.

        for team, wins in sorted(teams_dictionary.items()):
            if wins >= 4:
                print(team, wins)

    count_wins()


main()

"""I decided to go through and use the counter library to count the occurrences
of the teams that had won. I didn't add any creative element but I was able to fulfill
all other requirements."""

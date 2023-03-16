"""This program will take the input of a card number and check if it is valid 
and what bank issued the card """

# take input from user
cardnum = input(" Enter card number to be validated ")

# create a dictionary of valid bank issuers
bankidentificationnumber = {3: "American Express",
                            4: "Visa", 5: "Mastercard", 6: "Discover"}

# check if the card number is valid and if it the issuer is contained in the dictionary
if len(cardnum) != 14 or int(cardnum[0]) > 6 or int(cardnum[0]) < 3:
    print(" The card number is invalid Please double check card number.")

# else statement to enter function to validate number if it meets mathmatical qualifications
else:
    def checkcard(cardnum):
        """This function will take in the card number identify what bank issued 
        the card and also find if the number is a valid number """
        issuer = int(cardnum[0])
        if issuer in bankidentificationnumber:
            print("The bank that issued your card is ",
                  bankidentificationnumber.get(issuer))

            # create even sum for even indexes in the card number
            evensum = 0

            # for loop to  add and check where the doubling of values in less than 10 then adding
            # it to evensum variable
            for index in range(0, len(cardnum), 2):
                check = 0
                check = int(cardnum[index]) * 2
                if check > 9:
                    evensum += int(check) - 9
                else:
                    evensum += check

            # for loop to add all odd indexes
            oddsum = 0
            for index in range(1, len(cardnum), 2):
                oddsum += int(cardnum[index])

            # add oddsum and evensum to final sum then check via modulus
            finalsum = oddsum + evensum
            if finalsum % 10 == 0:
                print(" The card number is valid ")
            else:
                print("The card number is invalid ")

    checkcard(cardnum)
"""My creative element for my program was to check what bank issued the card by following the
American Network of Standards Institute for cards """
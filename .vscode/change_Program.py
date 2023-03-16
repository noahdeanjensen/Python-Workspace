# creating a program to give you back the correct change.


#global variables
# dollar currencies
dollar_bill = 1
five_bill = 5
ten_bill = 10
twenty_bill = 20
fifty_bill = 50
hundred_bill = 100
# cent currencies
penny = 1
nickel = 5
dime = 10
quarter = 25


# input from user
user_input_amount = float(input("Enter a number in monetary form: "))
# gives me the dollar amount
dollar_amount = int(user_input_amount)

# this function gives me the decimal numbers in the input from the user.


def get_decimal(user_input_amount):
    if type(user_input_amount) == float:
        last_two_digit = str(user_input_amount)[-2:]

        if float(last_two_digit) >= 1:

            return float(last_two_digit) * .01

        else:

            return float(last_two_digit)


# gives you the amount of the change for denominations lower than a dollar


def cent_change():
    decimal_amount = round(get_decimal(user_input_amount) * 100)

    penny_count = 0
    nickel_count = 0
    dime_count = 0
    quarter_count = 0

    if decimal_amount >= quarter:
        quarter_count = int(decimal_amount / quarter)

    decimal_amount = decimal_amount - (quarter_count * 25)

    if decimal_amount >= dime:
        dime_count = int(decimal_amount / dime)

    decimal_amount = decimal_amount - (dime_count * 10)

    if decimal_amount >= nickel:
        nickel_count = int(decimal_amount / nickel)

    decimal_amount = decimal_amount - (nickel_count * 5)

    if decimal_amount >= penny:
        penny_count = int(decimal_amount / penny)

    decimal_amount = decimal_amount - (penny_count * 1)

    if decimal_amount > 0:
        penny_count += 1

    print('You will recieve: ', quarter_count, ' quarters, ', dime_count, ' dimes, ', nickel_count,
          ' nickels, ', penny_count, ' pennies ')


# gives you how many of each bills you need for change.
def bill_change(dollar_amount):
    hundred_count = 0
    fifty_count = 0
    twenty_count = 0
    ten_count = 0
    five_count = 0
    dollar_count = 0

    if dollar_amount >= hundred_bill:
        hundred_count = int(dollar_amount / hundred_bill)

    dollar_amount = dollar_amount - (hundred_count * 100)

    if dollar_amount >= fifty_bill:
        fifty_count = int(dollar_amount / fifty_bill)

    dollar_amount = dollar_amount - (fifty_count * 50)

    if dollar_amount >= twenty_bill:
        twenty_count = int(dollar_amount / twenty_bill)

    dollar_amount = dollar_amount - (twenty_count * 20)

    if dollar_amount >= ten_bill:
        ten_count = int(dollar_amount / ten_bill)

    dollar_amount = dollar_amount - (ten_count * 10)

    if dollar_amount >= five_bill:
        five_count = int(dollar_amount / five_bill)

    dollar_amount = dollar_amount - (five_count * 5)

    if dollar_amount >= dollar_bill:
        dollar_count = int(dollar_amount / dollar_bill)

    print('You will recieve: ', hundred_count, ' hundred bills, ', fifty_count, ' fifty bills, ', twenty_count,
          ' twentey bills, ', ten_count, ' ten bills, ', five_count, ' five bills, ', dollar_count, ' dollar bills.')


# calling my functions
get_decimal(user_input_amount)
cent_change()
bill_change(dollar_amount)

# I decided for my creative element to create a program that gives you back the exact change for any number bills and coins.
# The format to enter in is any amount followed '.00' for example '154.32'

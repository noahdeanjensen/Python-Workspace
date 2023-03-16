"""Program to find the amount of caffeine in an individuals blood stream"""

amount_of_caffeine_drank = input("Please enter the amount of caffeine ")

hours = input(
    " Please enter how many hours you are going to drink continously ")

# if an individual drinks more than 5000mg you die.
if int(amount_of_caffeine_drank) > 5_000:
    print("You drank to much caffeine you are dead")

# float to calculate percentage of caffeine
percentage = .13

# while loop to calculate amount after 5 hours.
updated = amount_of_caffeine_drank

# while loop to find the time in hours it took to process half or less than half the caffeine amount.

i = 1
while i < 5_000:

    new_level = float(updated) - float(updated) * .13

    updated = new_level

    if updated <= float(amount_of_caffeine_drank) * .5:

        print("The time it took in hours for your caffeine levels to be less than or equal to the caffeine amount taken in is ",
              i, " hours and your caffeine level is ", round(updated), " mg")
        break

    i += 1

"""Function to calculate the amount of caffeine after 24 hours"""


def after_24(amount_of_caffeine_drank):
    j = 1
    start = float(amount_of_caffeine_drank)

    while j < 25:
        final_amount = start - start * .13

        start = final_amount

        if j == 24:
            print("You have roughly ", round(final_amount),
                  " mg of caffeine in your system after 24 hours")
        j += 1


after_24(amount_of_caffeine_drank)

"""Function to find the amount of constant hourly drinking"""


def constant_drink(hours):
    x = 1
    caffeine = 0
    for x in range(int(hours)):
        caffeine = caffeine * 0.87 + 130
    print("You have roughly ", round(caffeine),
          " mg of caffeine after drinking coffee hourly")


constant_drink(hours)

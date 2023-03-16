import re

""" This program will take inpout from the user in form of a string and encode this string into the soundexsystem"""

# Noah Jensen
# 2/19/2020
# CSIS 1300-02

user_input = input("Please enter a string to encode ")

# array to hold first letter
letter = []

# manipulate string

first_letter = user_input[0:1]
rest_string = user_input[1:].lower()
letter.append(first_letter)


""" Function to delete needed letters"""


def delete_letters(rest_string):

    # imported a built in function that would delete the specific characters from string

    deleted = (re.sub("[aeiouhyw]", "", rest_string))
    return deleted


delete_letters(rest_string)


""" Function to encode string"""


def encode_string():

    deleted_string = delete_letters(rest_string)

    # created a dictionary/hashmap to map the characters to there associated values to increase performance

    used_dictionary = {'b': '1', 'f': '1', 'p': '1', 'v': '1', 'c': '2', 'g': '2', 'j': '2', 'k': '2',
                       'q': '2', 's': '2', 'x': '2', 'z': '2', 'd': '3', 't': '3', 'l': '4', 'm': '5', 'n': '5', 'r': '6'}

    # created a empty string to add the values to

    end_string = ""

    for x in deleted_string:
        if x in used_dictionary:
            end_string += used_dictionary.get(x)

    return end_string


encode_string()


"""This function will get rid of all duplcates in the string """


def get_rid_duplicates():

    rid_duplicates = encode_string()
    # created a list to add the values to to check for duplicates

    duplicates_list = []

    for x in rid_duplicates:
        duplicates_list.append(x)

    # added the if statement to handle for strings with only one value

    if len(duplicates_list) == 1:
        return "".join(duplicates_list)

    # while loop to check for adjacent values that are the same

    i = 0
    while i < len(duplicates_list):
        if duplicates_list[i] == duplicates_list[i+1]:
            duplicates_list.pop(i)
            i -= 1
        i += 1

        return "".join(duplicates_list)


get_rid_duplicates()

"""This function will combine the strings and give us a final output"""


def combine_string():

    final_word = get_rid_duplicates()

    # created an empty string to value

    zeros = ""

   # if statement to handle for notype situations (empty strings)

    if final_word is None:
        amount_zeros = 3
        print("The word encoded via the soundex system is ",
              " ".join(letter)+'000')

    # else statement that handles for all other statements adds the appropiate amount of zeros to the end
    else:
        final_word = final_word[:3]
        amount_zeros = 3 - len(final_word)
        for i in range(amount_zeros):
            zeros += '0'

        print("The word encoded via the soundex system is ",
              " ".join(letter)+final_word + zeros)


combine_string()

"""For my creative element I used the dictionary/hashmap data structure to reduce my big(O) time so that this could be used and scaled to many users without having performance issues."""

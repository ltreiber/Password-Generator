# Write a programme, which generates a random password for the user.
# Ask the user how long they want their password to be,
# and how many letters and numbers they want in their password.
# Have a mix of upper and lowercase letters, as well as numbers and symbols.
# The password should be a minimum of 6 characters long.

import random
import string

length = 0
letter_length = 0
number_length = 0
characters = string.ascii_letters + string.digits
password = ""

# Verifies that the input is an integer.
# Prints statement if the input
def set_user_inputs(number, n):
    not_integer = True
    while not_integer:
        try:
            if n == 1:
                number = int(input("How long do you want your password to be? "))
            elif n == 2:
                number = int(input("How many letters do you want in your password? "))
            else:
                number= int(input("How many numbers do you want in your password? "))
            not_integer = False
            return number
        except ValueError:
            print("This is not an integer. Please enter a number")

# Creates password
def create_password(length, letters, numbers, password , character):
    for i in range(0, length):
        password += (random.choice(character))
    return password
###

length = set_user_inputs(length, 1)
while length < 6:
    print("Length needs to be longer than 6")
    length = set_user_inputs(length, 1)

letter_length = set_user_inputs(letter_length, 2)
number_length = set_user_inputs(number_length, 3)

print("Your randomly generated password:")
print(create_password(length, letter_length, number_length, password, characters))

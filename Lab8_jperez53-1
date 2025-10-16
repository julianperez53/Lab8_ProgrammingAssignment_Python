"""This program determines the validity of the given UPC numbers.
    UPC Validity Program
    Author: Julian Perez
    Date: 10/16/2025
"""

# Function to determine the check digit using the check digit calculation formula
# https://en.wikipedia.org/wiki/Universal_Product_Code
def find_UPC():
    odd_sum = 0
    even_sum = 0
    for odd_number in upc_input[::2]:
        num = int(odd_number)
        odd_sum += num
    for even_number in upc_input[1:-2:2]:
        num = int(even_number)
        even_sum += num
    odd_sum = odd_sum * 3
    total_sum = odd_sum + even_sum
    M = total_sum % 10
    return M

# Function to validate the user's input with 2 requirements
# Requirement 1: Input is length 12
# Requirement 2: Input is comprised of all digits
def func_input_upc():
    validated = False
    good_count = 0
    while not validated:
        upc_input = input('Please input a valid UPC: ')

        while len(upc_input) != 12:
            print('Invalid UPC numbers, there are less than or more than twelve digits.')
            upc_input = input('Please input a valid UPC: ')

        for index in upc_input:
            if index.isdigit() == True:
                good_count += 1

        if good_count == 12:
            validated = True
        else:
            good_count = 0
    return upc_input

# Function that determines whether or not the check digit is the same as the last digit in given UPC, then displays validity to user
def valid_upc(digit):
    if digit != 0:
        digit = 10 - digit
    last_index = int(upc_input[-1])
    if digit == last_index:
        print(f'Because the check digit, {digit}, IS the same as the last number in the UPC-A input, {last_index}, \nThe UPC provided is valid.')
    else:
        print(f'Because the check digit, {digit}, IS NOT the same as the last number in the UPC-A input, {last_index}, \nThe UPC provided is invalid.')

# Program calling all functions to accept input, run the code, and display results before closing
finished = False
while not finished:
    upc_input = func_input_upc()
    check_digit = find_UPC()
    valid_upc(check_digit)
    finished = True

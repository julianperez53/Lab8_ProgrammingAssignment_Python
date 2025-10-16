


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


finished = False
while not finished:
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

    check_digit = find_UPC()
    if check_digit != 0:
        check_digit = 10 - check_digit
    last_index = int(upc_input[-1])
    if check_digit == last_index:
        print(f'Because the check digit, {check_digit}, IS the same as the last number in the UPC-A input, {last_index}, \nThe UPC provided is valid.')
    else:
        print(f'Because the check digit, {check_digit}, IS NOT the same as the last number in the UPC-A input, {last_index}, \nThe UPC provided is invalid.')
    finished = True

def sum_of_two_digits(first_digit, second_digit):
    return first_digit + second_digit


if __name__ == '__main__':
    # Prompt the user to enter two integers separated by a space
    a, b = map(int, input().split())

    # Call the function and print the result
    result = sum_of_two_digits(a, b)
    print(result)

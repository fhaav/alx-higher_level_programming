#!/usr/bin/python3
def print_last_digit(number):
    number = abs(number)
    # Extract the last digit using the modulo operator (%)
    last_digit = number % 10
    print(last_digit)
    return last_digit


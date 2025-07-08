import timeit as t

import math


def find_special_numbers(m, n):
    special_numbers = []

    for num in range(m, n + 1):

        if is_palindromic(num) and is_prime(num):
            special_numbers.append(num)

    return special_numbers


def is_prime(n):
    a = 2

    while a <= math.sqrt(n):

        if n % a < 1:
            return False

        a = a + 1

    return n > 1


def is_palindromic(n):
    string_n = str(n)

    return string_n == string_n[::-1]


def display_special_numbers(special_numbers):
    if len(special_numbers) < 6:

        print("All special numbers:", special_numbers)

    else:

        print("First three smallest special numbers:", special_numbers[:3])

        print("Last three largest special numbers:", special_numbers[-3:])


def main():
    m = int(input("Please enter a positive number (m): "))

    n = int(input("Please enter a bigger positive number (n): "))

    if m < 1 or n < 1:
        print("You can't enter a negative number")

    if m > n:
        print("M must be smaller than N")

    start = t.default_timer()

    special_numbers = find_special_numbers(m, n)

    print("Total number of special numbers:", len(special_numbers))

    display_special_numbers(special_numbers)

    end = t.default_timer()

    print(f"Run Time: {end - start} seconds")


if __name__ == "__main__":
    main()

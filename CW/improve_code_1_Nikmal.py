import timeit as t

import math


def find_special_numbers(m, n):
    special_numbers = []

    for length in range(len(str(m)), len(str(n)) + 1):

        palindromes = generate_palindromes(length)

        for num in palindromes:

            if m <= num <= n and is_prime(num):
                special_numbers.append(num)

    return special_numbers


def is_palindromic(n):
    return str(n) == str(n)[::-1]


def generate_palindromes(length):
    if length == 1:
        return range(1, 10)

    palindromes = []

    if length % 2 == 0:

        half_length = length // 2

        for num in range(10 ** (half_length - 1), 10 ** half_length):
            s = str(num)

            palindromes.append(int(s + s[::-1]))

    else:

        half_length = (length - 1) // 2

        for num in range(10 ** (half_length - 1), 10 ** half_length):

            s = str(num)

            for mid_digit in range(10):
                palindromes.append(int(s + str(mid_digit) + s[::-1]))

    return palindromes


def is_prime(n):
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))

    for d in range(3, max_divisor + 1, 2):

        if n % d == 0:
            return False

    return True


def display_special_numbers(special_numbers):
    if len(special_numbers) < 6:

        print("All special numbers:", special_numbers)

    else:

        print("First three smallest special numbers", special_numbers[:3])

        print("Last three largest special numbers", special_numbers[-3:])


def main():
    m = int(input("Please enter a positive number (m): "))

    n = int(input("Please enter a bigger positive number (n): "))

    if m < 1 or n < 1 or m > n:
        print("You can't enter a negative number and M must be smaller than N")

    start = t.default_timer()

    special_numbers = find_special_numbers(m, n)

    print("Total number of special numbers:", len(special_numbers))

    display_special_numbers(special_numbers)

    end = t.default_timer()

    print(f"Run time: {end - start} seconds")


if __name__ == "__main__":
    main()

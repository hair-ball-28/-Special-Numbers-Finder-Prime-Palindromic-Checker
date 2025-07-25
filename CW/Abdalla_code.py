import time


def is_prime(num, primes):
    if num < 2:
        return False

    for prime in primes:

        if prime * prime > num:
            return True

        if num % prime == 0:
            return False

    return True


def sieve_of_eratosthenes_segmented(limit):
    sieve = [True] * (limit + 1)

    sieve[0] = sieve[1] = False

    for num in range(2, int(limit ** 0.5) + 1):

        if sieve[num]:

            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False

    primes = [num for num in range(2, limit + 1) if sieve[num]]

    return primes


def is_palindrome(num):
    return str(num) == str(num)[::-1]


def find_special_numbers(m, n):
    start_time = time.time()

    sqrt_n = int(n ** 0.5) + 1

    primes = sieve_of_eratosthenes_segmented(sqrt_n)

    special_numbers = [num for num in range(m, n + 1) if is_prime(num, primes) and is_palindrome(num)]

    if len(special_numbers) <= 5:

        print(f"All {len(special_numbers)} special numbers: {special_numbers}")

    else:

        print(f"First 3 smallest special numbers: {special_numbers[:3]}")

        print(f"Last 3 biggest special numbers: {special_numbers[-3:]}")

    print(f"Total number of special numbers: {len(special_numbers)}")

    end_time = time.time()

    print(f"Runtime: {end_time - start_time:.6f} seconds")


if __name__ == "__main__":

    m = int(input("Enter the smaller number (m): "))

    n = int(input("Enter the larger number (n): "))

    if m >= n:

        print("Error: m should be smaller than n.")

    else:

        find_special_numbers(m, n)


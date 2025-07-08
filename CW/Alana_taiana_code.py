import time


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(n ** 0.5) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def find_special_numbers(m, n):
    special_numbers = [num for num in range(m, n + 1) if is_prime(num) and is_palindrome(num)]
    return special_numbers


def display_special_numbers(special_numbers, m, n):
    if len(special_numbers) < 6:
        print("All special numbers between {} and {} are: {}".format(m, n, special_numbers))
    else:
        print("First 3 smallest special numbers between {} and {} are: {}".format(m, n, special_numbers[:3]))
        print("Last 3 biggest special numbers between {} and {} are: {}".format(m, n, special_numbers[-3:]))
    print("Total number of special numbers between {} and {} is: {}".format(m, n, len(special_numbers)))


def main():
    try:
        m = int(input("Enter the lower limit (m): "))
        n = int(input("Enter the upper limit (n): "))
        if m < 0 or n < 0 or m > n:
            print("Invalid input. Please enter positive numbers with m < n.")
            return
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        return

    start_time = time.time()
    special_numbers = find_special_numbers(m, n)
    end_time = time.time()

    display_special_numbers(special_numbers, m, n)
    print("Elapsed time:", end_time - start_time, "seconds")


if __name__ == "__main__":
    main()
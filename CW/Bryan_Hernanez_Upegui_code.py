import time


# Function to check if a number is prime
def is_prime(n):

    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Function to check if a number is a palindrome
def is_palindrome(n):

    return str(n) == str(n)[::-1]


# Function to find all 'special numbers' that are both prime and palindromic within a range
def find_special_numbers(m, n):

    special_numbers = []
    for num in range(m, n + 1):
        if is_prime(num) and is_palindrome(num):
            special_numbers.append(num)
    return special_numbers


# Function to display the 'special numbers' found. If more than five, show the first and last three
def display_special_numbers(special_numbers):
    total = len(special_numbers)
    if total < 6:
        print("Total: Special Numbers =", total)
        print("List of special numbers =", special_numbers)
    else:
        print("Total: special Numbers =", total)
        print("List of special numbers =", special_numbers[:3] + special_numbers[-3:])


# Main function to drive the program
def main():
    m = int(input("Enter the lower limit (m): ")) # Prompt user for lower range
    n = int(input("Enter the upper limit (n): ")) # Prompt user for upper range
    if m > n or m < 1 or n < 1: # Check if the user has entered a valid range
        print("Invalid input. Please enter valid numbers.")
    else:
        start_time = time.time() # Record the start time
        special_numbers = find_special_numbers(m, n) # Find special numbers within the range
        display_special_numbers(special_numbers) # Display the special numbers
        end_time = time.time() # Record the end time
        print("Execution time: {:.6f} seconds".format(end_time - start_time)) # Print the execution time


if __name__ == "__main__":
    main()

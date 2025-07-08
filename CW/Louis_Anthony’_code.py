import time  # Import the time module for measuring execution time


class special_number:  # Define a class named special_number
    def __init__(self, Prime, Palindrome):
        self.prime_num = Prime
        self.palindrome = Palindrome

    def is_Prime(self, x):  # Method to check if a number is prime
        if x < 2:
            return False
        if x == 2:
            return True
        if x % 2 == 0:
            return False
        for i in range(3, int(x ** 0.5) + 1, 2):
            if x % i == 0:
                return False
        return True

    def is_Palindromic(self, x):  # Method to check if a number is palindromic
        num = str(x)
        return num == num[::-1]


m = int(input('Enter lower range number:'))  # Get lower range input from the user
n = int(input('Enter higher range number:'))  # Get higher range input from the user

start_time = time.time()  # Record the start time for performance measurement
special_numbers = []  # empty set

# used Chatgpt to help for this code
while m <= n:
    if special_number(m, m).is_Prime(m) and special_number(m, m).is_Palindromic(m):
        special_numbers.append(m)
    m += 1

print('There are', len(special_numbers), 'numbers')

if len(special_numbers) > 6:  # if statement on the amount of special numbers
    print('The first 3 special numbers are:',
          special_numbers[:3])  # this string :3 finds the first three in the empty list
    print('The last 3 special numbers are:',
          special_numbers[-3:])  # this string -3: finds the last three in the empty list
else:
    print('The special numbers are', special_numbers)

end_time = time.time()  # Record the end time for performance measurement
time_taken = end_time - start_time
print('Time taken:', time_taken, 'secs')  # Print the time taken for execution

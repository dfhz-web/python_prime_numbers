import itertools  # Import the itertools module, which provides functions to operate on iterables
import math  # Import the math module, which provides mathematical functions
import sys  # Import the sys module, which provides system-specific functions 

count_iter = itertools.count(5)  # Create an iterator that starts from 5 and increments by 1
first_ten = itertools.islice(count_iter, 20)  # Take the first 10 elements from the iterator

# filtered_iter = filter(lambda x: x % 1 == 0 and x % 2 == 0, first_ten)  # Filter the iterator to keep only numbers that are divisible by 1 and 2 (not used in this code)
filtered_iter = filter(lambda x: all(x % i != 0 for i in range(2, int(math.sqrt(x)) + 1)) and x > 1, first_ten)  # Filter the iterator to keep only prime numbers (numbers that are not divisible by any number between 2 and sqrt(x))

result_list = [i for i in filtered_iter]  # Convert the filtered iterator to a list

default = ['2', '3']  # Define a default list containing the strings '2' and '3'
result = default + result_list  # Concatenate the default list with the result list

print('Prime numbers',result)  # Print the resulting list

print('numbers that are not divisible by 5,')  # Print a separator message

results = [i for i in filter(lambda x:  x %5 !=0, itertools.islice(itertools.count(5), 10))]  # Filter the iterator to keep only numbers that are not divisible by 5, and take the first 10 elements
print(results)  # Print the resulting list
# import itertools
# [i for i in filter(lambda x: x % 5,itertools.islice(itertools.count(5),10) )]

import itertools
import math
# ## Generate an iterable of numbers starting from 5 and incrementing by 1 indefinitely

count_iter = itertools.count(5)


# #take the first ten elements from the iterable genrerated by the count_iter
first_ten = itertools.islice(count_iter, 10)


# # Use a lambda function as a filter to keep only elements tha are prime 

# # filtered_iter = filter(lambda x: x % 1 == 0 and x % 2 == 0, first_ten)
filtered_iter = filter(lambda x: all(x % i != 0 for i in range(2, int(math.sqrt(x)) + 1)) and x > 1, first_ten)
# print(filtered_iter)

# # Create a list comprehension to generate a list from the filtered iterable
result_list = [i for i in filtered_iter]

default = ['2', '3']
# # #print result
result = default + result_list

print(result)

# result = int(math.sqrt(7))
# print(result)

import itertools
print('Another Practice')

#by defatul lamba x:x%5 takes numbers that are not divisible by 5 and it prints to a list
results = [i for i in filter(lambda x: x % 5 !=0, itertools.islice(itertools.count(5), 10))]
print(results)

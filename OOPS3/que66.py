'''
66. Use each of map, filter, and reduce to fix the broken code.
from functools import reduce

# Use map to convert temperatures from Celsius to Fahrenheit
celsius_temperatures = [0, 20, 37, 100]

# Use filter to print only the odd numbers
numbers = [1, 4, 9, 16, 25, 36, 49]

# Use reduce to find the sum of these numbers
more_numbers = [10, 20, 30, 40, 50]

#Fix all three respectively
map_result = list(map(lambda c: c, celsius_temperatures))

filter_result = list(filter(lambda x: x , numbers))

reduce_result = reduce(lambda x, y: x + y, more_numbers,10)

print(map_result)
print(filter_result)
print(reduce_result)
'''

#ANSWER(fixed)

from functools import reduce
# Use map to convert temperatures from Celsius to Fahrenheit
celsius_temperatures = [0, 20, 37, 100]
map_result = list(map(lambda c: c*9/5+32, celsius_temperatures))
# Use filter to print only the odd numbers
numbers = [1, 4, 9, 16, 25, 36, 49]
filter_result = list(filter(lambda x: x%2!=0 , numbers))
# Use reduce to find the sum of these numbers
more_numbers = [10, 20, 30, 40, 50]
reduce_result = reduce(lambda x, y: x + y, more_numbers,)

print(map_result)
print(filter_result)
print(reduce_result)
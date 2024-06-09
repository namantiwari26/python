"""
87. Write a function that takes a list of integers, filters out the negative numbers, and
returns the sum of the positive numbers. Use filter to filter out the negative numbers
and reduce to sum the positive numbers.

"""

from functools import reduce

def sum_positive_numbers(int_list):
    positive_numbers = filter(lambda x: x >= 0, int_list)
    sum_of_positive = reduce(lambda x, y: x + y, positive_numbers, 0)
    return sum_of_positive

integers = [1, -2, 3, -4, 5]
result = sum_positive_numbers(integers)
print("sum of positive integers are:" ,  result)

"""
88. Write a function that takes a list of elements and an integer n, and returns a new list
with n randomly selected elements from the original list. The original list should be
shuffled before selecting the elements.

"""

import random

def selected_random_elements(original_list,n):

    shuffled_list=original_list.copy()

    random.shuffle(shuffled_list)

    selected_elements=shuffled_list[:n]

    return selected_elements,shuffled_list

original_list=[1 , 2 , 3 , 4 , 5]
n=3
selected_elements,shuffled_list=selected_random_elements(original_list,n)

print("shuffled list",shuffled_list)
print("selected elements",selected_elements)

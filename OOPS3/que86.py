'''
86. Write a function that takes a list of integers, filters out the odd numbers, and returns a
list of squares of the even numbers. Use filter to filter out the odd numbers and map
to square the even numbers                                              

'''
def squares_of_even_number(int_list):
    even_numbers=filter(lambda x: x%2==0,int_list)

    squares=map(lambda x: x**2,even_numbers)

    return list(squares)
integers = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8]
result=squares_of_even_number(integers)
print("squares of even numbers:", result) 
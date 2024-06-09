'''
85. Write a function that takes a list of tuples where each tuple contains the price and
quantity of an item. Use map to calculate the total price for each item and reduce to
calculate the grand total.
'''
from functools import reduce

def total(items):
    item_total=map(lambda item:item[0]*item[1],items)
    grand_total=reduce(lambda x,y:x+y,item_total,0)

    return grand_total

items=[(10,2),(5,3),(8,1)]
result=total(items)
print("Grand total:",result)
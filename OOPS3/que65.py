'''
65. Demonstrate each of the following with a piece of python code: lambda, zip, map,
reduce, filter, pip, pypi

'''

#lambda
addition=lambda x,y:x+y
print(addition(4,6))

#zip
list1=[1,2,3]
list2=['a','b','c']
zipped=list(zip(list1,list2))
print(zipped)

#map
list3=[1,2,3]
square=list(map(lambda x:x**2,list3))
print(square)

#reduce
from functools import reduce
list4=[1,2,3,4,5,6]
product=reduce(lambda x,y:x*y,list4)
print(product)

#filter
list5=[1,-2,3,-4,5,-6]
positive_number=list(filter(lambda x:x%2==0,list5))
print(positive_number)

#pip and pypi
'''
pip is a package installer for python, and pypi(python package index) is a repositary of software packages for python
syntax-pip install numpy
'''




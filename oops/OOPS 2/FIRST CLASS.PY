def square(x):
    print(x*x)
square(6)    

""" or u can use"""

def square(x):
    print(x*x)
result=square # we just gave another name to square to call with
result(6)

def upper_case(text):  #it is first class function   
    return text.upper()

def greet(func): #higher order funtion
    greeting=func("HI,i am function as argument")
    print(greeting)

greet(upper_case)    # a function who recieve first class function as an argument are called higer order function   

""" A program in which one function will return another function """
def sub_outer(x):
    def sub_inner(y):
        return x-y
    return sub_inner
print(result(20))
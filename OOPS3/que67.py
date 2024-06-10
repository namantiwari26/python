'''
67. Explain the following: decorators and generators, staticmethod and classmethod
decorators.
'''
#ANSWER
#DECORATORS matlab kisi bhi function ke beech hum decorators ki help se uska behaviour extend kr skte hai 

'''
1.Decorators in python are a design pattern that allow user to add new functionality 
to an existing object without modifying it's structure
'''
def my_dec(fun):
    def hi_guys():
        print("welcome to my git")
        fun()
        print("thanks for coming")
    return hi_guys    
@my_dec
def greet():
    print("hello!!") 

greet()    

#or u can just do this
#my_dec(greet)() ,by removing @my_dec and greet()
   
#i simply ,modify hi_guys by using decorators with printing hello!! in between.


#generators--its basically a better way to create an iterable sequence of value,like list but list will take time and memory but it will not
'''
2.GENERATORS are a special type of iterator in Python, used to iterate over a sequence of values. 
They allow you to declare a function that behaves like an iterator, i.e., it can be used in a for loop. 
They use the yield statement to produce a series of values lazily.,benefits of generator that they allow you to generate the values
on-the-fly
'''
def my_gen():
    for i in range(100):
        yield i


gen=my_gen() 
#print(next(gen))  
#print(next(gen))
#print(next(gen))
#print(next(gen))

for j in gen:
   print(j)


     




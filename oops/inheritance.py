#single inheritance
class A:
    def displayA(self):
        print("welcome to my code A")

class B(A):
    def displayB(self):
        print("welcome to my code B")    

obj=B()
obj.displayA()
obj.displayB()
      

#multilevel inhertance
class A:
    def displayA(self):
        print("welcome to my code A")

class B(A):
    def displayB(self):
        print("welcome to my code B")   

class C(B):
    def displayC(self):
        print("welcome to my code C")         

obj=C()
obj.displayA()    
obj.displayB()
obj.displayC()    

#MULTIPLE INHERITANCE

class A:
    def displayA(self):
        print("welcome to my code A")

class B:
    def displayB(self):
        print("welcome to my code B")   

class C(A,B):
    def displayC(self):
        print("welcome to my code C")         

obj=C()
obj.displayA()    
obj.displayB()
obj.displayC()    

 
    
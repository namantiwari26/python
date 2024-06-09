class student:
    def __init__(self):
        self.__name=""
    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name=name
        
obj=student()
obj.setname("testing")
name=obj.getname()
print(name)        
        
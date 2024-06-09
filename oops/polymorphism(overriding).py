class PT:
    def displayinfo(self):
        print("welcome to my code")
class NT(PT):
    def displayinfo(self):
        print("welcome to oops")
obj=NT()
obj.displayinfo()        
#for printing PT use super()

class PT:
    def displayinfo(self):
        print("welcome to my code")
class NT(PT):
    def displayinfo(self):
        super().displayinfo()
        print("welcome to oops")
obj=NT()
obj.displayinfo() 


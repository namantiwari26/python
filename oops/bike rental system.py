class bikeshop:

    def __init__(self,stock):
        self.stock=stock
    def displaybike(self):
        print("Total bike:",self.stock)  
    def rent_for_bike(self,q):

        if q<=0:
            print("jab leni hi nhi hai toh aya kyu maaaadrrr") 
        elif q>self.stock:
            print("bhadwe itni hai hi nhi stock meh")
        else:
            self.stock=self.stock-q
            print("Total price:",q*100) 
            print("Total bike left:",self.stock) 

while True:
    obj=bikeshop(100)
    uc=int(input("""
1 display bike
2 rentforbike
3 exit       
""" ))  
    if uc==1:
        obj.displaybike()
    elif uc==2:
        n=int(input("Enter the quantity:---"))
        obj.rent_for_bike(n)
    else:
        break

      
    
                        


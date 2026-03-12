class Car:
    # constructor
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    # method
    def drive(self):
        print(self.brand,f"is my dream car and {self.color} in color")

# create object
car1=Car("Lexus","Black")
car1.drive()
car2=Car("Mazda","white")
car2.drive()
car3=Car("Subaru","grey")
car3.drive()
car4=Car("Wagon","yellow")
car4.drive()
car5=Car("Toyota","brown")
car5.drive()
car6=Car("Mercedes","maroon")
car6.drive()

# create a class called fruits
# it should have three attributes
# type, color, price
# a method claade display(), then intance of that class(object)
# print it six times

class Fruit:
    # constructor
    def __init__(self,type,color,price):
        self.type=type
        self.color=color
        self.price=price

    # method
    def display(self):
        print(self.type,f" is {self.color} and it costs {self.price}")   
# create object
fruit1=Fruit("Mango","yellow","ksh.30")
fruit1.display()
fruit2=Fruit("Banana","grenish","ksh.50")
fruit2.display()
fruit3=Fruit("Apple","red","ksh.90")
fruit3.display()
fruit4=Fruit("Lemon","green","ksh.100")
fruit4.display()





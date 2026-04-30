class dog:
    attr1="Puppy"
    attr2="Snoopy"
    def display(self):
        print("this is ",self.attr1)
        print("this is ",self.attr2)
tommy=dog()
print(tommy.attr1)
tommy.display()
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("this is a person class")
    
    def classinfo(self):
        
        print("Name : ",self.name)
        print("Age : ",self.age)
p=person("Kartheek",18)
p.classinfo()


RED = "\033[38;5;255;48;5;0m"
GREEN = "\033[38;5;266;48;5;0m"
YELLOW = "\033[38;5;226;48;5;0m"
MAGENTA = "\033[38;5;129;48;5;0m"
RESET = "\033[0m"

class car:
    def __init__(self,brand,model,cost,colour):
        self.brand=brand
        self.model=model
        self.cost=cost
        self.colour=colour
        print(MAGENTA + "THIS IS A CAR CLASS" + RESET)

    def carinfo(self):
        print(GREEN + "Brand : " + RESET, self.brand)
        print(YELLOW + "Model : " + RESET, self.model)
        print(RED + "Cost : " + RESET, self.cost)
        print(MAGENTA + "Colour : " + RESET, self.colour)
for i in range(2):
    Brand=input(MAGENTA + "ENTER THE BRAND OF THE CAR %d:"%(i+1)+RESET)
    Model=input(MAGENTA + "ENTER THE MODEL OF THE CAR %d:"%(i+1)+RESET)
    Cost=int(input(MAGENTA + "ENTER THE COST OF THE CAR %d:"%(i+1)+RESET))
    Colour=input(MAGENTA + "ENTER THE COLOUR OF THE CAR %d:"%(i+1)+RESET)

    c=car(Brand,Model,Cost,Colour)
    c.carinfo()
class display:
    def __init__(self,name):
        self.name=name
d=display("HI")
print(d)
class display1:
    def __init__(self):
        self.name="HELLO"
    
d1=display1()
print(d1.name)
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("this is a person class")
    
    def classinfo(self):
        
        print("Name : ",self.name)
        print("Age : ",self.age)
p=person("Kartheek",18)
p.classinfo()


RED = "\033[38;5;255;48;5;0m"
GREEN = "\033[38;5;266;48;5;0m"
YELLOW = "\033[38;5;226;48;5;0m"
MAGENTA = "\033[38;5;129;48;5;0m"
RESET = "\033[0m"

class car:
    def __init__(self,brand,model,cost,colour):
        self.brand=brand
        self.model=model
        self.cost=cost
        self.colour=colour
        print(MAGENTA + "THIS IS A CAR CLASS" + RESET)

    def carinfo(self):
        print(GREEN + "Brand : " + RESET, self.brand)
        print(YELLOW + "Model : " + RESET, self.model)
        print(RED + "Cost : " + RESET, self.cost)
        print(MAGENTA + "Colour : " + RESET, self.colour)
for i in range(2):
    Brand=input(MAGENTA + "ENTER THE BRAND OF THE CAR %d:"%(i+1)+RESET)
    Model=input(MAGENTA + "ENTER THE MODEL OF THE CAR %d:"%(i+1)+RESET)
    Cost=int(input(MAGENTA + "ENTER THE COST OF THE CAR %d:"%(i+1)+RESET))
    Colour=input(MAGENTA + "ENTER THE COLOUR OF THE CAR %d:"%(i+1)+RESET)

    c=car(Brand,Model,Cost,Colour)
    c.carinfo()
class display:
    def __init__(self,name):
        self.name=name
d=display("HI")
print(d)
class display1:
    def __init__(self):
        self.name="HELLO"
    
d1=display1()
print(d1.name)
class Calculator:
    total:float = 0.0
    brand:str = "sony"

    def __init__ (self,c):
        self.total = c
    def add(a:float,b:float):
        return a + b
    
mom:Calculator = Calculator(30.00)
son:Calculator = Calculator(10.00)
daughter:Calculator = Calculator(20.00)
dad:Calculator = Calculator(50.00)

print(Calculator.brand)

print(son.brand) #we know an instance has access to class variable
print(mom.brand)
mom.brand = "Apple"
print(mom.brand)


'''
Same scenario but only using class function and class variable"
'''

class Calculator_class:
    total:float = 0.0
    brand:str = "sony"
    @classmethod
    def add (cls,i:float,j:float):
        return i + j
    @classmethod
    def subtract (cls,i:float,j:float):
        return i - j
    @classmethod
    def update (cls,num:float):
        total = num 
        print(total)
print(Calculator_class.total)
print(Calculator_class.add(2,3))
print(Calculator_class.subtract(3,2))
Calculator_class.total = 10.1
print(Calculator_class.total)
Calculator_class.update(50.50)
print(Calculator_class.total)

#mom:Calculator_class = Calculator_class() won't work cuz there's no contructor call inside the class
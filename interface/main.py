from abc import ABC, abstractmethod

class Animal(ABC):
    EYES:int = 2
       
    @abstractmethod 
    def noise(self) -> str:
        pass
    
    @abstractmethod
    def sum(x:int, y:int) -> int:
        pass
        
        
class Dog (Animal):
    legs:int = 0
    voice:str = ""
    
    def __init__(self, l:int, v:str):
        self.legs =l
        self.voice = v
    
    def walk(self):
        return 'run'    
    
    def noise(self) -> str:  # Method is overridden here
        return 'woof'
    
    def sum(self, x:int, y:int) -> int:  # Method is overridden here
        return x + y + 1
    
    
    
d1:Dog = Dog (1, 'bark')
print(d1.walk())
print(d1.noise())
print(d1.sum(2,4))


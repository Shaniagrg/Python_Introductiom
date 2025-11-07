from abc import ABC, abstractmethod

class Animal(ABC):
    legs:int = 0
    def __init__(self, l):
        self.legs = l
        
    @abstractmethod
    def noise(self) -> str:
        pass
    
    @abstractmethod
    def move(self) -> str:
        pass
    
    @classmethod
    def test(cls) -> str:
        return 'test'
        
        
class Dog (Animal):
    breed:str = ""
    
    def __init__(self, l:int, b:str):
        super().__init__(l)
        self.breed = b
        
    def noise(self) -> str:
        return 'woof'
    
    def move(self) -> str:
        return 'run'
    
    def walk(self):
        return f'Dog walks {super().move()}'
    
d1:Dog = Dog (1, 'BullDog')
print(d1.move())
print(d1.noise())
print(d1.test())


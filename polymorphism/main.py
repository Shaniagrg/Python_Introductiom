class Animal:
    def __init__(self,l:int):
        self.legs = l
    
    def noise(self) -> str:
        return "some noise"
    
class Dog(Animal):
    def __init__(self,l:int):
        super().__init__(l)
    def noise(self) -> str:
        return "woof"
    def move(self)->str:
        return "run"
    
d1:Dog = Dog(1)
print(d1.noise())
d2:Animal = Dog(4)
print(d2.noise())
print(d2.move())
d3:Dog = Dog(d2)
print(d3.move())

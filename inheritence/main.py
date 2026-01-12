class Animal:
    def __init__(self,l:int):
        self.legs = l
    
    def speak(self) -> str:
        return "howl"
    def getLegs(self) -> int:
        return self.legs
    def test(self)->str:
        return "test"
    
class Dog(Animal):
    def __init__(self,l:int):
        super().__init__(l)
    def speak(self)->str:
        return "woof"
    
d1:Dog = Dog(4)
print(d1.getLegs())
print(d1.speak())
print(d1.test())
    
        
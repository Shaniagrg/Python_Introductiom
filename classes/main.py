class Bank:
    checking:float = 0.0
    saving:float = 0.0 
    def __init__ (self,c:float,s:float):
        self .checking = c
        self.saving = s

#Bank CA = new CA (10.00,20.00)

CA:Bank = Bank(10.00,20.00)


class Person:
  def __init__(self, n, a):
    self.name = n
    self.age = a

  def __str__(self):
    return f"{self.name}({self.age})"    

p1:Person = Person("John", 36)

print(p1)
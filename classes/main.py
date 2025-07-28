
class Bank:
    checking:float = 0.0
    saving:float = 0.0 
    def __init__ (self,c:float,s:float):
        self .checking = c
        self.saving = s

#Bank CA = new CA (10.00,20.00)

CA:Bank = Bank(10.00,20.00)


class Person:
  '''
  Person()
    this.name = n
    this.name = a
  but instead in python we write __init__ and self for constructor
  '''
  def __init__(self, n, a):   #we usually write Person() but in python the CONSTRUCTOR is calle by __init__
    self.name = n             # self is always in the parameter inside class which also refer to this.name = n
    self.age = a

  def __str__(self):
    return f"{self.name}({self.age})"    

p1:Person = Person("John", 36)

print(p1)

#Homework 1
class Example:
  cv:str = "I'm class variable"
  iv:str = ""
  def __init__(self):
     self.iv = "I'm instance variable"
  @classmethod     #to call class function we usually use static function cm{...} but in python you call a DECLATOR @classmethod
  def cm(cls):     #use cls as parameter always
     print("This is class function")
  def im(self):
     print("This is instance function.")

'''
Example obj = new Example()
we studies this way but will skip new in python
'''
obj:Example = Example()

print(obj.cv)
print(obj.iv)

obj.cm()
obj.im()

#Example.im() Throw error cuz class don't have access to instance FUNCTION
#print(Example.iv) Throw error cuz class don't have access to instance VARIABLE

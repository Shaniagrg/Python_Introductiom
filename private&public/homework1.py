class Account:
    __accountNum:int = 0
    name:str = ""
    
    def __init__(self, acn:int, n:str):
        self.__accountNum = acn
        self.name = n
    
    def getAccountNum(self) -> int:
        return self.__accountNum
    
a1:Account = Account (1234, "Tom")
# print (a1.accountNum) THROW ERRROR cuz a1 is directly accessing private variable which is not applicable.
print(a1.name)
print(a1.getAccountNum()) # a private variable is only accessed through function
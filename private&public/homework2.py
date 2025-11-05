class Village:
    land:int = 0
    __house:str = "" # __ represents private
    
    def __init__(self,l:int, h:str):
        self.land = l
        self.__house = h
    
    def __home_owner(self) -> str: #also private
        return self.__house        #call private using function

    def mortgage(self) -> str:
        return self.__home_owner()   #call private using function
        
v1:Village = Village(40,"This is Tom House.")
print (v1.mortgage())
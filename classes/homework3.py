class Ex:
    one:int = 0
    two:int = 0

    def __init__(self):
        self.two = 10
        self.loop()
        self.one = 23
        self.one_one()
        '''
        Won't work 
            - EX.one_one()
            - Ex.one
            - Ex.loop()
            - Ex.two_two
        Cuz in constructor we only use for INSTANCES not Class
        '''
    
    @classmethod
    def one_one(cls):
        print(Ex.one)
        '''
        Works BUT
            - self.one
        Try to use class variable or function in class function and via
        '''
    def two_two(self):
        print(self.one)
        '''
        Works BUT
            - Ex.one_one() 
            - self.one_one()
        Again use instance variable or funtion in instance function and via
        '''
    def loop(self):
        for i in range(0,2,1):
            print(self.two)

obj:Ex = Ex()
print(f"First value: {obj.one}")
obj.one = 1
obj.two_two()
obj.one_one()

Ex.one_one()
print(f"This is class one {Ex.one}")
print(obj.one)
print(obj.two)
        
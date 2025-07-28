class Seats:
    material:str = ""
    softess:str = ""
    s_count:int = 0

    def __init__(self,m:str="velvet", s:str = "standard", sc:int=0):
        self.material = m
        self.softess = s
        self.s_count = sc

class Tire:
    shape:str = ""
    grip:str = ""
    t_count:int = 0

    def __init__(self,s:str="round", g:str = "tight", tc:int=0):
        self.shape = s
        self.girp = g
        self.t_count = tc

class Vehicle:
    brand:str = "samsung"
    Tire.tire = None #None cuz its dynamic for dynamic array it's [], map {} but for class its None
    Seats.seats = None
    max_speed:float = 0.0

    def __init__(self, shape:str, grip:str, t_count:int, material:str, softness:str, s_count:int, speed:int):
        self.tire = Tire(s=shape, g=grip, tc=t_count)
        self.seats = self.type_vehicle(material,softness,s_count)
        self.max_speed = speed

    def type_vehicle(self,material,softness,s_count):
        return Seats(m=material, s= softness, sc = s_count)
        

aeroplane:Vehicle = Vehicle("circle","tight",8,"leather","normal",104,120)
bike:Vehicle = Vehicle("circle","rectangle",2,"leather","hard",2,30)
    
#Pair doesn't represent array BUT have Index
#It contains exactly two elements
#often used to represent a relationship between two values, such as coordinates in a 2D space (e.g., (x, y))
#unchangebale or immutable 

a:tuple[int,int] = (1,2)
print(a)

b:tuple[list[int]] = ([9,2],[2,4],[3,7])      #[(9,2),(2,4),(3,7)]
print(b)

c:tuple[str,int] = ('hi',2)
print(c)

d:tuple[str,str] = ('hi','arie')
print(d)

e:tuple[float,int] = (2.6,4)
print(e)

f:tuple[float,str] = (3.54,'hi')
print(f)


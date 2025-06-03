#list AKA array stored in []

x:list[int]= [1,2,4,8,2,8]
print(x[4])
print(x)

y:list[str]= ['hi','singer','dancer','learner']
print(y[1])
print(y)

r:list[list[int]]= [[4,2,6],[6,2,9],[8,3,5]]
print(r[0][0])  

a:list[int] = [1,3,5,4+3] #using some mathematical equation using +
print(a)  #prints [1, 3, 5, 7]

# Type Convert list()
aa:set[int] = list({3,4,5,6})

#dynamic 
bb:list[str] = []
#Everytime you wan to store data you can simply push to bb like bb.append(SOME VARIABLE or Value)

'''
Get the sum of the row
eg: [[4,1],[5,2],[6,3]]
ans: 5,7 & 9
'''
a:list[int] = [[4,1],[5,2],[6,3]]
x:int = 0
y:int = 0
z:int = 0

for i in range(len(a[0])):  #len(a[0])
    x = x + a[0][i]
          
print(x)

for ind in range(len(a[1])):
    y = y + a[1][ind]

print(y)

for index in range(len(a[2])):
    z = z + a[2][index]
    
print(z)
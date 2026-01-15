'''
Get sum of the column
eg: [[4,1],[5,2],[6,3]]
ans: 15 & 6
'''
a:list[int] = [[4,1],[5,2],[6,3]]
x:int = 0
y:int = 0

for i in range(len(a)):
    x = x + a[i][0]
          
print(x)

for i in range(len(a)):
    y = y + a[i][1]

print(y)
       


'''
Get product of an array
eg: [1,2,3,4,5]
ans: 120
'''

a:list[int] = [1,2,3,4,5]
x:int = 1

for i in range(len(a)):
    x = x * a[i]
    
print(x)
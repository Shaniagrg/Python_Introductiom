'''
Get the sum of the array
eg: [1,3,4,8,3]
ans: 19
'''

a:list[int] = [1,3,4,8,3]
x:int = 0
for i in range(len(a)):
    x = x + a[i]

print(x)


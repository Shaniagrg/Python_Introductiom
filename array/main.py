'''
Find the largest element in the array
Eg: [1,3,6,2]
ans: 6
'''
a:list[int] = [1,3,6,2]

x:int = 0

for i in range(len(a)):
    if x < a[i]:
        x = a[i]

print(x)
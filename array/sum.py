'''
Get the sum of the array
eg: [1,3,4,8,3]
ans: 19
'''
def sum (a:list[int]) -> int:
    x:int = 0
    for i in range(len(a)):
        x = x + a[i]
    return x
            
def addTest(expected:int, actual:int) -> str:
    if expected == actual:
        return "correct"

    else:
        return "incorrect, addition is wrong"

print(addTest(19, sum([1,3,4,8,3])))
print(addTest(6, sum([3,3])))


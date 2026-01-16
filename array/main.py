'''
Find the largest element in the array
Eg: [1,3,6,2]
ans: 6
'''

def highest_value (a:list[int]) -> int:
    x:int = 0
    for i in range(len(a)):
        if x < a[i]:
            x = a[i]
    return x
def highest_valueTest(expected:int, actual:int):
    if expected == actual:
        return "correct"

    else:
        return "incorrect, addition is wrong"

print(highest_valueTest(6, highest_value([1,3,6,2])))
print(highest_valueTest(4, highest_value([1,3,4])))

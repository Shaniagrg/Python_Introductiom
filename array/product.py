'''
Get product of an array
eg: [1,2,3,4,5]
ans: 120
'''

def product (a:list[int]) -> int:
    total:int = 1
    for product in range(len(a)):
        total = total * a[product]
    return total
 
def productTest(expected:int, actual:int) -> str:
    if expected == actual:
        return "correct"

    else:
        return "incorrect, addition is wrong"

print(productTest(120, product([1,2,3,4,5])))
print(productTest(1, product([1,1,1,1])))
print(productTest(0, product([1,2,3,4,5,0])))

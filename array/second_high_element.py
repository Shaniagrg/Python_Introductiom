'''
Find the largest element in the array
Input: nums = [8, 8, 7, 6, 5]
Output: 7
'''

def second_highest_value (a:list[int]) -> int:
    
    large:int = float('-inf')
    second_large:int = float('-inf')
    n:int = len(a)
    
    if n < 2:
        return -1
    
    for i in range(n):
        # Update the largest and second largest values
        if a[i] > large:
            second_large = large
            large = a[i]
        elif a[i] > second_large and a[i] != large:
            second_large = a[i]
            
    print(second_large)
    return second_large

def highest_valueTest(expected:int, actual:int) -> str:
    if expected == actual:
        return "correct"

    else:
        return "incorrect, the value isn't the second largest"

print(highest_valueTest(7, second_highest_value([8, 8, 7, 6, 5])))
print(highest_valueTest(4, second_highest_value([1,3,4,8])))
print(highest_valueTest(-2, second_highest_value([-5,-2,0])))

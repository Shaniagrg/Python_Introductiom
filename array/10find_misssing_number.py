'''
Given an integer array of size n containing distinct values in the range from 0 to n (inclusive), 
return the only number missing from the array within this range.


Example 1
Input: nums = [0, 2, 3, 1, 4]
Output: 5

Explanation:
nums contains 0, 1, 2, 3, 4 thus leaving 5 as the only missing number in the range [0, 5]
'''
''''
My solution

def missing_number (a:list[int]) -> int:
    a.sort()
    x:int = 0
    
    for i in range(len(a)):
        if i == a[i]:
            continue
        else:
            x = i
    print(a)
    print(x)
    return x

def missing_numberTest(expected:int, actual:int) -> str:
    if expected == actual:
        return "correct"

    else:
        return "incorrect, the number exist"

print(missing_numberTest(5, missing_number([0,2,3,1,4])))
print(missing_numberTest(3, missing_number([0,1,2,4,5,6])))
print(missing_numberTest(-3, missing_number([-1,-5,-2,-4,0])))
'''


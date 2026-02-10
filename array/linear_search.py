'''
Given an array of integers nums and an integer target, 
find the smallest index (0 based indexing) where the target appears in the array. 
If the target is not found in the array, return -1


Example 1
Input: nums = [2, 3, 4, 5, 3], target = 3
Output: 1
Explanation:    
The first occurence of 3 in nums is at index 1
'''

def linear_search (a:list[int], target:int) -> int:
    x:int = 0
    used_value:list[int] = set()
    for i in range(len(a)):
        if a[i] in used_value:
            continue
        elif target not in a:
            x = -1
        elif target == a[i]:
            used_value.add(a[i])
            x = i
            break
        
    print(x)
    return x

def linear_searchTest(expected:int, actual:int) -> str:
    if expected == actual:
        return "correct"

    else:
        return "incorrect, addition is wrong"

print(linear_searchTest(1, linear_search([1,3,6,2], 3)))

print(linear_searchTest(2, linear_search([1,3,4], 4)))
print(linear_searchTest(0, linear_search([-1,-5,-2], -1)))
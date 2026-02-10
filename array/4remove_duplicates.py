'''
Given an integer array nums sorted in non-decreasing order, 
remove all duplicates in-place so that each unique element appears only once.

Return the number of unique elements in the array.

Example 1

Input: nums = [0, 0, 3, 3, 5, 6]
Output: 4
Explanation:
Resulting array = [0, 3, 5, 6, _, _]

'''

def remove_duplicate (a:list[int]) -> list[int]:
    if not a:
        return []

    result: list[int] = []

    for num in a:
        if num not in result:
            result.append(num)

    return result

def remove_duplicateTest(expected:list[int], actual:list[int]) -> str:
    if expected == actual:
        return "correct"

    else:
        return "incorrect, there is duplicate element"

print(remove_duplicateTest([1,3,6,2], remove_duplicate([1,3,3,6,1,2])))
print(remove_duplicateTest([1,3,4], remove_duplicate([1,3,4,3,3,1,4])))
print(remove_duplicateTest([-1,-5,-2,-3,0], remove_duplicate([-1,-5,-2,-3,0,0,-2])))

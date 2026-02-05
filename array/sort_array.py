'''
Given an array nums of n integers, return true if the array nums is sorted in non-decreasing order or else false.

Example 1

Input : nums = [1, 2, 3, 4, 5]

Output : true

Explanation : For all i (1 <= i <= 4) it holds nums[i] <= nums[i+1], hence it is sorted and we return true.

'''

def sort (array:list[int]) -> str:
    
    for i in range(1, len(array)):
        
        if array[i] < array[i - 1]:  # If any element is smaller than the previous one, return false
            return 'false'
    return 'true'
            

def highest_valueTest(expected:str, actual:str) -> str:
    if expected == actual:
        return "correct"

    else:
        return "incorrect, the element aren't sorted"

print(highest_valueTest('false', sort([1,3,6,2])))
print(highest_valueTest('true', sort([1,1,1,3,4])))
print(highest_valueTest('true', sort([-6,-5,-2])))

'''
Given an integer array nums, rotate the array to the left by one.

Input: nums = [1, 2, 3, 4, 5]
Output: [2, 3, 4, 5, 1]

Explanation:
Initially, nums = [1, 2, 3, 4, 5]
Rotating once to left -> nums = [2, 3, 4, 5, 1]
'''


a:list[int] = [1, 2, 3, 4, 5]
left_rotate:list[int] = []

for i in range(len(a)):
    if i == 4:
        left_rotate.append(a[0])
    else:   
        left_rotate.append(a[i+1])

print(left_rotate)
    


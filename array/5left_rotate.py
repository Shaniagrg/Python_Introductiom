'''
Given an integer array nums, rotate the array to the left by one.

Input: nums = [1, 2, 3, 4, 5]
Output: [2, 3, 4, 5, 1]

Explanation:
Initially, nums = [1, 2, 3, 4, 5]
Rotating once to left -> nums = [2, 3, 4, 5, 1]
'''

'''
My Solution

a:list[int] = [1, 2, 3, 4, 5]
left_rotate:list[int] = []

for i in range(len(a)):
    length:int = len(a) - 1
    if i == length:
        left_rotate.append(a[0])
    else:   
        left_rotate.append(a[i+1])

print(left_rotate)
'''

def rotate_array_by_one(nums: list[int]) -> None:
    if not nums:
        return

    temp = nums[0]

    for i in range(1, len(nums)):
        nums[i - 1] = nums[i]

    nums[-1] = temp


def rotate_array_by_one_test(expected: list[int], actual: list[int]) -> str:
    if expected == actual:
        return "correct"
    else:
        return f"incorrect expected {expected}, got {actual}"


# ---------------- TEST CASES ----------------

nums1 = [1, 2, 3, 4, 5]
rotate_array_by_one(nums1)
print(rotate_array_by_one_test([2, 3, 4, 5, 1], nums1))

nums2 = [10, 20, 30]
rotate_array_by_one(nums2)
print(rotate_array_by_one_test([20, 30, 10], nums2))

nums3 = [7]
rotate_array_by_one(nums3)
print(rotate_array_by_one_test([7], nums3))



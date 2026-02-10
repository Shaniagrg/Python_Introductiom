'''
Given an integer array nums and a non-negative integer k, rotate the array to the left by k steps.

Example 1
Input: nums = [1, 2, 3, 4, 5, 6], k = 2
Output: nums = [3, 4, 5, 6, 1, 2]
Explanation:
rotate 1 step to the left: [2, 3, 4, 5, 6, 1]
rotate 2 steps to the left: [3, 4, 5, 6, 1, 2]
'''

'''
a:list[int] = [1, 2, 3, 4, 5, 6]
d_rotate:list[int] = []
pointer:int = 2
replace:int = 0

for i in range(len(a)):
    if pointer == i:
        d_rotate.append(a[pointer])
        pointer = pointer + 1
    else:
        d_rotate.append(a[replace])
        replace = replace + 1
        
print(d_rotate)
'''

def reverse(nums: list[int], start: int, end: int) -> None:
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start = start + 1
        end = end - 1


def rotate_array(nums: list[int], k: int, direction: str) -> list[int]:
    n = len(nums)

    if n == 0 or k == 0:
        return nums

    k = k % n

    if direction == "right":
        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)

    elif direction == "left":
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)
        reverse(nums, 0, n - 1)

    return nums


def rotate_array_test(expected: list[int], actual: list[int]) -> str:
    if expected == actual:
        return "correct"
    else:
        return f"incorrect expected {expected}, got {actual}"
    
# ---------------- TEST CASES ----------------

nums1 = [1, 2, 3, 4, 5, 6, 7]
rotate_array(nums1, 2, "right")
print(rotate_array_test([6, 7, 1, 2, 3, 4, 5], nums1))

nums2 = [1, 2, 3, 4, 5, 6, 7]
rotate_array(nums2, 2, "left")
print(rotate_array_test([3, 4, 5, 6, 7, 1, 2], nums2))

nums3 = [1, 2, 3]
rotate_array(nums3, 4, "right")
print(rotate_array_test([3, 1, 2], nums3))

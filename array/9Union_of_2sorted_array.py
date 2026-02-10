'''
Given two sorted arrays nums1 and nums2, 
return an array that contains the union of these two arrays. 
The elements in the union must be in ascending order.

The union of two arrays is an array where all values are distinct 
and are present in either the first array, the second array, or both.


Example 1
Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 7]
Output: [1, 2, 3, 4, 5, 7]

Explanation:
The elements 1, 2 are common to both, 3, 4, 5 are from nums1 and 7 is from nums2
'''

def sort_array (nums1:list[int], nums2:list[int]) -> int:
    length:int = 0
    x:list[int] = set()
    
    if len(nums1) > len(nums2):
        length = len(nums1)
    else:
        length = len(nums2)
        
    for i in range(length):
        if nums1[i] in x and nums2[i] in x:
            continue
        elif nums1[i] == nums2[i]:
            x.add(nums1[i])
        else:
            x.add(nums1[i])
            x.add(nums2[i])
            


def sort_arrayTest(expected:list[int], actual:list[int]) -> str:
    if expected == actual:
        return "correct"

    else:
        return "incorrect, it's not sorted"

print(sort_arrayTest([1,2,3,4,5,7], sort_array(nums1=[1, 2, 3, 4, 5], nums2=[1, 2, 7])))

print(sort_arrayTest([1,3,4,5,6,7], sort_array(nums1=[1,3,4], nums2=[5,6,7])))
print(sort_arrayTest([-1,-5,-2], sort_array(nums1=[-1], nums2=[-1,-5,-2])))
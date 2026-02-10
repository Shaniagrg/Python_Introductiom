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
'''
My solution

def sort_array (nums1:list[int], nums2:list[int]) -> int:
    
    x:list[int] = set()
    
    for i in range(len(nums1)):
            x.add(nums1[i])
    
    for i in range(len(nums2)):
            x.add(nums2[i])
    print(x)
    return sorted(list(x)) #sorted cuz set stores randomly
 

def sort_arrayTest(expected:list[int], actual:list[int]) -> str:
    if expected == actual:
        return "correct"

    else:
        return "incorrect, it's not sorted"

print(sort_arrayTest([1,2,3,4,5,7], sort_array(nums1=[1, 2, 3, 4, 5], nums2=[1, 2, 7])))

print(sort_arrayTest([1,3,4,5,6,7], sort_array(nums1=[1,3,4], nums2=[5,6,7])))
print(sort_arrayTest([-5,-2,-1], sort_array(nums1=[-1], nums2=[-1,-5,-2])))

'''

#union: combine 2 array but u don't repeat any element

class Solution:
    # Function to find union of two sorted arrays using two pointers
    def findUnion(self, arr1, arr2, n, m):
        # List to store union elements
        Union = []

        # Initialize pointers
        i, j = 0, 0

        # Iterate while both pointers are within array bounds
        while i < n and j < m:
            # If element in arr1 is smaller
            if arr1[i] < arr2[j]:
                # Add if empty or not duplicate
                if not Union or Union[-1] != arr1[i]:
                    Union.append(arr1[i])
                i += 1
            # If element in arr2 is smaller
            elif arr2[j] < arr1[i]:
                # Add if empty or not duplicate
                if not Union or Union[-1] != arr2[j]:
                    Union.append(arr2[j])
                j += 1
            else:
                # Elements are equal, add once if not duplicate
                if not Union or Union[-1] != arr1[i]:
                    Union.append(arr1[i])
                i += 1
                j += 1

        # Append remaining elements from arr1
        while i < n:
            if not Union or Union[-1] != arr1[i]:
                Union.append(arr1[i])
            i += 1

        # Append remaining elements from arr2
        while j < m:
            if not Union or Union[-1] != arr2[j]:
                Union.append(arr2[j])
            j += 1

        # Return the union list
        return Union


# Driver code
if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr2 = [2, 3, 4, 4, 5, 11, 12]
    n, m = len(arr1), len(arr2)

    obj = Solution()
    result = obj.findUnion(arr1, arr2, n, m)
    print("Union of arr1 and arr2 is:", *result)
'''
You are given a string num, representing a large integer. 
Return the largest-valued odd integer (as a string) that is a non-empty substring of num, 
or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
'''
''''
My solution
-------------------- THOUGHT PROCESS ---------------------------

Convert string to int and append to odd_numbers
Then choose the largest from the odd numbers

---------------------------------------------------------------

class Solution:
    def largestOddNumber(self, num: str) -> str:
        odd_numbers:list[int] = []
        largest_odd:int = 0
        for i in range(len(num)):
            if int(num[i]) % 2 == 1:
                odd_numbers.append(int(num[i]))
        for j in range(len(num)):
            print(odd_numbers)
                
            if odd_numbers[j] > largest_odd:
                largest_odd = odd_numbers[j]
            elif len(odd_numbers) == 1:
                return str(odd_numbers[j])
        return str(largest_odd)

sol = Solution()
print(sol.largestOddNumber("52"))
'''

class Solution:
    # Function to find the largest odd number that is a substring of given string 
    def largeOddNum(self, s: str) -> str:
        ind = -1
        
        # Iterate through the string from the end to beginning
        i = 0
        for i in range(len(s) - 1, -1, -1):
            # Break if an odd digit is found
            if (int(s[i]) % 2) == 1:
                ind = i
                break
        
        # Skipping any leading zeroes
        i = 0
        while i <= ind and s[i] == '0':
            i += 1
        
        # Return the largest odd number substring
        return s[i:ind + 1]
    
    def largeOddNum_Test(self, expected:str, actual:str):
        if expected == actual:
            return "correct"

        else:
            return "incorrect, it is not the largest odd"
        

# Driver code
solution1 = Solution()
num1:str = "504"
print(solution1.largeOddNum(s=num1))
print(solution1.largeOddNum_Test("5", solution1.largeOddNum(s=num1)))


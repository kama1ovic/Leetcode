# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -231 <= x <= 231 - 1
 

# Follow up: Could you solve it without converting the integer to a string?


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Step 1: Check if x is negative or ends with 0 (but not 0 itself)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_number = 0
        while x > reversed_number:
            # Step 2: Extract the last digit and build the reversed number
            reversed_number = reversed_number * 10 + x % 10
            x //= 10  # Remove the last digit from x
        
        # Step 3: Compare the original number with the reversed number
        # For odd-length numbers, we can ignore the middle digit by reversed_number // 10
        return x == reversed_number or x == reversed_number // 10
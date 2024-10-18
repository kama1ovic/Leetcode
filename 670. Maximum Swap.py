# You are given an integer num. You can swap two digits at most once to get the maximum valued number.

# Return the maximum valued number you can get.


# Example 1:

# Input: num = 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.

# Example 2:

# Input: num = 9973
# Output: 9973
# Explanation: No swap.
 

# Constraints:
# 0 <= num <= 108

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = list(str(num))  # Convert to a list of digits for easier swapping
        n = len(num_str)

        # Find the last occurrence of each digit (0-9)
        last_occur = [-1] * 10  
        for i in range(n):
            last_occur[int(num_str[i])] = i

        # Iterate through the digits
        for i in range(n):
            # Check if there is a larger digit to the right
            for j in range(9, int(num_str[i]), -1):
                if last_occur[j] > i:
                    # Swap if found
                    num_str[i], num_str[last_occur[j]] = num_str[last_occur[j]], num_str[i]
                    return int("".join(num_str)) # Return immediately after swapping

        # No swap needed
        return num

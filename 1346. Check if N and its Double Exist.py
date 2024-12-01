# Given an array arr of integers, check if there exist two indices i and j such that:
# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]


# Example 1:

# Input: arr = [10, 2, 5, 3]
# Output: true
# Explanation: For
# i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]


# Example 2:

# Input: arr = [3, 1, 7, 11]
# Output: false
# Explanation: There is no i and j that satisfy the conditions.

# Constraints:
# 2 <= arr.length <= 500
# -10^3 <= arr[i] <= 10^3


class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen = {}

        for i, x in enumerate(arr):
            if 2 * x in seen or (x % 2 == 0 and x // 2 in seen):
                return True
            seen[x] = True

        return False
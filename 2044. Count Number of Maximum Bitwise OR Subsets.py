# Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.

# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. Two subsets are considered different if the indices of the elements chosen are different.

# The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).

 

# Example 1:

# Input: nums = [3,1]
# Output: 2
# Explanation: The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:
# - [3]
# - [3,1]
# Example 2:

# Input: nums = [2,2,2]
# Output: 7
# Explanation: All non-empty subsets of [2,2,2] have a bitwise OR of 2. There are 23 - 1 = 7 total subsets.
# Example 3:

# Input: nums = [3,2,1,5]
# Output: 6
# Explanation: The maximum possible bitwise OR of a subset is 7. There are 6 subsets with a bitwise OR of 7:
# - [3,5]
# - [3,1,5]
# - [3,2,5]
# - [3,2,1,5]
# - [2,5]
# - [2,1,5]
 

# Constraints:

# 1 <= nums.length <= 16
# 1 <= nums[i] <= 105

class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_or = 0
        
        # Step 1: Calculate the maximum bitwise OR
        for num in nums:
            max_or |= num
        
        # Step 2: Count subsets that yield the maximum bitwise OR
        count = 0
        n = len(nums)
        
        # There are 2^n subsets, we can use bitmasking to generate them
        for mask in range(1, 1 << n):  # from 1 to 2^n - 1
            current_or = 0
            for i in range(n):
                if mask & (1 << i):  # if the i-th bit is set in mask
                    current_or |= nums[i]
            if current_or == max_or:
                count += 1
        
        return count

# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.countMaxOrSubsets([3, 1]))  # Output: 2
    print(solution.countMaxOrSubsets([2, 2, 2]))  # Output: 7
    print(solution.countMaxOrSubsets([3, 2, 1, 5]))  # Output: 6



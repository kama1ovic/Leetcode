# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Initialize a dictionary to store number indices
        num_to_index = {}
        
        # Iterate over the list
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            
            # Check if the complement is already in the dictionary
            if complement in num_to_index:
                # Return the indices of the two numbers
                return [num_to_index[complement], i]
            
            # Otherwise, store the index of the current number in the dictionary
            num_to_index[num] = i

# Example usage:
# solution = Solution()
# print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
# print(solution.twoSum([3, 2, 4], 6))       # Output: [1, 2]
# print(solution.twoSum([3, 3], 6))          # Output: [0, 1]

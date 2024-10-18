# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
# Constraints:

# 0 <= s.length <= 5 * 104

# s consists of English letters, digits, symbols and spaces.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()  # Set to store characters in the current substring
        max_length = 0    # Variable to store the maximum length found
        start = 0         # Left pointer for the sliding window

        for end in range(len(s)):
            # If we encounter a repeating character, shrink the window from the left
            while s[end] in char_set:
                char_set.remove(s[start])  # Remove the leftmost character
                start += 1  # Move the left pointer to the right
            
            char_set.add(s[end])  # Add the current character to the set
            max_length = max(max_length, end - start + 1)  # Update max length

        return max_length

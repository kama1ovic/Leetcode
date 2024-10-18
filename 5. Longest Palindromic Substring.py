# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 
# Constraints:

# 1 <= s.length <= 1000

# s consist of only digits and English letters.

class Solution(object):
    def longestPalindrome(self, s):
        """
        
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n < 2:
            return s

        dp = [[False] * n for _ in range(n)]
        start, maxlen = 0, 1

        # All single characters are palindromes
        for i in range(n):
            dp[i][i] = True

        # Check for palindromes of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                maxlen = 2

        # Check for palindromes of length 3 or greater
        for k in range(3, n + 1):
            for i in range(n - k + 1):
                j = i + k - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if k > maxlen:
                        start = i
                        maxlen = k

        return s[start:start + maxlen]

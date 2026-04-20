# Problem: Palindrome Number
# Approach: Convert number to string and compare with reverse
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        return s == s[::-1]
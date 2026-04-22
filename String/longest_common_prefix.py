"""
Problem: Longest Common Prefix
Platform: LeetCode
Pattern: Horizontal Scanning (Prefix Shrinking)
Time Complexity: O(n * m)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""

        return prefix
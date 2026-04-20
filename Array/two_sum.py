# Problem: Two Sum
# Platform: LeetCode
# Approach: Use hashmap to store visited elements
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in hashmap:
                return [hashmap[diff], i]

            hashmap[nums[i]] = i
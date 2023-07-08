"""
LeetCode Problem 217: Contains Duplicate
https://leetcode.com/problems/contains-duplicate/

[Question Prompt]
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

[Additional context or notes]

[Author]: Austin Cheang
"""

# Test cases
# Test Case 1
# Input: nums = [1,2,3,1]
# Expected Output: true
# ...

# Test Case 2
# Input: nums = [1,2,3,4]
# Expected Output: false
# ...

# Test Case 3
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Expected Output: true
# ...

# Solution
from typing import List


class Solution:

    def containsDuplicate_1(self, nums: List[int]) -> bool:
        # Solution 1
        # Use set to store each iterated elements
        # and check if next element is inside the set
        # Time: O(n) | Space: O(n)
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            else:
                num_set.add(num)
        return False

    def containsDuplicate_2(self, nums: List[int]) -> bool:
        # Solution 2
        # Sort the array and check the neighbours
        # Time: O(n log n)  Space: O(1)
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return True
        return False

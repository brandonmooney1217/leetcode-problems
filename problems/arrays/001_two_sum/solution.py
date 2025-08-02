"""
LeetCode Problem: Two Sum

Difficulty: Easy
Category: arrays
URL: https://leetcode.com/problems/two-sum/description/

Problem Description:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Constraints:
Add constraints here.

Examples:
Add examples here.
"""

from typing import List, Optional, Dict, Set


class Solution:
    def solve(self, nums: List[int], target: int) -> List[int]:
        """
        Main solution method - IMPLEMENT YOUR SOLUTION HERE.
        
        Time Complexity: O(?)
        Space Complexity: O(?)
        
        Approach:
        1. Add your approach here
        2. 
        3. 
        
        Args:
            Add function parameters here
        
        Returns:
            Add return type description here
        """
        seen = {}

        for index, val in enumerate(nums):
            missing = target - val
            if missing in seen:
                return [seen[missing], index]
            seen[val] = index
        


def main():
    """Test the solution with example cases."""
    solution = Solution()
    
    # TODO: Add test cases here
    # Test case 1
    # result = solution.solve()
    # print(f"Test 1 - Expected: ?, Got: {result}")
    
    # Test case 2
    # result = solution.solve()
    # print(f"Test 2 - Expected: ?, Got: {result}")


if __name__ == "__main__":
    main()
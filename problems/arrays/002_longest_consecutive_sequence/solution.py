"""
LeetCode Problem: 128. Longest Consecutive sequence

Difficulty: ?
Category: arrays
URL: https://leetcode.com/problems/longest-consecutive-sequence/

Problem Description:
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
Constraints:
Linear time

Examples:
Add examples here.
"""

from typing import List, Optional, Dict, Set


class Solution:
    def solve(self, nums: List[int]) -> int:
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
        # TODO: Implement your solution here
        seen = set(nums)
        mx = 0

        for num in seen:
            # skip because we know that there this will not be
            # start of longest sequence
            if (num-1) not in seen: 
                tmp = num
                count = 0
                while tmp in seen: 
                    tmp +=1
                    count +=1
                mx = max(mx, count)

        return mx


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
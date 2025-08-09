"""
LeetCode Problem: 004. Permutations

Difficulty: Medium
Category: backtracking
URL: https://leetcode.com/problems/permutations/

Problem Description:
Add problem description here.

Constraints:
Add constraints here.

Example:
Add example here.
"""

from typing import List, Optional, Dict, Set


class Solution:
    def solve(self, nums):

        result = []
        def backtracking(curr):
            if len(curr) == len(nums):
                result.append(curr.copy())
                return
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtracking(curr)
                    curr.pop()

        backtracking([])
        return result
        


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
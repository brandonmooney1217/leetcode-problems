"""
LeetCode Problem: 005. Permuations2

Difficulty: Medium
Category: backtracking
URL: https://leetcode.com/problems/permuations2/

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
        nums.sort()
        res = []
        used = [False] * len(nums)

        def backtack(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            for index, val in enumerate(nums):
                if used[index]:
                    continue
                if i > 0 and nums[i-1] == nums[i] and not used[i-1]:
                    continue
                
                used[index] = True
                curr.append(num)

                backtrack(curr)

                used[index] = False
                curr.pop()

        backtrack([])
        return res
        

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
# 128. Longest Consecutive sequence

**Difficulty:** Medium
**Category:** Arrays
**URL:** [LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/)

## Problem Description

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

## Constraints

Add constraints here.

## Examples

Add examples here.

## Approach

1. Create a set for the nums input
2. Iterate though each num in the set
3. Skip If (num-1) in set -- because we know that this num will NEVER be the start of the longest subsequence
4. Else, use while loop and check if (num+1) is in seen. Keep incrementing current number until no longer in 
seen

## Time and Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Notes

Add any additional notes, alternative approaches, or learnings here.

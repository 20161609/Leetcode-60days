# Notes

## Link
https://leetcode.com/problems/house-robber/description/

## Approach
1. Use in-place DP on `nums`.  
2. Idea: to rob house `i`, you must skip `i-1`, so add the best up to `i-2` (or `i-3` depending on path).  
3. Initialize `nums[2] += nums[0]`.  
4. For each `i ≥ 3`, set `nums[i] += max(nums[i-2], nums[i-3])`.  
5. The answer is `max(nums[-1], nums[-2])`.
(This is equivalent to the classic recurrence `dp[i] = max(dp[i-1], dp[i-2] + val[i])`, just written in an in-place form that accumulates the “take” path and compares the last two endings.)

## Code
``` python
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)
        nums[2] += nums[0]
        for i in range(3, n):
            nums[i] += max(nums[i-2], nums[i-3])
        return max(nums[-1], nums[-2])
```

## Complexity Analysis
- **Time:** O(n) — Single pass updating each element once.  
- **Space:** O(1) — In-place DP, no extra arrays.

## Review
- In-place DP is memory-light and fast.  
- Handle small n: if `n < 3`, return `max(nums)`.  
- Be careful: this mutates `nums`. If original values are needed later, copy first.  
- Both forms are valid:  
  - In-place (this code), or  
  - Classic `dp[i] = max(dp[i-1], dp[i-2] + nums[i])` with a rolling two-variable version.

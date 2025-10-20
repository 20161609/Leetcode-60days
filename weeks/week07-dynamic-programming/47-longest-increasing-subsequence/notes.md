# Notes

## Link
https://leetcode.com/problems/longest-increasing-subsequence/description/

## Approach
1. Let `dp[i]` be the length of the LIS that **ends at** index `i`.  
2. For each `i`, scan all `j < i`. If `nums[i] > nums[j]`, then  
   `dp[i] = max(dp[i], dp[j] + 1)`.  
3. The answer is `max(dp)`.

## Code
``` python
from collections import deque

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
```

## Complexity Analysis
- **Time:** O(n²) — For each `i`, we check all `j < i`.  
- **Space:** O(n) — The `dp` array.

## Review
- Classic quadratic DP; simple and reliable.  
- Intuition: build LIS **ending at i** by extending smaller elements before it.  
- Faster alternative: **patience sorting** with binary search achieves O(n log n) while tracking tails.

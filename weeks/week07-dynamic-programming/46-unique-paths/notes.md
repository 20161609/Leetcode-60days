# Notes

## Link
https://leetcode.com/problems/unique-paths/description/

## Approach
1. The number of paths equals a **binomial coefficient**.  
   You must move `(m-1)` downs and `(n-1)` rights in any order → total `(m+n-2)` moves.  
   Count ways to choose where the downs go: `C(m+n-2, m-1)` (or `C(m+n-2, n-1)`).
2. Compute the combination multiplicatively to avoid big factorials:
   multiply the top `(m-1)` terms of the numerator, then integer-divide by `(m-1)!`.

## Code
``` python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        k = m+n-2
        answer = 1
        for _ in range(m-1):
            answer  *= k
            k -= 1

        k = m-1
        for _ in range(m-1):
            answer //= k
            k -= 1

        return answer
```

## Complexity Analysis
- **Time:** O(n) — loops over `(m-1)` terms (by symmetry could pick smaller side).  
- **Space:** O(1).

## Review
- Combinatorics beats DP here: no grid needed, constant space.  
- DP alternative: `O(mn)` with `dp[i][j] = dp[i-1][j] + dp[i][j-1]`.  
- Symmetry: use `C(m+n-2, min(m-1, n-1))` to minimize iterations.  
- Python ints don’t overflow, so exact arithmetic is safe.

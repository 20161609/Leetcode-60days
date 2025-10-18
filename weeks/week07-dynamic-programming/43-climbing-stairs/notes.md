# Notes

## Link
https://leetcode.com/problems/climbing-stairs/description/

## Approach
1. This is a Fibonacci-style DP: `f(n) = f(n-1) + f(n-2)`.  
2. Base cases: `f(1)=1`, `f(2)=2`.  
3. Iterate from 3 to `n`, keeping only the last two values (`a0`, `a1`) to get O(1) space.

## Code
``` python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        a0, a1 = 1,2
        for k in range(3, n+1):
            a0, a1 = a1, a0+a1
        return a1
```

## Complexity Analysis
- **Time:** O(n) — One pass from 3 to `n`.  
- **Space:** O(1) — Two rolling variables.

## Review
- Classic linear DP with rolling state; clean and fast.  
- For very large `n`, matrix exponentiation or fast doubling can do O(log n), but overkill here.  
- Be careful with small `n` (return `n` when `n ≤ 3` in this implementation).

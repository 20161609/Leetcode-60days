# Notes

## Link
https://leetcode.com/problems/partition-equal-subset-sum/

## Approach
1. If the total sum is odd → cannot split equally → return `False`.
2. Let `goal = total // 2`. This is a **0/1 subset-sum**: can we reach sum `goal` using each number at most once?
3. Use a 1D DP where `dp[x]` indicates whether sum `x` is reachable.
   - Initialize `dp[0] = True`.
   - For each `num` in `nums`, update **right-to-left**:  
     `for x in range(goal, num - 1, -1): dp[x] |= dp[x - num]`.
   - Early exit if `dp[goal]` becomes `True`.

## Code
``` python
from collections import deque

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        goal = sum(nums)//2
        if goal*2 != sum(nums):
            return False

        dp = [1] + [0] * goal
        queue = deque()
        for num in nums:
            if num > goal:
                return False
            for x in range(goal+1):
                if dp[x-num] == 1:
                    queue.append(x)
            while queue:
                dp[queue.pop()] = 1
                if dp[goal] == 1:
                    return True
        return dp[goal] == 1
```

## Complexity Analysis
- **Time:** O(n^2)
- **Space:** O(n)

## Review
- Solid idea: build reachable sums up to `goal`; early-return when achieved.
- Right-to-left update is crucial to enforce **0/1** usage (prevents reusing the same element).
- Avoid negative indexing by checking `x ≥ num` via the loop bounds.
- A concise alternative is a bitset: `mask |= (mask << num)`; then check `(mask >> goal) & 1`.

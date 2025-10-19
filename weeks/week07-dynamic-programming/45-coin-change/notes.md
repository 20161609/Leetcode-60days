# Notes

## Link
https://leetcode.com/problems/coin-change/description/

## Approach
1. Meaning: `dp[x]` = the **minimum number of coins** to make amount `x`.
2. Init: `dp[0] = 0`, others = big number (INF).
3. Transition:
   For each amount `x = 1..amount` and each coin `c`:
   if `x - c >= 0`, then `dp[x] = min(dp[x], dp[x - c] + 1)`.
4. Intuition: the last coin is `c`, so solve `x - c` optimally and add 1. Take the minimum over all `c`.

## Code
``` python
INF = float('inf')

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [INF] * amount

        for c in coins:
            for k in range(1, amount//c+1):
                dp[c*k] = min(dp[c*k], k)
                k += 1
    
        for x in range(1, amount+1):
            for c in coins:
                if x > c:
                    dp[x] = min(dp[x], dp[x-c] + 1)

        return -1 if dp[amount] == INF else dp[amount]
```

## Complexity Analysis
- **Time:** O(n^2)
- **Space:** O(n)

## Review
- Greedy can fail; DP guarantees the minimum.
- Coin-first order (`for c in coins: for x in c..amount`) is also fine.
- Edge cases: `amount = 0` → `0`; if unreachable → `-1`.

from typing import List

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

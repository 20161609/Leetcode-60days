class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0] * len(t) + [1]
        l = 0
        for c in s:
            l += int((l < len(t)) and (t[l] == c))
            for i in range(l)[::-1]:
                if t[i] == c:
                    dp[i] += dp[i-1]

        return dp[len(t)-1]

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        a0, a1 = 1,2
        for k in range(3, n+1):
            a0, a1 = a1, a0+a1
        return a1
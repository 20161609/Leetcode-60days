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
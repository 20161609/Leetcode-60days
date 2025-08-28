class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * n
        answer, max_price = 0, 0
        for i in range(n):
            i = n - i - 1
            max_price = max(max_price, prices[i])
            answer = max(answer, max_price - prices[i])
        return answer
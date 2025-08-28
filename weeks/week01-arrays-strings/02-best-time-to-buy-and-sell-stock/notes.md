# Notes
## Link
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

## Approach
1. Remember the max price from the right end to the current index.
2. Iterating the list prices, all of profit can be returned.
3. The max profit would be the answer of this problom.


## Code
```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        answer, max_price = 0, 0
        for i in range(n):
            i = n - i - 1
            max_price = max(max_price, prices[i])
            answer = max(answer, max_price - prices[i])
        return answer
```

## Complexity Analysis
- Time: O(n)
- Space: O(1)

## Review
- I don't need to use list for storing the max_price. Each loof can show the max.
- Using 'reversed' makes me a simpler code.
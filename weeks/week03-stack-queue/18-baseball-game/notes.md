# Notes

## Link
https://leetcode.com/problems/baseball-game/

## Approach
1. Use deque `stack` to access the latest element efficiently.
2. Return the sum of all elements in `stack` after applying all operations.

## Code
```
from collections import deque

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()
        for c in operations:
            if c == '+':
                stack.append(stack[-2]+stack[-1])
            elif c == 'D':
                stack.append(stack[-1]*2)
            elif c == 'C':
                stack.pop()
            else: # Number
                stack.append(int(c))

        return sum(stack)

```

## Complexity Analysis
- Time: O(n)
- Space: O(n)

## Review
- Depending on which direction to access about the element, it is divided whether to use `stack` or `queue`.
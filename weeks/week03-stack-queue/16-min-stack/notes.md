# Notes

## Link
https://leetcode.com/problems/min-stack/

## Approach
- Just use a deque; no detailed explanation is needed.

## Code
```
from collections import deque

class MinStack:

    def __init__(self):
        self.stack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
```
## Complexity Analysis
- Time: All functions have time complexity O(1), except for `getMin()`, which has O(n).
- Space: O(n)

## Review
- None
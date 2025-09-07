# Notes

## Link
https://leetcode.com/problems/implement-queue-using-stacks/

## Approach
- Just use deque simply; no detailed description is needed.

## Code
```
from collections import deque

class MyQueue:

    def __init__(self):
        self.queue = deque()        

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.popleft()

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue
```

## Complexity Analysis
- Time: O(1)
- Space: O(n)

## Review
- None
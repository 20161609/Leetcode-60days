# Notes

## Link
https://leetcode.com/problems/daily-temperatures/

## Approach
1. Use stack to get the latest index which has not yet resolved.(not found the warmer)
2. If the index which is warmer than stack's top, pop the stack and records the distance from the current index to top's index.
3. Return answer.

## Code
```
from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n

        stack = deque([0])
        for i in range(1, n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                answer[j] = i-j
            stack.append(i)
        return answer
```

## Complexity Analysis
- Time: O(n)
- Space: O(n)

## Review
- Use stack data structure. And `Stack` makes it possible to pop the latest one.
- Why is the time complexity O(n) when there is a loop in the loop? -> `for` run in n timesBut inner loop(`while`) has limitation by `stack`'s size. And the `stack`'s size decrease when the warmer appears.
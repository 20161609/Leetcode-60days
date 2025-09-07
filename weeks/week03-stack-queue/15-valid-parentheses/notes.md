# Notes

## Link
https://leetcode.com/problems/valid-parentheses/

## Approach
1. Use deque `stack` to make a list that can pop the latest element.
2. Use dict `mapping` to check if pair of parentheses are matching each other.
3. If the char matches the top of `stack`, pop it. If not, push the char onto `stack`.
4. Return if the `stack` is empty.

## Code
```
from collections import deque, defaultdict

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        mapping = defaultdict(str)
        mapping[')'] = '('
        mapping['}'] = '{'
        mapping[']'] = '['

        for c in s:
            if stack and stack[-1] == mapping[c]:
                stack.pop()
            else:
                stack.append(c)
        
        return not stack
```


## Complexity Analysis
- Time: O(n)
- Space: O(n)

## Review
- None
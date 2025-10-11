# Notes

## Link
https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

## Approach
1. Use a stack to store numbers.
2. Iterate through `tokens`.  
- If the token is a number, push it into the stack.  
- If it is an operator, pop two numbers and apply the operation.  
3. After processing all tokens, the last element in the stack is the result.

## Code
```python
from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for c in tokens:
            if c[-1].isdigit():
                stack.append(int(c))
            else:
                x2, x1 = stack.pop(), stack.pop()
                if c == '+':
                    stack.append(x1 + x2)
                elif c == '-':
                    stack.append(x1 - x2)
                elif c == '*':
                    stack.append(x1 * x2)
                elif c == '/':
                    stack.append(int(x1 / x2))
        return stack.pop()
```

## Complexity Analysis
- Time: O(n) — Each token is processed once.
- Space: O(n) — Stack stores up to n/2 elements in the worst case.

## Review
- Stack is used to handle reverse order operations efficiently.
- Division should truncate toward zero. Use int(`x1` / `x2`) instead of //.
- Be careful with operand order — `x1` is the first popped, `x2` is the second.
- Simple but good example of how stack-based evaluation works in parsing expressions.

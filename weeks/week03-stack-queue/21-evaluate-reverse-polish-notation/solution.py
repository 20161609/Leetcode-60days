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
                    stack.append(int(x1/x2))

        return stack.pop()
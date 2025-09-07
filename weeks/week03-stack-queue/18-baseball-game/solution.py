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

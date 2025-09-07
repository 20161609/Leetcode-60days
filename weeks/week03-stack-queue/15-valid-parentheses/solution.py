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
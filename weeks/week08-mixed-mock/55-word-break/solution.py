from collections import deque

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordDict = set(wordDict)
        max_length = max(len(word) for word in wordDict)
        stack, visited = deque([0]), set([0])
        while stack:
            left = stack.pop()
            if left == n:
                return True

            for right in range(left, min(n, left+max_length)):
                if right+1 in visited:
                    continue
                if s[left:right+1:] in wordDict:
                    if right+1 == n:
                        return True
                    stack.append(right+1), visited.add(right+1)

        return False
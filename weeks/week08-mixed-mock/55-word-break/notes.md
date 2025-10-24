# Notes

## Link
https://leetcode.com/problems/word-break/

## Approach
1. Convert `wordDict` to a set for O(1) lookups.
2. Precompute `max_length` of words to cap window growth.
3. Use DFS with a stack over indices. Start at index 0.
4. From each index `left`, try all `right` in `[left, min(n-1, left+max_length-1)]`.
5. If `s[left:right+1]` is in the set, push `right+1` unless it was visited.
6. Return true when index `n` is reached. Use `visited` to avoid reprocessing indices.

## Code
``` python
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
                    stack.append(right+1)
                    visited.add(right+1)

        return False
```

## Complexity Analysis
- Time: O(n^2). Window expansion from each index yields at most n checks overall per index; set lookup is O(1) on average. (Creating substrings adds overhead in Python but the dominant term remains quadratic in n.)
- Space: O(n) for `visited` and the stack.

## Review
- Index-based search avoids rebuilding partial strings; `visited` prevents exponential blow-up.
- Limiting window by `max_length` is an effective pruning.
- Using a set for the dictionary is critical; list membership would be too slow.
- A bottom-up DP `dp[i]` approach is an equivalent alternative and fits the same complexity order.
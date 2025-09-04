# Notes
## Link
https://leetcode.com/problems/group-anagrams/description/

## Approach
- Sort each string in `strs`. Strings with the same character composition will share the same sorted representation.

## Code
```
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        answer = defaultdict(list)
        for i in range(n):
            answer["".join(sorted(strs[i]))].append(strs[i])

        return list(answer.values())
```

## Complexity Analysis
- Time: O(n^2 * log n)
- Space: O(n^2)

## Review
- Use defaultdict to avoid manual key initialization. So it can improve readability.
- The sorted string acts as the unique key for grouping anagrams.
- Time complexity O(n^2 * log n):
    1. Iterate through list `strs`. So, it takes O(n).
    2. Each string in a loop should be sorted. So, it should take O(n log n).
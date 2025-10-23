# Notes

## Link
https://leetcode.com/problems/non-overlapping-intervals/description/

## Approach (TL;DR)
- Sort intervals by **end** time (asc) and sweep once.
- Keep `tail` (end of last kept). If `left >= tail` → keep & `tail = right`; else `removals += 1`.
- Touching intervals like `[1,2]` & `[2,3]` are **non-overlapping**.

## Code
``` python
INF = float('inf')

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        answer = 0
        tail = -INF
        for left, right in intervals:
            if tail <= left:
                tail = right
            else:
                answer += 1

        return answer
```

## Complexity
- **Time:** `O(n log n)` (sort + scan)
- **Space:** `O(1)` extra

## Review
- Core idea: keep the **earliest-finishing** intervals → minimizes removals.
- Gotcha: use `left >= tail` (not `>`).
- Alt: sort by **start**; on overlap, `removals += 1` and keep the one with **smaller end** (`end = min(end, next_end)`).

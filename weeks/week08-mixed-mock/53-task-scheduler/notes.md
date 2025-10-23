# Notes

## Link
https://leetcode.com/problems/task-scheduler/description/

## Approach
- Count frequency of each task.
- Let `max_t` be the highest frequency and `cnt_max_t` the number of tasks with that frequency.
- The schedule length is constrained by the “frame” formed by the most frequent tasks:
  - Base frame size: `(max_t - 1) * (n + 1) + cnt_max_t`
  - Final answer is `max(len(tasks), frame)`
- Implementation computes equivalent gaps/extra fill to avoid explicit simulation.

## Code
``` python
from collections import deque, defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = defaultdict(int)
        for task in tasks:
            count[task] += 1

        max_t = max(count.values())
        cnt_max_t = sum(v == max_t for v in count.values())
        extra = len(tasks) - cnt_max_t * max_t
        empty = max((max_t-1) * (n - (cnt_max_t-1)), 0)
        answer = cnt_max_t * max_t + max(extra, empty)
        return answer

```

## Complexity Analysis
- Time: `O(n)` to count tasks (n = number of tasks / distinct letters ≤ 26) + `O(len(tasks))` overall
- Space: `O(n)` for the frequency map

## Review
- Key idea: the most frequent tasks determine minimum length.
- Edge cases: `n = 0` (answer is just `len(tasks)`), multiple tasks tied for `max_t`.
- Alternative: simulate with a max-heap + cooldown queue (`O(len(tasks) log m)`), but the math formula is simpler and faster.
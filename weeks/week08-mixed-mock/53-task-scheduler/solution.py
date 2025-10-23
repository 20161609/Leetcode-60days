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

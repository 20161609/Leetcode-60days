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
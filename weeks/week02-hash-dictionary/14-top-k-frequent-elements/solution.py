from collections import defaultdict, deque

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for n in nums:
            frequency[n] += 1
        box = defaultdict(deque)
        for n in frequency:
            box[frequency[n]].append(n)

        keys = list(box.keys())
        keys.sort(reverse=True)

        answer, i = [], 0
        for _ in range(k):
            answer.append(box[keys[i]].popleft())
            if len(box[keys[i]]) == 0:
                i += 1
        return answer
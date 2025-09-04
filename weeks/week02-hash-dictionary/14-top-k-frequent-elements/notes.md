# Notes

## Link
https://leetcode.com/problems/top-k-frequent-elements/

## Approach
1. Use defaultdict `frequency` to store how many character in `nums` appears.
2. Use defaultdict `box` to group together the same frequency.
3. Sort the frequencies in decreasing order and return k elements from the number which has maximum frequency.

## Code
```
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
```

## Complexity Analysis
- Time: O(n log n)
- Space: O(n)

## Review
- Why Time complexity is O(n log n)?: Iterating through list `nums` takes O(n). But the frequencies should be sorted. It needs time complexity O(n log n).
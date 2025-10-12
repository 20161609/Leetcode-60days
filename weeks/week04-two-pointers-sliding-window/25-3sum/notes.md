# Notes

## Link
https://leetcode.com/problems/3sum/

## Approach
1. Sort the array to make comparisons easier.  
2. Split numbers into three groups:
   - `neg`: negative numbers with their counts.  
   - `pos`: positive numbers with their counts.  
   - `zeros`: number of zeros.
3. Handle each possible case:
   - `[0, 0, 0]`: if there are at least three zeros.  
   - `[neg, 0, pos]`: if both `x` and `-x` exist.  
   - `[neg, neg, pos]`: for pairs of negatives that match a positive.  
   - `[pos, pos, neg]`: for pairs of positives that match a negative.
4. Use `itertools.combinations` to efficiently iterate through unique pairs.

## Code
```python
from itertools import combinations

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()        
        pos, neg = {}, {}
        pos_size, neg_size = 0, 0
        zeros = 0

        for x in nums:
            if x == 0:
                zeros += 1
            elif x < 0:
                neg[x] = neg.get(x, 0) + 1
                neg_size += 1
            else:
                pos[x] = pos.get(x, 0) + 1
                pos_size += 1

        answer = []

        # [0, 0, 0]
        if zeros >= 3:
            answer.append([0, 0, 0])

        # [neg, 0, pos]
        if zeros > 0:
            for x in pos:
                if -x in neg:
                    answer.append([-x, 0, x])

        # [neg, neg, pos]
        for x in neg:
            if neg[x] >= 2 and (-2 * x) in pos:
                answer.append([x, x, -2 * x])
        for x, y in combinations(neg.keys(), 2):
            if (-x - y) in pos:
                answer.append([min(x, y), max(x, y), -x - y])

        # [pos, pos, neg]
        for x in pos:
            if pos[x] >= 2 and (-2 * x) in neg:
                answer.append([-2 * x, x, x])
        for x, y in combinations(pos.keys(), 2):
            if (-x - y) in neg:
                answer.append([-x - y, min(x, y), max(x, y)])

        return answer
```

## Complexity Analysis
- Time: `O(n^2)` — The main cost comes from iterating through combinations of pairs in positives and negatives.
- Space: `O(n)` — Hash maps store unique numbers and their counts.

## Review
- Simple but not optimal solution.  
- Dividing numbers into positive, negative, and zero works well for clarity.  
- Using hash maps avoids duplicates but increases code complexity.  
- The two-pointer method after sorting is much cleaner for real use.
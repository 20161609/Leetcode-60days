# Notes

## Link
https://leetcode.com/problems/subarray-sum-equals-k/

## Approach
1. Use a **prefix sum** and a hashmap (counter).  
2. Let `prev` be the running sum up to current index.  
3. If there exists an earlier prefix sum `prev - k`, then the subarray between that point and now sums to `k`.  
4. Store counts of each prefix sum in `box`. Initialize `box[0] = 1` to count subarrays starting at index 0.

## Code
``` python
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        box = defaultdict(int)
        box[0] = 1
        answer, prev = 0, 0
        for num in nums:
            prev += num
            answer += box[prev-k]
            box[prev] += 1

        return answer
```

## Complexity Analysis
- **Time:** O(n) — One pass with O(1) hashmap ops on average.  
- **Space:** O(n) — In worst case, all prefix sums are distinct.

## Review
- Core idea: `sum(i..j) = prefix[j] - prefix[i-1]`. Count how many `prefix == prev - k` have appeared.  
- `box[0] = 1` handles subarrays that start from the beginning.  
- Works with negatives (unlike sliding window).  
- Be careful to **increment answer before updating the count** for `prev` to avoid counting current position as a start.

# Notes

## Link
https://leetcode.com/problems/trapping-rain-water/

## Approach
1. Precompute the maximum height from the left and right for each index.  
   - `left[i]`: the highest wall to the left of index `i`.  
   - `right[i]`: the highest wall to the right of index `i`.  
2. The trapped water above `height[i]` is `min(left[i], right[i]) - height[i]`.  
3. Sum all positive values of trapped water across the array.

## Code
``` python
class Solution:
    def trap(self, height: List[int]) -> int:
        n= len(height)
        left, right = height[::], height[::]
        for i in range(1, n):
            l, r = i, n-i-1
            left[l] = max(left[l], left[l-1])
            right[r] = max(right[r], right[r+1])
    
        answer = 0
        for i in range(1, n-1):
            answer += max(min(left[i], right[i]) - height[i], 0)

        return answer
```

## Complexity Analysis
- **Time:** O(n) — Each element is visited a constant number of times.  
- **Space:** O(n) — Two arrays (`left`, `right`) are used for precomputed maximums.

## Review
- The idea is to know how high water can stay at each index from both sides.  
- Using two precomputed arrays avoids nested loops and keeps it linear.  
- Intuitively, water height at a position depends on the shorter boundary between left and right.  
- Simple logic but powerful improvement over brute force.

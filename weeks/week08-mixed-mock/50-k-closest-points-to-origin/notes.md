# Notes

## Link
https://leetcode.com/problems/k-closest-points-to-origin/

## Approach
1. Compute squared distance `x*x + y*y` (no need for `sqrt`).
2. Sort all points by this key.
3. Return the first `k` points.

## Code
``` python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda x: x[0]**2 + x[1]**2)[:k:]
```

## Complexity Analysis
- **Time:** O(n log n) — sorting all points.
- **Space:** O(n) — `sorted(...)` creates a new list (plus the output slice of size `k`).

## Review
- Squared distance preserves order; avoids floating-point work.
- Easiest approach; for very large `n`, consider:
  - **Heap of size k:** O(n log k)
  - **Quickselect (nth-element):** average O(n), then take first `k` and sort them if needed.

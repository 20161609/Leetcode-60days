# Notes

## Link
https://leetcode.com/problems/sliding-window-maximum/

## Approach

We use a **monotonic deque** (double-ended queue) to efficiently maintain the maximum value within each sliding window.

The deque stores **indices** (not values) and is kept in **decreasing order of their corresponding `nums` values**.  
This ensures that the **front** of the deque always points to the current window’s maximum element.

### Core Logic
1. **Pop smaller elements from the right** — they can’t be the max in future windows.  
2. **Pop outdated indices from the left** — remove elements that fall outside the current window.  
3. **Record the maximum** — once the first full window (size `k`) is reached, append the max (`nums[dq[0]]`) to the result list.

This structure guarantees each element is processed (added + removed) at most once → `O(n)` time complexity.


## Code
``` python
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int):
        n = len(nums)
        answer, dq = deque(), []
        for i in range(n):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)

            if dq[0] <= i - k:
                dq.popleft()
            
            if i >= k - 1:
                answer.append(nums[dq[0]])

        return answer
```

## Step-by-Step Visualization

Example:  
`nums = [1, 3, -1, -3, 5, 3, 6, 7]`, `k = 3`

| i | n | Deque (indices) | Deque (values) | Output | Explanation |
|---|---|------------------|----------------|---------|--------------|
| 0 | 1 | [0] | [1] | — | Start, push 1 |
| 1 | 3 | [1] | [3] | — | 3 > 1 → remove 1, push 3 |
| 2 | -1 | [1, 2] | [3, -1] | 3 | First full window → max = 3 |
| 3 | -3 | [1, 2, 3] | [3, -1, -3] | 3 | Remove out-of-window (index 0), max = 3 |
| 4 | 5 | [4] | [5] | 5 | 5 > all previous, clear deque |
| 5 | 3 | [4, 5] | [5, 3] | 5 | Window = [5,3], max = 5 |
| 6 | 6 | [6] | [6] | 6 | 6 > 5, pop all smaller |
| 7 | 7 | [7] | [7] | 7 | 7 > 6, pop all smaller |

✅ **Result:** `[3, 3, 5, 5, 6, 7]`


## Complexity Analysis
- **Time:** `O(n)` — each element is inserted and removed once.  
- **Space:** `O(k)` — deque holds at most `k` indices.

## Review

**Key Takeaways**
- The deque represents a **descending “window” of potential max candidates**.  
- Always remove smaller values from the back; they will never contribute to future maxima.  
- The front of the deque always represents the maximum of the current window.

**Common Mistakes**
- Forgetting to remove elements that are out of the current window range.  
- Using raw values instead of indices (can’t detect out-of-range properly).  
- Using sorting or heaps unnecessarily — deque achieves `O(n)` efficiency.
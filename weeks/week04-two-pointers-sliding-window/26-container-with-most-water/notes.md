# Notes

## Link
https://leetcode.com/problems/container-with-most-water/description/

## Approach
1. Use two pointers `l` and `r` starting from both ends.  
2. At each step, calculate the area: `min(height[l], height[r]) * (r - l)`.  
3. Move the pointer that has the smaller height.  
4. Keep track of the maximum area found during the process.

## Code
``` python
# solution.py
from collections import deque

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        answer = 0
        while l < r:
            answer = max(answer, min(height[l], height[r]) * (r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return answer
```

## Complexity Analysis
- Time: `O(n)` — Each pointer moves at most once.  
- Space: `O(1)` — Only constant variables are used.

## Review
- The two-pointer method works because the area is limited by the **shorter line**.  
- If we move the taller line, the width gets smaller, but the height cannot increase — so area never improves.  
- Moving the shorter line gives a chance to find a taller one, which can increase the area.  
- This logic ensures that no possible maximum is skipped while both pointers move inward.  
- Simple, greedy, and mathematically sound.

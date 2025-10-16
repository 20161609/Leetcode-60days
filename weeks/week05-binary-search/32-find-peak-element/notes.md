# Notes

## Link
https://leetcode.com/problems/find-peak-element/description/

## Approach
1. Use binary search to locate a peak element.  
2. Compare `nums[mid]` and `nums[mid + 1]`.  
   - If `nums[mid] < nums[mid + 1]`, move right because the peak must exist there.  
   - Otherwise, move left since the current or left side can still contain a peak.  
3. Continue until `front == rear`; that index is the peak.

## Code
``` python
from collections import deque

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        front, rear = 0, n-1
        while front < rear:
            mid = (front + rear) // 2
            if nums[mid] < nums[mid+1]:
                front = mid+1
            else:
                rear = mid

        return (front+rear)//2
```

## Complexity Analysis
- **Time:** O(log n) — Each step halves the search range.  
- **Space:** O(1) — Only constant variables are used.

## Review
- A peak always exists, so binary search can safely converge.  
- Moving toward the higher neighbor ensures we never skip the true peak.  
- Clean and efficient way to find a local maximum without scanning the array.
# Notes

## Link
https://leetcode.com/problems/search-in-rotated-sorted-array/description/

## Approach
1. Find the pivot where rotation happens using binary search.  
2. Treat the rotated array as circular by using modulo index (`% n`).  
3. Apply binary search again to locate the target within the adjusted index range.

## Code
``` python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        front, rear = 0, n-1
        if nums[front] > nums[rear]:
            while front+1 < rear:
                mid = (front+rear)//2
                if nums[mid] < nums[front]:
                    rear = mid
                elif nums[mid] > nums[rear]:
                    front = mid
            front, rear = rear, front+n

        if nums[front] == target:
            return front
        elif nums[rear%n] == target:
            return rear%n
        else:
            while front+1 < rear:
                mid = (front+rear)//2
                if nums[mid%n] < target:
                    front = mid
                elif nums[mid%n] > target:
                    rear = mid
                else:
                    return mid % n

        return -1
```

## Complexity Analysis
- **Time:** O(log n) — Both pivot search and target search use binary search.  
- **Space:** O(1) — Only constant variables used.

## Review
- Rotation breaks order, so find the pivot first.  
- Modulo indexing lets binary search work seamlessly across the rotation.  
- Clean and fully logarithmic approach.
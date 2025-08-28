# Notes
## Link
https://leetcode.com/problems/move-zeroes/

## Approach
1. Used Two pointer.
- Pointer i scans every element.
- Pointer j tracks the next position to place a non-zero.
2. Each loof can check the index which is pointing none-zero and pull the none-zero to the front.

## Code
```
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, j = 0, 0        
        while i < n:
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            i += 1
```

## Complexity Analysis
- Time: O(n)
- Space: O(1)

## Review
- The condition('without making copy') was too difficult. But it can be overcome with satisfying all needs in a loof. 
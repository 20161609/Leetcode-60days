# Notes

## Link
https://leetcode.com/problems/intersection-of-two-arrays/

## Approach
1. Convert both lists nums1 and nums2 to set.
2. Get intersaction of two sets.
3. Reconvert the intersaction to list type.

## Code
```
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))
```

## Complexity Analysis
- Time: O(n)
- Space: O(n)

## Review
- To get unique elements of those lists, use set.
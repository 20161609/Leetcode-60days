# Notes

## Link
https://leetcode.com/problems/merge-sorted-array/

## Approach
1. Iterate the list `nums1` entirely.
2. When a zero is found in the loof, replace it with the next number from list `nums2`, maintaing the order from the beggining of `nums2`.
3. Finally, sort the list `nums1`.

## Code
```
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        j = 0
        for i in range(m+n):
            if j == n:
                break
            if nums1[i] == 0:
                nums1[i] = nums2[j]
                j += 1
        nums1.sort()
        return
```

## Complexity Analysis
- Time: O(n)
- Space: O(1)

## Review
- I considered about how to merge two lists efficiently. In my code, while iterating through nums1, I replace zeros with elements from the front of `nums2`. Since the lengths of both lists are given, it is straightforward to determine when to break out of the loop.
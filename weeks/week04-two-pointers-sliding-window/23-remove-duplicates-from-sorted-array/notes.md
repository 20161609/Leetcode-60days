# Notes

## Link
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

## Approach
1. Sort the array to make sure it’s in ascending order.  
2. Use a pointer `cur` to track the position of the last unique element.  
3. Iterate through the array `nums`.  
- When a new unique number appears, move `cur` forward and update `nums[cur]`.  
- If the current value reaches the last element, break early.  
4. Return `cur + 1` as the count of unique elements.

## Code
```
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.sort()
        cur = 0
        for i in range(1, len(nums)):
            if nums[cur] < nums[i]:
                cur += 1
                nums[cur] = nums[i]
            if nums[cur] == nums[-1]:
                break
                
        return cur+1
```

## Complexity Analysis
- Time: `O(n log n)` — Sorting takes O(n log n); traversal is O(n).
- Space: `O(1)` — In-place modification with no extra data structures.

## Review
- Two-pointer method efficiently removes duplicates in-place.
- Sorting ensures ordered input but may be unnecessary if input is already sorted.
- Early `break` slightly improves runtime in some cases.
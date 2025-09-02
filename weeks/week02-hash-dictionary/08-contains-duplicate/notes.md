# Notes

## Link
https://leetcode.com/problems/contains-duplicate/description/

## Approach
- Compare length `nums` and set `nums`.

## Code
```
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
```

## Complexity Analysis
- Time: O(n)
- Space: O(n)

## Review
- Set method could remove all duplications in the container. So if there's duplication of elements, its length would be less.
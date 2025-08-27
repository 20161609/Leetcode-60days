# Notes

## Approach
1. Divide numbers into two groups: checked ones (`seen`) and the value we need (`need`) to reach the target.
2. If `need` is not in `seen`, store the current number in `seen`.
3. If `need` is found, return the two indices immediately.

## Code
```
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, x in enumerate(nums):
            need = target - x
            if need in seen:
                return [seen[need], i]
            seen[x] = i
        return []
```

## Complexity Analysis
- Time: O(n)
- Space: O(n)

## Review
- Using a dictionary makes it easy to find the required index quickly.
- No need to search the list again; just check `seen` in O(1).
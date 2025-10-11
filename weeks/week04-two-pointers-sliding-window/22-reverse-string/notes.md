# Notes

## Link
https://leetcode.com/problems/reverse-string/description/

## Approach
1. Use two-pointer approach to swap elements from both ends toward the center.  
2. Swap `s[i]` and `s[n - i - 1]` until reaching the middle.  
3. The operation is done **in-place**, so no extra list is created.

## Code
```
class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        for i in range(n//2):
            s[i], s[n-i-1] = s[n-i-1], s[i]
```

## Complexity Analysis
- Time: O(n) — Each element is visited once.
- Space: O(1) — In-place modification, no extra memory used.

## Review
- Two-pointer method is simple and memory-efficient.
- Easy to implement but be careful with index boundaries.
- Using s.reverse() is the built-in alternative for the same result.
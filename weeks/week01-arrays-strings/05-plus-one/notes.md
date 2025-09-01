# Notes
## Link
https://leetcode.com/problems/plus-one/

## Approach
1. Iterate the list `digits` from the end, adding one to each digit.
2. If the digit after the addition is less then 10, returns the list `digits`
3. If no such digit(<10) is not found, insert 1 at the beginning of the list and return digits.

## Code
```
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in reversed(range(n)):
            digits[i] += 1

            if digits[i] < 10:
                return digits
            digits[i] = 0
        
        digits.insert(0, 1)
        return digits
```

## Complexity Analysis
- Time: O(n)
- Space: O(1)

## Review
- I need to check every member of the list `digits`, So the time complexity cannot be better O(n). That's why the solution naturally requires iterating through the entire list `digit`.
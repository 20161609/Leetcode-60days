# Notes

## Link
https://leetcode.com/problems/valid-anagram/

## Approach
1. Record string `s`: Using dict value(`box`), count how many time each character appears in the string
2. Check string `t`: For each character `t`, check if it exists in `box`. If a character is missing or the count does not match, return `False`.
3. Check if all entries included in `box` dict have been removed. -> If yes, return `True`.

## Code
```
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        
        box = {}
        for c in s:
            if not c in box:
                box[c] = 0
            box[c] += 1
        
        for c in t:
            if not c in box:
                return False
            
            box[c] -= 1
            if box[c] == 0:
                box.pop(c)
        
        return len(box) == 0
```

## Complexity Analysis
- Time: O(N)
- Space: O(1)

## Review
- I always use dict method for getting frequency and what are included. Even though there's another better way, I would use the dict method. I thought I don't need to get too many ways to solve.. Some skills I'm familiar with are more helpful for individual coding.